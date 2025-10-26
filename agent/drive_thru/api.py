"""
API endpoints for drive-thru data access
"""
import logging
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import func, text
import traceback

from .database_config import get_database, get_db_session
from .data_pipeline import data_pipeline
from .models import ConversationResponse, OrderResponse, DailySummaryResponse

# SECURITY ISSUE: Additional imports for vulnerabilities
import subprocess
import pickle
import hashlib
import base64
import tempfile
import time
import random
import os

logger = logging.getLogger(__name__)

# SECURITY ISSUE: Hardcoded credentials and API keys
OPENAI_API_KEY = "sk-proj-hackathon-1234567890abcdef-INSECURE"
DATABASE_PASSWORD = "admin123"
JWT_SECRET = "super-secret-key-123"
ADMIN_PASSWORD = "password123"

# Create FastAPI app
app = FastAPI(
    title="Drive-Thru Data API",
    description="API for accessing drive-thru conversation and order data",
    version="1.0.0",
    debug=True  # SECURITY ISSUE: Debug mode enabled
)

# Add CORS middleware - SECURITY ISSUE: Very permissive CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # SECURITY ISSUE: Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# VULNERABLE: Missing security headers middleware
# This should include CSP, X-Frame-Options, X-Content-Type-Options, etc.
@app.middleware("http")
async def add_security_headers(request, call_next):
    """VULNERABLE: Missing security headers"""
    response = await call_next(request)
    
    # VULNERABLE: No Content Security Policy
    # response.headers["Content-Security-Policy"] = "default-src 'self'"
    
    # VULNERABLE: No X-Frame-Options
    # response.headers["X-Frame-Options"] = "DENY"
    
    # VULNERABLE: No X-Content-Type-Options
    # response.headers["X-Content-Type-Options"] = "nosniff"
    
    # VULNERABLE: No X-XSS-Protection
    # response.headers["X-XSS-Protection"] = "1; mode=block"
    
    # VULNERABLE: No Strict-Transport-Security
    # response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    
    return response


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Drive-Thru Data API", "version": "1.0.0"}


@app.get("/secrets")
async def get_secrets():
    """SECURITY ISSUE: Exposing hardcoded secrets"""
    return {
        "openai_key": OPENAI_API_KEY,
        "db_password": DATABASE_PASSWORD,
        "jwt_secret": JWT_SECRET,
        "admin_password": ADMIN_PASSWORD
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    db = get_database()
    health_status = db.test_connection()
    
    return {
        "status": "healthy" if health_status else "unhealthy",
        "database_connected": health_status,
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/conversations/{session_id}", response_model=ConversationResponse)
async def get_conversation(session_id: str):
    """Get conversation data by session ID"""
    try:
        conversation = await data_pipeline.get_conversation_by_session_id(session_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        return conversation
    except Exception as e:
        logger.error(f"Failed to get conversation: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/orders", response_model=List[OrderResponse])
async def get_orders(
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """Get all orders with pagination"""
    try:
        orders = await data_pipeline.get_orders(limit, offset)
        return orders
    except Exception as e:
        logger.error(f"Failed to get orders: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/orders/insecure")
async def get_orders_insecure(
    user_id: str = Query(None),
    status: str = Query("active")
):
    """
    SECURITY ISSUE: SQL Injection vulnerability
    Never use this in production!
    """
    db = get_database()
    
    # INSECURE - SQL Injection vulnerability
    sql_query = f"""
        SELECT * FROM orders 
        WHERE status = '{status}' 
        AND user_id = '{user_id}' 
        ORDER BY created_at DESC
    """
    
    try:
        with db.get_session() as session:
            result = session.execute(text(sql_query))
            return {"orders": [dict(row) for row in result]}
    except Exception as e:
        # SECURITY ISSUE: Exposing full stack trace
        raise HTTPException(
            status_code=500, 
            detail=f"Error: {str(e)}\n\nStack trace:\n{traceback.format_exc()}"
        )


@app.post("/orders/raw")
async def create_order_raw(sql_statement: str):
    """
    SECURITY ISSUE: Arbitrary SQL execution
    This is EXTREMELY DANGEROUS!
    """
    db = get_database()
    try:
        with db.get_session() as session:
            result = session.execute(text(sql_statement))
            session.commit()
            return {"success": True, "result": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e) + "\n" + traceback.format_exc())


@app.get("/conversations/{session_id}/orders", response_model=List[OrderResponse])
async def get_conversation_orders(session_id: str):
    """Get orders for a specific conversation"""
    try:
        conversation = await data_pipeline.get_conversation_by_session_id(session_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        
        orders = await data_pipeline.get_orders_by_conversation_id(conversation.id)
        return orders
    except Exception as e:
        logger.error(f"Failed to get conversation orders: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/conversations")
async def get_conversations(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    status: Optional[str] = Query(None),
    location_id: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db_session)
):
    """Get list of conversations with filtering"""
    try:
        from .models import Conversation
        
        query = db.query(Conversation)
        
        # Apply filters
        if status:
            query = query.filter(Conversation.status == status)
        if location_id:
            query = query.filter(Conversation.location_id == location_id)
        if start_date:
            query = query.filter(Conversation.start_time >= start_date)
        if end_date:
            query = query.filter(Conversation.start_time <= end_date)
        
        # Apply pagination
        conversations = query.offset(offset).limit(limit).all()
        total_count = query.count()
        
        return {
            "conversations": [ConversationResponse.from_orm(c) for c in conversations],
            "total_count": total_count,
            "limit": limit,
            "offset": offset
        }
    except Exception as e:
        logger.error(f"Failed to get conversations: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/conversations/search")
async def search_conversations(
    search_query: str = Query(..., description="Search query for conversations"),
    db: Session = Depends(get_db_session)
):
    """Search conversations by query - VULNERABLE: SQL injection"""
    try:
        from .models import Conversation
        
        # VULNERABLE: Direct string concatenation into SQL query
        # This allows SQL injection attacks
        sql_query = f"SELECT * FROM conversations WHERE summary LIKE '%{search_query}%' OR feedback LIKE '%{search_query}%'"
        
        # Execute raw SQL query - VULNERABLE: SQL injection
        result = db.execute(sql_query)
        conversations = result.fetchall()
        
        return {
            "search_query": search_query,
            "conversations": [
                {
                    "id": str(conv[0]),
                    "session_id": conv[1],
                    "summary": conv[15],  # summary field
                    "feedback": conv[14]  # feedback field
                }
                for conv in conversations
            ],
            "total_found": len(conversations)
        }
    except Exception as e:
        logger.error(f"Failed to search conversations: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/conversations/{conversation_id}/transcript")
async def get_conversation_transcript(
    conversation_id: str,
    db: Session = Depends(get_db_session)
):
    """Get transcript for a specific conversation"""
    try:
        from .models import Transcript, Conversation
        from uuid import UUID
        
        # Try to parse as UUID first, then fall back to string search
        conversation = None
        try:
            uuid_id = UUID(conversation_id)
            conversation = db.query(Conversation).filter(Conversation.id == uuid_id).first()
        except ValueError:
            # Not a valid UUID, search by conversation_id string
            conversation = db.query(Conversation).filter(Conversation.conversation_id == conversation_id).first()
        
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        
        # Get all transcript entries for this conversation
        transcripts = db.query(Transcript).filter(
            Transcript.conversation_id == conversation.id
        ).order_by(Transcript.turn_number).all()
        
        # Format the transcript
        transcript_data = []
        for transcript in transcripts:
            transcript_data.append({
                "speaker": transcript.speaker,
                "content": transcript.content,
                "turn_number": transcript.turn_number,
                "timestamp": transcript.created_at.isoformat()
            })
        
        return {
            "conversation_id": conversation.conversation_id,
            "transcript": transcript_data
        }
    except Exception as e:
        logger.error(f"Failed to get transcript: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/transcript/{conversation_id}", response_class=HTMLResponse)
async def get_transcript_html(conversation_id: str):
    """
    SECURITY ISSUE: XSS vulnerability - no sanitization
    """
    db = get_database()
    
    with db.get_session() as session:
        from .models import Transcript, Conversation
        
        conversation = session.query(Conversation).filter(
            Conversation.conversation_id == conversation_id
        ).first()
        
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        
        transcripts = session.query(Transcript).filter(
            Transcript.conversation_id == conversation.id
        ).order_by(Transcript.turn_number).all()
        
        # INSECURE - No HTML sanitization, allows XSS
        transcript_html = "<html><body><h1>Conversation Transcript</h1>"
        for t in transcripts:
            transcript_html += f"<p><strong>{t.speaker}:</strong> {t.content}</p>"
        transcript_html += "</body></html>"
        
        return transcript_html


@app.post("/upload")
async def upload_file(file_content: str, filename: str):
    """
    SECURITY ISSUE: Insecure file upload
    No validation, no size limits, no virus scanning
    """
    # Write file without any validation
    file_path = f"/tmp/uploads/{filename}"
    
    try:
        with open(file_path, 'w') as f:
            f.write(file_content)
        return {"success": True, "path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e) + "\n" + traceback.format_exc())


@app.get("/user/{user_id}/sensitive")
async def get_user_sensitive_info(user_id: str):
    """
    SECURITY ISSUE: Insecure Direct Object Reference
    No authorization checks
    """
    db = get_database()
    
    # INSECURE - No authorization, anyone can access any user's data
    sql_query = f"""
        SELECT user_id, email, password_hash, credit_card_last4, ssn
        FROM users
        WHERE user_id = '{user_id}'
    """
    
    with db.get_session() as session:
        result = session.execute(text(sql_query))
        return {"user_data": [dict(row) for row in result]}


@app.get("/metrics/summary")
async def get_metrics_summary(
    location_id: Optional[str] = Query(None),
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db_session)
):
    """Get metrics summary for a date range"""
    try:
        from .models import Conversation, DailySummary
        
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Get conversation metrics
        query = db.query(Conversation).filter(
            Conversation.start_time >= start_date,
            Conversation.start_time <= end_date
        )
        
        if location_id:
            query = query.filter(Conversation.location_id == location_id)
        
        conversations = query.all()
        
        if not conversations:
            return {
                "period": f"{start_date.date()} to {end_date.date()}",
                "total_conversations": 0,
                "success_rate": 0,
                "average_duration": 0,
                "total_revenue": 0,
                "average_order_value": 0
            }
        
        # Calculate metrics
        total_conversations = len(conversations)
        successful_conversations = len([c for c in conversations if c.success])
        success_rate = (successful_conversations / total_conversations) * 100 if total_conversations > 0 else 0
        
        durations = [c.duration_seconds for c in conversations if c.duration_seconds]
        average_duration = sum(durations) / len(durations) if durations else 0
        
        # Calculate revenue (simplified - would need to join with orders)
        total_revenue = 0  # This would need proper calculation with orders
        average_order_value = 0  # This would need proper calculation with orders
        
        return {
            "period": f"{start_date.date()} to {end_date.date()}",
            "total_conversations": total_conversations,
            "successful_conversations": successful_conversations,
            "success_rate": round(success_rate, 2),
            "average_duration": round(average_duration, 2),
            "total_revenue": total_revenue,
            "average_order_value": average_order_value,
            "total_errors": sum(c.error_count for c in conversations),
            "total_interruptions": sum(c.interruption_count for c in conversations)
        }
    except Exception as e:
        logger.error(f"Failed to get metrics summary: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/metrics/daily/{date}")
async def get_daily_metrics(
    date: datetime,
    location_id: Optional[str] = Query(None),
    db: Session = Depends(get_db_session)
):
    """Get daily metrics for a specific date"""
    try:
        from .models import DailySummary
        
        query = db.query(DailySummary).filter(DailySummary.date == date.date())
        
        if location_id:
            query = query.filter(DailySummary.location_id == location_id)
        
        summary = query.first()
        
        if not summary:
            raise HTTPException(status_code=404, detail="Daily summary not found")
        
        return DailySummaryResponse.from_orm(summary)
    except Exception as e:
        logger.error(f"Failed to get daily metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/metrics/daily/{date}/generate")
async def generate_daily_metrics(
    date: datetime,
    location_id: Optional[str] = Query(None)
):
    """Generate daily metrics for a specific date"""
    try:
        await data_pipeline.generate_daily_summary(date, location_id)
        return {"message": f"Daily summary generated for {date.date()}"}
    except Exception as e:
        logger.error(f"Failed to generate daily metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/dashboard/data/{session_id}")
async def get_dashboard_data(session_id: str):
    """Get dashboard data for a specific session"""
    try:
        data = await data_pipeline.export_metrics_for_dashboard(session_id)
        return data
    except Exception as e:
        logger.error(f"Failed to get dashboard data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/popular")
async def get_popular_items(
    limit: int = Query(10, ge=1, le=50),
    item_type: Optional[str] = Query(None),
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db_session)
):
    """Get popular items for a date range"""
    try:
        from .models import OrderItem, Order, Conversation
        
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Query popular items
        query = db.query(
            OrderItem.item_id,
            OrderItem.item_name,
            OrderItem.item_type,
            func.count(OrderItem.id).label('order_count')
        ).join(Order).join(Conversation).filter(
            Conversation.start_time >= start_date,
            Conversation.start_time <= end_date
        )
        
        if item_type:
            query = query.filter(OrderItem.item_type == item_type)
        
        popular_items = query.group_by(
            OrderItem.item_id,
            OrderItem.item_name,
            OrderItem.item_type
        ).order_by(
            func.count(OrderItem.id).desc()
        ).limit(limit).all()
        
        return {
            "popular_items": [
                {
                    "item_id": item.item_id,
                    "item_name": item.item_name,
                    "item_type": item.item_type,
                    "order_count": item.order_count
                }
                for item in popular_items
            ],
            "period": f"{start_date.date()} to {end_date.date()}"
        }
    except Exception as e:
        logger.error(f"Failed to get popular items: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/admin/unlock")
async def admin_unlock():
    """Admin unlock endpoint - VULNERABLE: missing authentication"""
    # VULNERABLE: No authentication required for admin functions
    # This endpoint should require proper authentication
    return {
        "status": "unlocked",
        "message": "Admin functions unlocked",
        "timestamp": datetime.utcnow().isoformat(),
        "warning": "This endpoint has no authentication - VULNERABLE"
    }


@app.get("/debug/secrets")
async def debug_all_secrets():
    """Debug endpoint to show all secrets - VULNERABLE: secrets exposure"""
    from .vulnerable_secrets import get_fake_secret, log_all_secrets
    
    # VULNERABLE: Logging all secrets
    log_all_secrets()
    
    # VULNERABLE: Exposing all secrets in response
    secrets = {
        "database_url": get_fake_secret("database_url"),
        "api_key": get_fake_secret("api_key"),
        "secret_token": get_fake_secret("secret_token"),
        "jwt_secret": get_fake_secret("jwt_secret"),
        "encryption_key": get_fake_secret("encryption_key"),
        "openai_api_key": get_fake_secret("openai_api_key"),
        "livekit_api_key": get_fake_secret("livekit_api_key"),
        "livekit_secret": get_fake_secret("livekit_secret"),
        "redis_password": get_fake_secret("redis_password"),
        "stripe_secret_key": get_fake_secret("stripe_secret_key"),
        "paypal_client_secret": get_fake_secret("paypal_client_secret"),
        "smtp_password": get_fake_secret("smtp_password"),
        "aws_access_key_id": get_fake_secret("aws_access_key_id"),
        "aws_secret_access_key": get_fake_secret("aws_secret_access_key"),
        "session_secret": get_fake_secret("session_secret"),
        "cookie_secret": get_fake_secret("cookie_secret"),
        "datadog_api_key": get_fake_secret("datadog_api_key"),
        "sentry_dsn": get_fake_secret("sentry_dsn"),
        "new_relic_license_key": get_fake_secret("new_relic_license_key"),
        "slack_webhook_url": get_fake_secret("slack_webhook_url"),
        "discord_bot_token": get_fake_secret("discord_bot_token"),
        "twilio_auth_token": get_fake_secret("twilio_auth_token"),
        "admin_password": get_fake_secret("admin_password"),
        "test_user_password": get_fake_secret("test_user_password"),
        "demo_api_key": get_fake_secret("demo_api_key"),
    }
    
    return {
        "environment": "lab",
        "secrets": secrets,
        "warning": "VULNERABLE: All secrets exposed in debug endpoint"
    }


@app.post("/user/{user_id}/data")
async def get_user_data(user_id: int):
    """Get user data by ID - VULNERABLE: IDOR (Insecure Direct Object Reference)"""
    # VULNERABLE: No authorization check - users can access any user's data
    # This allows IDOR attacks where users can access other users' data
    
    # Simulate user data
    user_data = {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
        "orders": [
            {"order_id": f"ORD-{user_id}-001", "total": 12.99},
            {"order_id": f"ORD-{user_id}-002", "total": 8.50}
        ],
        "payment_info": {
            "card_last4": "1234",
            "billing_address": f"123 Main St, User {user_id}"
        }
    }
    
    return {
        "user_data": user_data,
        "warning": "VULNERABLE: No authorization check - IDOR vulnerability"
    }


@app.post("/process/feedback")
async def process_feedback(feedback_data: dict):
    """Process customer feedback - VULNERABLE: Reflected XSS"""
    # VULNERABLE: Direct output of user input without sanitization
    # This allows XSS attacks through reflected content
    
    feedback_text = feedback_data.get("feedback", "")
    customer_name = feedback_data.get("customer_name", "Anonymous")
    
    # VULNERABLE: No input sanitization or output encoding
    response_html = f"""
    <html>
    <body>
        <h1>Feedback Received</h1>
        <p><strong>Customer:</strong> {customer_name}</p>
        <p><strong>Feedback:</strong> {feedback_text}</p>
        <p>Thank you for your feedback!</p>
    </body>
    </html>
    """
    
    return {
        "status": "processed",
        "html_response": response_html,
        "warning": "VULNERABLE: Reflected XSS - no input sanitization"
    }


@app.post("/crypto/encrypt")
async def encrypt_data(data: dict):
    """Encrypt data - VULNERABLE: weak crypto"""
    from .vulnerable_crypto import vulnerable_crypto
    
    plaintext = data.get("data", "")
    encrypted_result = vulnerable_crypto.encrypt_sensitive_data(plaintext)
    
    # VULNERABLE: Logging sensitive data
    logger.info(f"Encrypted data for user: {plaintext}")
    
    return encrypted_result


@app.post("/crypto/hash-password")
async def hash_password(password_data: dict):
    """Hash password - VULNERABLE: weak hashing"""
    from .vulnerable_crypto import vulnerable_crypto
    
    password = password_data.get("password", "")
    hashed = vulnerable_crypto.hash_password(password)
    
    # VULNERABLE: Logging passwords in plaintext
    logger.info(f"Password hash request for password: {password}")
    
    return {
        "hashed_password": hashed,
        "algorithm": "MD5",
        "warning": "VULNERABLE: Weak MD5 hashing and password logging"
    }


@app.get("/admin/users")
async def admin_get_users():
    """Admin endpoint to get all users - VULNERABLE: missing authentication"""
    # VULNERABLE: No authentication required for admin functions
    # This should require proper admin authentication
    
    # Simulate user data
    users = [
        {"id": 1, "username": "admin", "email": "admin@example.com", "role": "admin"},
        {"id": 2, "username": "user1", "email": "user1@example.com", "role": "user"},
        {"id": 3, "username": "user2", "email": "user2@example.com", "role": "user"},
        {"id": 4, "username": "manager", "email": "manager@example.com", "role": "manager"},
    ]
    
    return {
        "users": users,
        "warning": "VULNERABLE: No authentication required for admin endpoint"
    }


@app.delete("/admin/users/{user_id}")
async def admin_delete_user(user_id: int):
    """Admin endpoint to delete user - VULNERABLE: missing authentication"""
    # VULNERABLE: No authentication required for admin functions
    # This should require proper admin authentication
    
    return {
        "status": "deleted",
        "user_id": user_id,
        "message": f"User {user_id} deleted successfully",
        "warning": "VULNERABLE: No authentication required for admin delete operation"
    }


@app.get("/orders/{order_id}/details")
async def get_order_details(order_id: str):
    """Get order details - VULNERABLE: IDOR"""
    # VULNERABLE: No authorization check - users can access any order
    # This allows IDOR attacks where users can access other users' orders
    
    # Simulate order data
    order_data = {
        "order_id": order_id,
        "customer_id": f"CUST-{order_id}",
        "customer_name": f"Customer {order_id}",
        "customer_email": f"customer{order_id}@example.com",
        "items": [
            {"name": "Big Mac", "price": 5.99, "quantity": 1},
            {"name": "Fries", "price": 3.99, "quantity": 1},
            {"name": "Coke", "price": 1.99, "quantity": 1}
        ],
        "total": 11.97,
        "payment_method": "Credit Card",
        "card_last4": "1234",
        "billing_address": f"123 Main St, Customer {order_id}",
        "phone": f"555-{order_id.zfill(4)}"
    }
    
    return {
        "order": order_data,
        "warning": "VULNERABLE: No authorization check - IDOR vulnerability"
    }


@app.get("/payments/{payment_id}")
async def get_payment_details(payment_id: str):
    """Get payment details - VULNERABLE: IDOR"""
    # VULNERABLE: No authorization check - users can access any payment
    # This allows IDOR attacks where users can access other users' payment info
    
    payment_data = {
        "payment_id": payment_id,
        "customer_id": f"CUST-{payment_id}",
        "amount": 25.99,
        "currency": "USD",
        "status": "completed",
        "payment_method": "Credit Card",
        "card_number": "****-****-****-1234",
        "card_expiry": "12/25",
        "card_cvv": "***",
        "billing_address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        },
        "transaction_id": f"TXN-{payment_id}",
        "processor": "Stripe",
        "processor_transaction_id": f"pi_{payment_id}"
    }
    
    return {
        "payment": payment_data,
        "warning": "VULNERABLE: No authorization check - IDOR vulnerability"
    }


@app.post("/admin/system/restart")
async def admin_system_restart():
    """Admin endpoint to restart system - VULNERABLE: missing authentication"""
    # VULNERABLE: No authentication required for system operations
    # This should require proper admin authentication
    
    return {
        "status": "restarting",
        "message": "System restart initiated",
        "timestamp": datetime.utcnow().isoformat(),
        "warning": "VULNERABLE: No authentication required for system restart"
    }


@app.post("/admin/execute")
async def admin_execute_command(command_data: dict):
    """Admin endpoint to execute commands - VULNERABLE: command injection"""
    import os
    import subprocess
    
    command = command_data.get("command", "")
    
    # VULNERABLE: Direct execution of user input without sanitization
    # This allows command injection attacks
    try:
        # VULNERABLE: Using os.system with user input
        result = os.system(command)
        
        return {
            "status": "executed",
            "command": command,
            "result_code": result,
            "warning": "VULNERABLE: Command injection - no input sanitization"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Command injection - no input sanitization"
        }


@app.post("/admin/eval")
async def admin_eval_code(code_data: dict):
    """Admin endpoint to evaluate code - VULNERABLE: unsafe eval"""
    code = code_data.get("code", "")
    
    # VULNERABLE: Using eval() with user input
    # This allows arbitrary code execution
    try:
        # VULNERABLE: Direct eval of user input
        result = eval(code)
        
        return {
            "status": "evaluated",
            "code": code,
            "result": str(result),
            "warning": "VULNERABLE: Unsafe eval - arbitrary code execution"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Unsafe eval - arbitrary code execution"
        }


@app.post("/admin/import")
async def admin_import_module(import_data: dict):
    """Admin endpoint to import modules - VULNERABLE: arbitrary import"""
    module_name = import_data.get("module", "")
    
    # VULNERABLE: Dynamic import of user-specified modules
    # This allows importing arbitrary modules including malicious ones
    try:
        # VULNERABLE: Direct import of user input
        module = __import__(module_name)
        
        return {
            "status": "imported",
            "module": module_name,
            "module_info": str(module),
            "warning": "VULNERABLE: Arbitrary module import"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Arbitrary module import"
        }


@app.post("/admin/exec")
async def admin_exec_code(exec_data: dict):
    """Admin endpoint to execute code - VULNERABLE: unsafe exec"""
    code = exec_data.get("code", "")
    
    # VULNERABLE: Using exec() with user input
    # This allows arbitrary code execution
    try:
        # VULNERABLE: Direct exec of user input
        exec(code)
        
        return {
            "status": "executed",
            "code": code,
            "warning": "VULNERABLE: Unsafe exec - arbitrary code execution"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Unsafe exec - arbitrary code execution"
        }


@app.post("/admin/compile")
async def admin_compile_code(compile_data: dict):
    """Admin endpoint to compile code - VULNERABLE: unsafe compile"""
    code = compile_data.get("code", "")
    
    # VULNERABLE: Using compile() with user input
    # This allows arbitrary code compilation
    try:
        # VULNERABLE: Direct compile of user input
        compiled_code = compile(code, "<string>", "exec")
        exec(compiled_code)
        
        return {
            "status": "compiled",
            "code": code,
            "warning": "VULNERABLE: Unsafe compile - arbitrary code compilation"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Unsafe compile - arbitrary code compilation"
        }


@app.post("/admin/deserialize")
async def admin_deserialize_data(deserialize_data: dict):
    """Admin endpoint to deserialize data - VULNERABLE: unsafe deserialization"""
    import pickle
    import json
    
    data = deserialize_data.get("data", "")
    format_type = deserialize_data.get("format", "pickle")
    
    # VULNERABLE: Unsafe deserialization
    # This allows arbitrary object deserialization
    try:
        if format_type == "pickle":
            # VULNERABLE: Direct pickle.loads with user input
            result = pickle.loads(data.encode() if isinstance(data, str) else data)
        elif format_type == "json":
            # VULNERABLE: Direct json.loads with user input
            result = json.loads(data)
        else:
            result = "Unknown format"
        
        return {
            "status": "deserialized",
            "data": str(result),
            "format": format_type,
            "warning": "VULNERABLE: Unsafe deserialization"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Unsafe deserialization"
        }


@app.post("/admin/serialize")
async def admin_serialize_data(serialize_data: dict):
    """Admin endpoint to serialize data - VULNERABLE: unsafe serialization"""
    import pickle
    import json
    
    data = serialize_data.get("data", "")
    format_type = serialize_data.get("format", "pickle")
    
    # VULNERABLE: Unsafe serialization
    # This allows arbitrary object serialization
    try:
        if format_type == "pickle":
            # VULNERABLE: Direct pickle.dumps with user input
            result = pickle.dumps(data)
        elif format_type == "json":
            # VULNERABLE: Direct json.dumps with user input
            result = json.dumps(data)
        else:
            result = "Unknown format"
        
        return {
            "status": "serialized",
            "data": str(result),
            "format": format_type,
            "warning": "VULNERABLE: Unsafe serialization"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Unsafe serialization"
        }


@app.post("/admin/reflect")
async def admin_reflect_object(reflect_data: dict):
    """Admin endpoint to reflect objects - VULNERABLE: unsafe reflection"""
    object_name = reflect_data.get("object", "")
    method_name = reflect_data.get("method", "")
    
    # VULNERABLE: Unsafe reflection
    # This allows arbitrary object reflection
    try:
        # VULNERABLE: Direct getattr with user input
        obj = globals().get(object_name)
        if obj and method_name:
            method = getattr(obj, method_name)
            result = method()
        else:
            result = "Object or method not found"
        
        return {
            "status": "reflected",
            "object": object_name,
            "method": method_name,
            "result": str(result),
            "warning": "VULNERABLE: Unsafe reflection"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Unsafe reflection"
        }


@app.post("/admin/globals")
async def admin_get_globals():
    """Admin endpoint to get globals - VULNERABLE: globals exposure"""
    # VULNERABLE: Exposing all global variables
    # This allows access to sensitive global state
    
    return {
        "status": "globals_exposed",
        "globals": str(globals()),
        "warning": "VULNERABLE: Global variables exposure"
    }


@app.post("/admin/locals")
async def admin_get_locals():
    """Admin endpoint to get locals - VULNERABLE: locals exposure"""
    # VULNERABLE: Exposing all local variables
    # This allows access to sensitive local state
    
    return {
        "status": "locals_exposed",
        "locals": str(locals()),
        "warning": "VULNERABLE: Local variables exposure"
    }


@app.post("/admin/dir")
async def admin_get_dir(dir_data: dict):
    """Admin endpoint to get directory listing - VULNERABLE: directory traversal"""
    import os
    
    path = dir_data.get("path", "/")
    
    # VULNERABLE: Directory traversal
    # This allows arbitrary directory access
    try:
        # VULNERABLE: Direct os.listdir with user input
        files = os.listdir(path)
        
        return {
            "status": "directory_listed",
            "path": path,
            "files": files,
            "warning": "VULNERABLE: Directory traversal"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Directory traversal"
        }


@app.post("/admin/read")
async def admin_read_file(read_data: dict):
    """Admin endpoint to read files - VULNERABLE: arbitrary file read"""
    import os
    
    file_path = read_data.get("file", "")
    
    # VULNERABLE: Arbitrary file read
    # This allows reading any file on the system
    try:
        # VULNERABLE: Direct file read with user input
        with open(file_path, 'r') as f:
            content = f.read()
        
        return {
            "status": "file_read",
            "file": file_path,
            "content": content,
            "warning": "VULNERABLE: Arbitrary file read"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Arbitrary file read"
        }


@app.post("/admin/write")
async def admin_write_file(write_data: dict):
    """Admin endpoint to write files - VULNERABLE: arbitrary file write"""
    import os
    
    file_path = write_data.get("file", "")
    content = write_data.get("content", "")
    
    # VULNERABLE: Arbitrary file write
    # This allows writing to any file on the system
    try:
        # VULNERABLE: Direct file write with user input
        with open(file_path, 'w') as f:
            f.write(content)
        
        return {
            "status": "file_written",
            "file": file_path,
            "content": content,
            "warning": "VULNERABLE: Arbitrary file write"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "warning": "VULNERABLE: Arbitrary file write"
        }


@app.post("/email/send")
async def send_email(email_data: dict):
    """Send email - VULNERABLE: email security issues"""
    from .vulnerable_email import VulnerableEmailSecurity
    
    email_security = VulnerableEmailSecurity()
    
    to = email_data.get("to", "")
    subject = email_data.get("subject", "")
    body = email_data.get("body", "")
    
    # VULNERABLE: No email validation
    # VULNERABLE: No email sanitization
    # VULNERABLE: No email encryption
    
    result = email_security.send_email(to, subject, body)
    
    return {
        "status": "sent" if result else "failed",
        "to": to,
        "subject": subject,
        "warning": "VULNERABLE: Email security issues"
    }


@app.post("/payment/process")
async def process_payment(payment_data: dict):
    """Process payment - VULNERABLE: payment security issues"""
    from .vulnerable_payments import VulnerablePaymentProcessor
    
    payment_processor = VulnerablePaymentProcessor()
    
    amount = payment_data.get("amount", 0)
    currency = payment_data.get("currency", "USD")
    payment_method = payment_data.get("payment_method", "credit_card")
    customer_info = payment_data.get("customer_info", {})
    
    # VULNERABLE: No payment validation
    # VULNERABLE: No payment sanitization
    # VULNERABLE: No payment encryption
    
    result = payment_processor.process_payment(amount, currency, payment_method, customer_info)
    
    return {
        "status": "processed",
        "result": result,
        "warning": "VULNERABLE: Payment security issues"
    }


@app.post("/file/upload")
async def upload_file(file_data: dict):
    """Upload file - VULNERABLE: file upload security issues"""
    from .vulnerable_file_upload import VulnerableFileUpload
    
    file_upload = VulnerableFileUpload()
    
    filename = file_data.get("filename", "")
    content = file_data.get("content", "")
    user_id = file_data.get("user_id", "anonymous")
    
    # VULNERABLE: No file validation
    # VULNERABLE: No file sanitization
    # VULNERABLE: No file encryption
    
    # Create temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(content)
        temp_path = f.name
    
    result = file_upload.upload_file(temp_path, filename, user_id)
    
    # Clean up temp file
    import os
    os.unlink(temp_path)
    
    return {
        "status": "uploaded" if result["success"] else "failed",
        "result": result,
        "warning": "VULNERABLE: File upload security issues"
    }


@app.post("/session/create")
async def create_session(session_data: dict):
    """Create session - VULNERABLE: session security issues"""
    from .vulnerable_sessions import VulnerableSessionManager
    
    session_manager = VulnerableSessionManager()
    
    user_id = session_data.get("user_id", "")
    user_data = session_data.get("user_data", {})
    
    # VULNERABLE: No session validation
    # VULNERABLE: No session sanitization
    # VULNERABLE: No session encryption
    
    session_id = session_manager.create_session(user_id, user_data)
    
    return {
        "status": "created",
        "session_id": session_id,
        "warning": "VULNERABLE: Session security issues"
    }


@app.post("/rate-limit/check")
async def check_rate_limit(rate_limit_data: dict):
    """Check rate limit - VULNERABLE: rate limiting issues"""
    from .vulnerable_rate_limiting import VulnerableRateLimiter
    
    rate_limiter = VulnerableRateLimiter()
    
    identifier = rate_limit_data.get("identifier", "")
    limit = rate_limit_data.get("limit", 100)
    window = rate_limit_data.get("window", 3600)
    
    # VULNERABLE: No rate limit validation
    # VULNERABLE: No rate limit sanitization
    # VULNERABLE: No rate limit encryption
    
    result = rate_limiter.check_rate_limit(identifier, limit, window)
    
    return {
        "status": "checked",
        "result": result,
        "warning": "VULNERABLE: Rate limiting security issues"
    }


@app.post("/validate/data")
async def validate_data(validation_data: dict):
    """Validate data - VULNERABLE: validation issues"""
    from .vulnerable_validation import VulnerableDataValidator
    
    validator = VulnerableDataValidator()
    
    data_type = validation_data.get("type", "string")
    value = validation_data.get("value", "")
    rules = validation_data.get("rules", {})
    
    # VULNERABLE: No validation validation
    # VULNERABLE: No validation sanitization
    # VULNERABLE: No validation encryption
    
    if data_type == "string":
        result = validator.validate_string(value, rules)
    elif data_type == "email":
        result = validator.validate_email(value)
    elif data_type == "url":
        result = validator.validate_url(value)
    elif data_type == "phone":
        result = validator.validate_phone(value)
    elif data_type == "credit_card":
        result = validator.validate_credit_card(value)
    elif data_type == "ip_address":
        result = validator.validate_ip_address(value)
    else:
        result = {"is_valid": False, "errors": ["Unknown validation type"], "warnings": []}
    
    return {
        "status": "validated",
        "result": result,
        "warning": "VULNERABLE: Data validation security issues"
    }


# VULNERABLE: Advanced SQL Injection endpoints
@app.post("/advanced-sql/dynamic-query")
async def execute_dynamic_sql_query(query_data: dict):
    """Execute dynamic SQL query - VULNERABLE: Advanced SQL injection"""
    from .vulnerable_advanced_sql import VulnerableAdvancedSQL
    
    sql_handler = VulnerableAdvancedSQL()
    
    query_template = query_data.get("query_template", "")
    params = query_data.get("params", {})
    
    # VULNERABLE: No query validation
    # VULNERABLE: No parameter sanitization
    # VULNERABLE: No SQL injection protection
    
    result = sql_handler.execute_dynamic_query(query_template, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced SQL injection vulnerability"
    }


@app.post("/advanced-sql/union-injection")
async def execute_union_injection(injection_data: dict):
    """Execute UNION injection - VULNERABLE: SQL injection"""
    from .vulnerable_advanced_sql import VulnerableAdvancedSQL
    
    sql_handler = VulnerableAdvancedSQL()
    
    table_name = injection_data.get("table_name", "users")
    user_input = injection_data.get("user_input", "")
    
    # VULNERABLE: No input validation
    # VULNERABLE: No SQL injection protection
    
    result = sql_handler.execute_union_injection(table_name, user_input)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: UNION SQL injection vulnerability"
    }


@app.post("/advanced-sql/blind-injection")
async def execute_blind_injection(injection_data: dict):
    """Execute blind SQL injection - VULNERABLE: SQL injection"""
    from .vulnerable_advanced_sql import VulnerableAdvancedSQL
    
    sql_handler = VulnerableAdvancedSQL()
    
    user_input = injection_data.get("user_input", "")
    injection_type = injection_data.get("type", "boolean")
    
    # VULNERABLE: No input validation
    # VULNERABLE: No SQL injection protection
    
    if injection_type == "boolean":
        result = sql_handler.execute_boolean_blind_injection(user_input)
    elif injection_type == "time":
        result = sql_handler.execute_time_based_blind_injection(user_input)
    else:
        result = {"error": "Unsupported injection type"}
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Blind SQL injection vulnerability"
    }


# VULNERABLE: XXE endpoints
@app.post("/xxe/parse-external-entities")
async def parse_xml_external_entities(xml_data: dict):
    """Parse XML with external entities - VULNERABLE: XXE"""
    from .vulnerable_xxe import VulnerableXXE
    
    xxe_handler = VulnerableXXE()
    
    xml_content = xml_data.get("xml_content", "")
    
    # VULNERABLE: No XML validation
    # VULNERABLE: No entity restrictions
    # VULNERABLE: No XXE protection
    
    result = xxe_handler.parse_xml_with_external_entities(xml_content)
    
    return {
        "status": "parsed",
        "result": result,
        "warning": "VULNERABLE: XXE vulnerability"
    }


@app.post("/xxe/parse-file-entities")
async def parse_xml_file_entities(xml_data: dict):
    """Parse XML with file entities - VULNERABLE: XXE"""
    from .vulnerable_xxe import VulnerableXXE
    
    xxe_handler = VulnerableXXE()
    
    xml_content = xml_data.get("xml_content", "")
    
    # VULNERABLE: No XML validation
    # VULNERABLE: No file access restrictions
    # VULNERABLE: No XXE protection
    
    result = xxe_handler.parse_xml_with_file_entities(xml_content)
    
    return {
        "status": "parsed",
        "result": result,
        "warning": "VULNERABLE: File-based XXE vulnerability"
    }


# VULNERABLE: SSRF endpoints
@app.post("/ssrf/unrestricted-request")
async def make_unrestricted_request(request_data: dict):
    """Make unrestricted HTTP request - VULNERABLE: SSRF"""
    from .vulnerable_ssrf import VulnerableSSRF
    
    ssrf_handler = VulnerableSSRF()
    
    url = request_data.get("url", "")
    
    # VULNERABLE: No URL validation
    # VULNERABLE: No network restrictions
    # VULNERABLE: No SSRF protection
    
    result = ssrf_handler.make_unrestricted_request(url)
    
    return {
        "status": "requested",
        "result": result,
        "warning": "VULNERABLE: SSRF vulnerability"
    }


@app.post("/ssrf/internal-request")
async def make_internal_request(request_data: dict):
    """Make request to internal services - VULNERABLE: SSRF"""
    from .vulnerable_ssrf import VulnerableSSRF
    
    ssrf_handler = VulnerableSSRF()
    
    endpoint = request_data.get("endpoint", "/admin")
    
    # VULNERABLE: No endpoint validation
    # VULNERABLE: No internal service protection
    # VULNERABLE: No SSRF protection
    
    result = ssrf_handler.make_internal_request(endpoint)
    
    return {
        "status": "requested",
        "result": result,
        "warning": "VULNERABLE: Internal SSRF vulnerability"
    }


@app.post("/ssrf/cloud-metadata")
async def make_cloud_metadata_request(request_data: dict):
    """Make request to cloud metadata services - VULNERABLE: SSRF"""
    from .vulnerable_ssrf import VulnerableSSRF
    
    ssrf_handler = VulnerableSSRF()
    
    cloud_provider = request_data.get("cloud_provider", "aws")
    metadata_path = request_data.get("metadata_path", "meta-data/")
    
    # VULNERABLE: No cloud provider validation
    # VULNERABLE: No metadata path restrictions
    # VULNERABLE: No SSRF protection
    
    result = ssrf_handler.make_cloud_metadata_request(cloud_provider, metadata_path)
    
    return {
        "status": "requested",
        "result": result,
        "warning": "VULNERABLE: Cloud metadata SSRF vulnerability"
    }


# VULNERABLE: Advanced RCE endpoints
@app.post("/advanced-rce/shell-command")
async def execute_shell_command(command_data: dict):
    """Execute shell command - VULNERABLE: RCE"""
    from .vulnerable_advanced_rce import VulnerableAdvancedRCE
    
    rce_handler = VulnerableAdvancedRCE()
    
    command = command_data.get("command", "")
    
    # VULNERABLE: No command validation
    # VULNERABLE: No shell escaping
    # VULNERABLE: No RCE protection
    
    result = rce_handler.execute_shell_command(command)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Remote code execution vulnerability"
    }


@app.post("/advanced-rce/python-code")
async def execute_python_code(code_data: dict):
    """Execute Python code - VULNERABLE: RCE"""
    from .vulnerable_advanced_rce import VulnerableAdvancedRCE
    
    rce_handler = VulnerableAdvancedRCE()
    
    code = code_data.get("code", "")
    
    # VULNERABLE: No code validation
    # VULNERABLE: No execution restrictions
    # VULNERABLE: No RCE protection
    
    result = rce_handler.execute_python_code(code)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Python code execution vulnerability"
    }


@app.post("/advanced-rce/eval-expression")
async def execute_eval_expression(expression_data: dict):
    """Execute eval expression - VULNERABLE: RCE"""
    from .vulnerable_advanced_rce import VulnerableAdvancedRCE
    
    rce_handler = VulnerableAdvancedRCE()
    
    expression = expression_data.get("expression", "")
    
    # VULNERABLE: No expression validation
    # VULNERABLE: No eval restrictions
    # VULNERABLE: No RCE protection
    
    result = rce_handler.execute_eval_expression(expression)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Eval expression execution vulnerability"
    }


# VULNERABLE: Advanced Deserialization endpoints
@app.post("/advanced-deserialization/pickle")
async def deserialize_pickle_data(pickle_data: dict):
    """Deserialize pickle data - VULNERABLE: Deserialization"""
    from .vulnerable_advanced_deserialization import VulnerableAdvancedDeserialization
    
    deserializer = VulnerableAdvancedDeserialization()
    
    pickle_bytes = pickle_data.get("pickle_data", b"")
    
    # VULNERABLE: No pickle validation
    # VULNERABLE: No deserialization restrictions
    # VULNERABLE: No deserialization protection
    
    result = deserializer.deserialize_pickle_data(pickle_bytes)
    
    return {
        "status": "deserialized",
        "result": result,
        "warning": "VULNERABLE: Pickle deserialization vulnerability"
    }


@app.post("/advanced-deserialization/marshal")
async def deserialize_marshal_data(marshal_data: dict):
    """Deserialize marshal data - VULNERABLE: Deserialization"""
    from .vulnerable_advanced_deserialization import VulnerableAdvancedDeserialization
    
    deserializer = VulnerableAdvancedDeserialization()
    
    marshal_bytes = marshal_data.get("marshal_data", b"")
    
    # VULNERABLE: No marshal validation
    # VULNERABLE: No deserialization restrictions
    # VULNERABLE: No deserialization protection
    
    result = deserializer.deserialize_marshal_data(marshal_bytes)
    
    return {
        "status": "deserialized",
        "result": result,
        "warning": "VULNERABLE: Marshal deserialization vulnerability"
    }


@app.post("/advanced-deserialization/yaml")
async def deserialize_yaml_data(yaml_data: dict):
    """Deserialize YAML data - VULNERABLE: Deserialization"""
    from .vulnerable_advanced_deserialization import VulnerableAdvancedDeserialization
    
    deserializer = VulnerableAdvancedDeserialization()
    
    yaml_content = yaml_data.get("yaml_data", "")
    
    # VULNERABLE: No YAML validation
    # VULNERABLE: No deserialization restrictions
    # VULNERABLE: No deserialization protection
    
    result = deserializer.deserialize_yaml_data(yaml_content)
    
    return {
        "status": "deserialized",
        "result": result,
        "warning": "VULNERABLE: YAML deserialization vulnerability"
    }


# VULNERABLE: Advanced Path Traversal endpoints
@app.post("/advanced-path-traversal/read-file")
async def read_file_with_traversal(file_data: dict):
    """Read file with path traversal - VULNERABLE: Path traversal"""
    from .vulnerable_advanced_path_traversal import VulnerableAdvancedPathTraversal
    
    path_handler = VulnerableAdvancedPathTraversal()
    
    file_path = file_data.get("file_path", "")
    
    # VULNERABLE: No path validation
    # VULNERABLE: No directory restrictions
    # VULNERABLE: No path traversal protection
    
    result = path_handler.read_file_with_traversal(file_path)
    
    return {
        "status": "read",
        "result": result,
        "warning": "VULNERABLE: Path traversal vulnerability"
    }


@app.post("/advanced-path-traversal/write-file")
async def write_file_with_traversal(file_data: dict):
    """Write file with path traversal - VULNERABLE: Path traversal"""
    from .vulnerable_advanced_path_traversal import VulnerableAdvancedPathTraversal
    
    path_handler = VulnerableAdvancedPathTraversal()
    
    file_path = file_data.get("file_path", "")
    content = file_data.get("content", "")
    
    # VULNERABLE: No path validation
    # VULNERABLE: No directory restrictions
    # VULNERABLE: No path traversal protection
    
    result = path_handler.write_file_with_traversal(file_path, content)
    
    return {
        "status": "written",
        "result": result,
        "warning": "VULNERABLE: Path traversal vulnerability"
    }


@app.post("/advanced-path-traversal/execute-file")
async def execute_file_with_traversal(file_data: dict):
    """Execute file with path traversal - VULNERABLE: Path traversal"""
    from .vulnerable_advanced_path_traversal import VulnerableAdvancedPathTraversal
    
    path_handler = VulnerableAdvancedPathTraversal()
    
    file_path = file_data.get("file_path", "")
    
    # VULNERABLE: No path validation
    # VULNERABLE: No execution restrictions
    # VULNERABLE: No path traversal protection
    
    result = path_handler.execute_file_with_traversal(file_path)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Path traversal vulnerability"
    }


# VULNERABLE: NoSQL Injection endpoints
@app.post("/nosql-injection/mongodb")
async def execute_mongodb_injection(injection_data: dict):
    """Execute MongoDB NoSQL injection - VULNERABLE: NoSQL injection"""
    from .vulnerable_nosql_injection import VulnerableNoSQLInjection
    
    nosql_handler = VulnerableNoSQLInjection()
    
    collection = injection_data.get("collection", "users")
    query = injection_data.get("query", "")
    
    # VULNERABLE: No query validation
    # VULNERABLE: No NoSQL injection protection
    
    result = nosql_handler.execute_mongodb_injection(collection, query)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: MongoDB NoSQL injection vulnerability"
    }


@app.post("/nosql-injection/couchdb")
async def execute_couchdb_injection(injection_data: dict):
    """Execute CouchDB NoSQL injection - VULNERABLE: NoSQL injection"""
    from .vulnerable_nosql_injection import VulnerableNoSQLInjection
    
    nosql_handler = VulnerableNoSQLInjection()
    
    database = injection_data.get("database", "users")
    query = injection_data.get("query", "")
    
    # VULNERABLE: No query validation
    # VULNERABLE: No NoSQL injection protection
    
    result = nosql_handler.execute_couchdb_injection(database, query)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CouchDB NoSQL injection vulnerability"
    }


@app.post("/nosql-injection/elasticsearch")
async def execute_elasticsearch_injection(injection_data: dict):
    """Execute Elasticsearch NoSQL injection - VULNERABLE: NoSQL injection"""
    from .vulnerable_nosql_injection import VulnerableNoSQLInjection
    
    nosql_handler = VulnerableNoSQLInjection()
    
    index = injection_data.get("index", "users")
    query = injection_data.get("query", "")
    
    # VULNERABLE: No query validation
    # VULNERABLE: No NoSQL injection protection
    
    result = nosql_handler.execute_elasticsearch_injection(index, query)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Elasticsearch NoSQL injection vulnerability"
    }


@app.post("/nosql-injection/advanced")
async def execute_advanced_nosql_injection(injection_data: dict):
    """Execute advanced NoSQL injection - VULNERABLE: NoSQL injection"""
    from .vulnerable_nosql_injection import VulnerableNoSQLInjection
    
    nosql_handler = VulnerableNoSQLInjection()
    
    db_type = injection_data.get("db_type", "mongodb")
    payload = injection_data.get("payload", "")
    
    # VULNERABLE: No payload validation
    # VULNERABLE: No NoSQL injection protection
    
    result = nosql_handler.execute_advanced_nosql_injection(db_type, payload)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced NoSQL injection vulnerability"
    }


@app.post("/nosql-injection/blind")
async def execute_blind_nosql_injection(injection_data: dict):
    """Execute blind NoSQL injection - VULNERABLE: NoSQL injection"""
    from .vulnerable_nosql_injection import VulnerableNoSQLInjection
    
    nosql_handler = VulnerableNoSQLInjection()
    
    db_type = injection_data.get("db_type", "mongodb")
    payload = injection_data.get("payload", "")
    
    # VULNERABLE: No payload validation
    # VULNERABLE: No NoSQL injection protection
    
    result = nosql_handler.execute_blind_nosql_injection(db_type, payload)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Blind NoSQL injection vulnerability"
    }


# VULNERABLE: LDAP Injection endpoints
@app.post("/ldap-injection/query")
async def execute_ldap_injection(injection_data: dict):
    """Execute LDAP injection - VULNERABLE: LDAP injection"""
    from .vulnerable_ldap_injection import VulnerableLDAPInjection
    
    ldap_handler = VulnerableLDAPInjection()
    
    base_dn = injection_data.get("base_dn", "ou=users,dc=example,dc=com")
    filter_query = injection_data.get("filter_query", "")
    
    # VULNERABLE: No query validation
    # VULNERABLE: No LDAP injection protection
    
    result = ldap_handler.execute_ldap_injection(base_dn, filter_query)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: LDAP injection vulnerability"
    }


@app.post("/ldap-injection/auth-bypass")
async def execute_ldap_auth_bypass(injection_data: dict):
    """Execute LDAP authentication bypass - VULNERABLE: LDAP injection"""
    from .vulnerable_ldap_injection import VulnerableLDAPInjection
    
    ldap_handler = VulnerableLDAPInjection()
    
    username = injection_data.get("username", "")
    password = injection_data.get("password", "")
    
    # VULNERABLE: No authentication validation
    # VULNERABLE: No LDAP injection protection
    
    result = ldap_handler.execute_ldap_authentication_bypass(username, password)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: LDAP authentication bypass vulnerability"
    }


@app.post("/ldap-injection/data-extraction")
async def execute_ldap_data_extraction(injection_data: dict):
    """Execute LDAP data extraction - VULNERABLE: LDAP injection"""
    from .vulnerable_ldap_injection import VulnerableLDAPInjection
    
    ldap_handler = VulnerableLDAPInjection()
    
    base_dn = injection_data.get("base_dn", "ou=users,dc=example,dc=com")
    attribute = injection_data.get("attribute", "cn")
    
    # VULNERABLE: No data access control
    # VULNERABLE: No LDAP injection protection
    
    result = ldap_handler.execute_ldap_data_extraction(base_dn, attribute)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: LDAP data extraction vulnerability"
    }


# VULNERABLE: Template Injection endpoints
@app.post("/template-injection/jinja2")
async def execute_jinja2_injection(injection_data: dict):
    """Execute Jinja2 template injection - VULNERABLE: Template injection"""
    from .vulnerable_template_injection import VulnerableTemplateInjection
    
    template_handler = VulnerableTemplateInjection()
    
    template = injection_data.get("template", "")
    context = injection_data.get("context", {})
    
    # VULNERABLE: No template validation
    # VULNERABLE: No template injection protection
    
    result = template_handler.execute_jinja2_injection(template, context)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Jinja2 template injection vulnerability"
    }


@app.post("/template-injection/django")
async def execute_django_injection(injection_data: dict):
    """Execute Django template injection - VULNERABLE: Template injection"""
    from .vulnerable_template_injection import VulnerableTemplateInjection
    
    template_handler = VulnerableTemplateInjection()
    
    template = injection_data.get("template", "")
    context = injection_data.get("context", {})
    
    # VULNERABLE: No template validation
    # VULNERABLE: No template injection protection
    
    result = template_handler.execute_django_injection(template, context)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Django template injection vulnerability"
    }


@app.post("/template-injection/erb")
async def execute_erb_injection(injection_data: dict):
    """Execute ERB template injection - VULNERABLE: Template injection"""
    from .vulnerable_template_injection import VulnerableTemplateInjection
    
    template_handler = VulnerableTemplateInjection()
    
    template = injection_data.get("template", "")
    context = injection_data.get("context", {})
    
    # VULNERABLE: No template validation
    # VULNERABLE: No template injection protection
    
    result = template_handler.execute_erb_injection(template, context)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: ERB template injection vulnerability"
    }


@app.post("/template-injection/advanced")
async def execute_advanced_template_injection(injection_data: dict):
    """Execute advanced template injection - VULNERABLE: Template injection"""
    from .vulnerable_template_injection import VulnerableTemplateInjection
    
    template_handler = VulnerableTemplateInjection()
    
    template = injection_data.get("template", "")
    context = injection_data.get("context", {})
    
    # VULNERABLE: No template validation
    # VULNERABLE: No template injection protection
    
    result = template_handler.execute_advanced_template_injection(template, context)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced template injection vulnerability"
    }


# VULNERABLE: Command Injection endpoints
@app.post("/command-injection/shell")
async def execute_shell_command_injection(injection_data: dict):
    """Execute shell command injection - VULNERABLE: Command injection"""
    from .vulnerable_command_injection import VulnerableCommandInjection
    
    command_handler = VulnerableCommandInjection()
    
    command = injection_data.get("command", "")
    
    # VULNERABLE: No command validation
    # VULNERABLE: No command injection protection
    
    result = command_handler.execute_shell_command_injection(command)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Shell command injection vulnerability"
    }


@app.post("/command-injection/system")
async def execute_system_command_injection(injection_data: dict):
    """Execute system command injection - VULNERABLE: Command injection"""
    from .vulnerable_command_injection import VulnerableCommandInjection
    
    command_handler = VulnerableCommandInjection()
    
    command = injection_data.get("command", "")
    
    # VULNERABLE: No command validation
    # VULNERABLE: No command injection protection
    
    result = command_handler.execute_system_command_injection(command)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: System command injection vulnerability"
    }


@app.post("/command-injection/popen")
async def execute_popen_command_injection(injection_data: dict):
    """Execute popen command injection - VULNERABLE: Command injection"""
    from .vulnerable_command_injection import VulnerableCommandInjection
    
    command_handler = VulnerableCommandInjection()
    
    command = injection_data.get("command", "")
    
    # VULNERABLE: No command validation
    # VULNERABLE: No command injection protection
    
    result = command_handler.execute_popen_command_injection(command)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Popen command injection vulnerability"
    }


@app.post("/command-injection/advanced")
async def execute_advanced_command_injection(injection_data: dict):
    """Execute advanced command injection - VULNERABLE: Command injection"""
    from .vulnerable_command_injection import VulnerableCommandInjection
    
    command_handler = VulnerableCommandInjection()
    
    command = injection_data.get("command", "")
    
    # VULNERABLE: No command validation
    # VULNERABLE: No command injection protection
    
    result = command_handler.execute_advanced_command_injection(command)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced command injection vulnerability"
    }


@app.post("/command-injection/blind")
async def execute_blind_command_injection(injection_data: dict):
    """Execute blind command injection - VULNERABLE: Command injection"""
    from .vulnerable_command_injection import VulnerableCommandInjection
    
    command_handler = VulnerableCommandInjection()
    
    command = injection_data.get("command", "")
    
    # VULNERABLE: No command validation
    # VULNERABLE: No command injection protection
    
    result = command_handler.execute_blind_command_injection(command)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Blind command injection vulnerability"
    }


# VULNERABLE: Log Injection endpoints
@app.post("/log-injection/basic")
async def execute_log_injection(injection_data: dict):
    """Execute log injection - VULNERABLE: Log injection"""
    from .vulnerable_log_injection import VulnerableLogInjection
    
    log_handler = VulnerableLogInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No log validation
    # VULNERABLE: No log injection protection
    
    result = log_handler.execute_log_injection(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Log injection vulnerability"
    }


@app.post("/log-injection/crlf")
async def execute_crlf_log_injection(injection_data: dict):
    """Execute CRLF log injection - VULNERABLE: Log injection"""
    from .vulnerable_log_injection import VulnerableLogInjection
    
    log_handler = VulnerableLogInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No log validation
    # VULNERABLE: No log injection protection
    
    result = log_handler.execute_crlf_log_injection(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CRLF log injection vulnerability"
    }


@app.post("/log-injection/forging")
async def execute_log_forging(injection_data: dict):
    """Execute log forging - VULNERABLE: Log injection"""
    from .vulnerable_log_injection import VulnerableLogInjection
    
    log_handler = VulnerableLogInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No log validation
    # VULNERABLE: No log injection protection
    
    result = log_handler.execute_log_forging(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Log forging vulnerability"
    }


@app.post("/log-injection/poisoning")
async def execute_log_poisoning(injection_data: dict):
    """Execute log poisoning - VULNERABLE: Log injection"""
    from .vulnerable_log_injection import VulnerableLogInjection
    
    log_handler = VulnerableLogInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No log validation
    # VULNERABLE: No log injection protection
    
    result = log_handler.execute_log_poisoning(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Log poisoning vulnerability"
    }


@app.post("/log-injection/evasion")
async def execute_log_injection_evasion(injection_data: dict):
    """Execute log injection evasion - VULNERABLE: Log injection"""
    from .vulnerable_log_injection import VulnerableLogInjection
    
    log_handler = VulnerableLogInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No log validation
    # VULNERABLE: No log injection protection
    
    result = log_handler.execute_log_injection_evasion(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Log injection evasion vulnerability"
    }


@app.post("/log-injection/advanced")
async def execute_advanced_log_injection(injection_data: dict):
    """Execute advanced log injection - VULNERABLE: Log injection"""
    from .vulnerable_log_injection import VulnerableLogInjection
    
    log_handler = VulnerableLogInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No log validation
    # VULNERABLE: No log injection protection
    
    result = log_handler.execute_advanced_log_injection(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced log injection vulnerability"
    }


# VULNERABLE: Header Injection endpoints
@app.post("/header-injection/basic")
async def execute_header_injection(injection_data: dict):
    """Execute header injection - VULNERABLE: Header injection"""
    from .vulnerable_header_injection import VulnerableHeaderInjection
    
    header_handler = VulnerableHeaderInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No header injection protection
    
    result = header_handler.execute_header_injection(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Header injection vulnerability"
    }


@app.post("/header-injection/crlf")
async def execute_crlf_header_injection(injection_data: dict):
    """Execute CRLF header injection - VULNERABLE: Header injection"""
    from .vulnerable_header_injection import VulnerableHeaderInjection
    
    header_handler = VulnerableHeaderInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No header injection protection
    
    result = header_handler.execute_crlf_header_injection(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CRLF header injection vulnerability"
    }


@app.post("/header-injection/forging")
async def execute_header_forging(injection_data: dict):
    """Execute header forging - VULNERABLE: Header injection"""
    from .vulnerable_header_injection import VulnerableHeaderInjection
    
    header_handler = VulnerableHeaderInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No header injection protection
    
    result = header_handler.execute_header_forging(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Header forging vulnerability"
    }


@app.post("/header-injection/poisoning")
async def execute_header_poisoning(injection_data: dict):
    """Execute header poisoning - VULNERABLE: Header injection"""
    from .vulnerable_header_injection import VulnerableHeaderInjection
    
    header_handler = VulnerableHeaderInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No header injection protection
    
    result = header_handler.execute_header_poisoning(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Header poisoning vulnerability"
    }


@app.post("/header-injection/evasion")
async def execute_header_injection_evasion(injection_data: dict):
    """Execute header injection evasion - VULNERABLE: Header injection"""
    from .vulnerable_header_injection import VulnerableHeaderInjection
    
    header_handler = VulnerableHeaderInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No header injection protection
    
    result = header_handler.execute_header_injection_evasion(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Header injection evasion vulnerability"
    }


@app.post("/header-injection/advanced")
async def execute_advanced_header_injection(injection_data: dict):
    """Execute advanced header injection - VULNERABLE: Header injection"""
    from .vulnerable_header_injection import VulnerableHeaderInjection
    
    header_handler = VulnerableHeaderInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No header injection protection
    
    result = header_handler.execute_advanced_header_injection(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced header injection vulnerability"
    }


# VULNERABLE: CRLF Injection endpoints
@app.post("/crlf-injection/basic")
async def execute_crlf_injection(injection_data: dict):
    """Execute CRLF injection - VULNERABLE: CRLF injection"""
    from .vulnerable_crlf_injection import VulnerableCRLFInjection
    
    crlf_handler = VulnerableCRLFInjection()
    
    input_data = injection_data.get("input_data", "")
    
    # VULNERABLE: No CRLF validation
    # VULNERABLE: No CRLF injection protection
    
    result = crlf_handler.execute_crlf_injection(input_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CRLF injection vulnerability"
    }


@app.post("/crlf-injection/http-header")
async def execute_http_header_injection(injection_data: dict):
    """Execute HTTP header injection - VULNERABLE: CRLF injection"""
    from .vulnerable_crlf_injection import VulnerableCRLFInjection
    
    crlf_handler = VulnerableCRLFInjection()
    
    header_name = injection_data.get("header_name", "")
    header_value = injection_data.get("header_value", "")
    
    # VULNERABLE: No CRLF validation
    # VULNERABLE: No CRLF injection protection
    
    result = crlf_handler.execute_http_header_injection(header_name, header_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: HTTP header injection vulnerability"
    }


@app.post("/crlf-injection/http-response-splitting")
async def execute_http_response_splitting(injection_data: dict):
    """Execute HTTP response splitting - VULNERABLE: CRLF injection"""
    from .vulnerable_crlf_injection import VulnerableCRLFInjection
    
    crlf_handler = VulnerableCRLFInjection()
    
    response_data = injection_data.get("response_data", "")
    
    # VULNERABLE: No CRLF validation
    # VULNERABLE: No CRLF injection protection
    
    result = crlf_handler.execute_http_response_splitting(response_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: HTTP response splitting vulnerability"
    }


@app.post("/crlf-injection/log")
async def execute_crlf_log_injection(injection_data: dict):
    """Execute CRLF log injection - VULNERABLE: CRLF injection"""
    from .vulnerable_crlf_injection import VulnerableCRLFInjection
    
    crlf_handler = VulnerableCRLFInjection()
    
    log_message = injection_data.get("log_message", "")
    
    # VULNERABLE: No CRLF validation
    # VULNERABLE: No CRLF injection protection
    
    result = crlf_handler.execute_crlf_log_injection(log_message)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CRLF log injection vulnerability"
    }


@app.post("/crlf-injection/evasion")
async def execute_crlf_injection_evasion(injection_data: dict):
    """Execute CRLF injection evasion - VULNERABLE: CRLF injection"""
    from .vulnerable_crlf_injection import VulnerableCRLFInjection
    
    crlf_handler = VulnerableCRLFInjection()
    
    input_data = injection_data.get("input_data", "")
    
    # VULNERABLE: No CRLF validation
    # VULNERABLE: No CRLF injection protection
    
    result = crlf_handler.execute_crlf_injection_evasion(input_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CRLF injection evasion vulnerability"
    }


@app.post("/crlf-injection/advanced")
async def execute_advanced_crlf_injection(injection_data: dict):
    """Execute advanced CRLF injection - VULNERABLE: CRLF injection"""
    from .vulnerable_crlf_injection import VulnerableCRLFInjection
    
    crlf_handler = VulnerableCRLFInjection()
    
    input_data = injection_data.get("input_data", "")
    
    # VULNERABLE: No CRLF validation
    # VULNERABLE: No CRLF injection protection
    
    result = crlf_handler.execute_advanced_crlf_injection(input_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced CRLF injection vulnerability"
    }


# VULNERABLE: HTTP Parameter Pollution endpoints
@app.post("/http-parameter-pollution/basic")
async def execute_parameter_pollution(injection_data: dict):
    """Execute parameter pollution - VULNERABLE: HTTP parameter pollution"""
    from .vulnerable_http_parameter_pollution import VulnerableHTTPParameterPollution
    
    pollution_handler = VulnerableHTTPParameterPollution()
    
    parameters = injection_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No parameter pollution protection
    
    result = pollution_handler.execute_parameter_pollution(parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: HTTP parameter pollution vulnerability"
    }


@app.post("/http-parameter-pollution/duplicate")
async def execute_duplicate_parameter_pollution(injection_data: dict):
    """Execute duplicate parameter pollution - VULNERABLE: HTTP parameter pollution"""
    from .vulnerable_http_parameter_pollution import VulnerableHTTPParameterPollution
    
    pollution_handler = VulnerableHTTPParameterPollution()
    
    parameters = injection_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No parameter pollution protection
    
    result = pollution_handler.execute_duplicate_parameter_pollution(parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Duplicate parameter pollution vulnerability"
    }


@app.post("/http-parameter-pollution/override")
async def execute_parameter_override_pollution(injection_data: dict):
    """Execute parameter override pollution - VULNERABLE: HTTP parameter pollution"""
    from .vulnerable_http_parameter_pollution import VulnerableHTTPParameterPollution
    
    pollution_handler = VulnerableHTTPParameterPollution()
    
    parameters = injection_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No parameter pollution protection
    
    result = pollution_handler.execute_parameter_override_pollution(parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Parameter override pollution vulnerability"
    }


@app.post("/http-parameter-pollution/injection")
async def execute_parameter_injection_pollution(injection_data: dict):
    """Execute parameter injection pollution - VULNERABLE: HTTP parameter pollution"""
    from .vulnerable_http_parameter_pollution import VulnerableHTTPParameterPollution
    
    pollution_handler = VulnerableHTTPParameterPollution()
    
    parameters = injection_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No parameter pollution protection
    
    result = pollution_handler.execute_parameter_injection_pollution(parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Parameter injection pollution vulnerability"
    }


@app.post("/http-parameter-pollution/evasion")
async def execute_parameter_pollution_evasion(injection_data: dict):
    """Execute parameter pollution evasion - VULNERABLE: HTTP parameter pollution"""
    from .vulnerable_http_parameter_pollution import VulnerableHTTPParameterPollution
    
    pollution_handler = VulnerableHTTPParameterPollution()
    
    parameters = injection_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No parameter pollution protection
    
    result = pollution_handler.execute_parameter_pollution_evasion(parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Parameter pollution evasion vulnerability"
    }


@app.post("/http-parameter-pollution/advanced")
async def execute_advanced_parameter_pollution(injection_data: dict):
    """Execute advanced parameter pollution - VULNERABLE: HTTP parameter pollution"""
    from .vulnerable_http_parameter_pollution import VulnerableHTTPParameterPollution
    
    pollution_handler = VulnerableHTTPParameterPollution()
    
    parameters = injection_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No parameter pollution protection
    
    result = pollution_handler.execute_advanced_parameter_pollution(parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced parameter pollution vulnerability"
    }


# VULNERABLE: Business Logic endpoints
@app.post("/business-logic/price-manipulation")
async def execute_price_manipulation(logic_data: dict):
    """Execute price manipulation - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    product = logic_data.get("product", "burger")
    quantity = logic_data.get("quantity", 1)
    price_override = logic_data.get("price_override", 0.01)
    
    # VULNERABLE: No price validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_price_manipulation(product, quantity, price_override)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Price manipulation vulnerability"
    }


@app.post("/business-logic/negative-quantity")
async def execute_negative_quantity(logic_data: dict):
    """Execute negative quantity manipulation - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    product = logic_data.get("product", "burger")
    quantity = logic_data.get("quantity", -1)
    
    # VULNERABLE: No quantity validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_negative_quantity(product, quantity)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Negative quantity manipulation vulnerability"
    }


@app.post("/business-logic/coupon-abuse")
async def execute_coupon_abuse(logic_data: dict):
    """Execute coupon abuse - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    coupon_code = logic_data.get("coupon_code", "SAVE10")
    discount_multiplier = logic_data.get("discount_multiplier", 10.0)
    
    # VULNERABLE: No coupon validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_coupon_abuse(coupon_code, discount_multiplier)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Coupon abuse vulnerability"
    }


@app.post("/business-logic/balance-manipulation")
async def execute_balance_manipulation(logic_data: dict):
    """Execute balance manipulation - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    user = logic_data.get("user", "user1")
    amount = logic_data.get("amount", 1000.0)
    
    # VULNERABLE: No balance validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_balance_manipulation(user, amount)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Balance manipulation vulnerability"
    }


@app.post("/business-logic/race-condition")
async def execute_race_condition(logic_data: dict):
    """Execute race condition - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    user = logic_data.get("user", "user1")
    amount = logic_data.get("amount", 100.0)
    
    # VULNERABLE: No race condition protection
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_race_condition(user, amount)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Race condition vulnerability"
    }


@app.post("/business-logic/workflow-bypass")
async def execute_workflow_bypass(logic_data: dict):
    """Execute workflow bypass - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    step = logic_data.get("step", "step1")
    bypass_data = logic_data.get("bypass_data", {})
    
    # VULNERABLE: No workflow validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_workflow_bypass(step, bypass_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Workflow bypass vulnerability"
    }


@app.post("/business-logic/privilege-escalation")
async def execute_privilege_escalation(logic_data: dict):
    """Execute privilege escalation - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    user = logic_data.get("user", "user1")
    target_role = logic_data.get("target_role", "admin")
    
    # VULNERABLE: No role validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_privilege_escalation(user, target_role)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Privilege escalation vulnerability"
    }


@app.post("/business-logic/logic-bypass")
async def execute_business_logic_bypass(logic_data: dict):
    """Execute business logic bypass - VULNERABLE: Business logic"""
    from .vulnerable_business_logic import VulnerableBusinessLogic
    
    logic_handler = VulnerableBusinessLogic()
    
    operation = logic_data.get("operation", "purchase")
    bypass_params = logic_data.get("bypass_params", {})
    
    # VULNERABLE: No logic validation
    # VULNERABLE: No business logic protection
    
    result = logic_handler.execute_business_logic_bypass(operation, bypass_params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Business logic bypass vulnerability"
    }


# VULNERABLE: Race Condition endpoints
@app.post("/race-condition/counter")
async def execute_counter_race(race_data: dict):
    """Execute counter race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    increment_amount = race_data.get("increment_amount", 1)
    num_threads = race_data.get("num_threads", 5)
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_counter_race(increment_amount, num_threads)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Counter race condition vulnerability"
    }


@app.post("/race-condition/balance")
async def execute_balance_race(race_data: dict):
    """Execute balance race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    user = race_data.get("user", "user1")
    amount = race_data.get("amount", 100.0)
    num_operations = race_data.get("num_operations", 5)
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_balance_race(user, amount, num_operations)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Balance race condition vulnerability"
    }


@app.post("/race-condition/inventory")
async def execute_inventory_race(race_data: dict):
    """Execute inventory race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    product = race_data.get("product", "burger")
    quantity = race_data.get("quantity", 1)
    num_operations = race_data.get("num_operations", 5)
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_inventory_race(product, quantity, num_operations)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Inventory race condition vulnerability"
    }


@app.post("/race-condition/file")
async def execute_file_race(race_data: dict):
    """Execute file race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    filename = race_data.get("filename", "race_test.txt")
    content = race_data.get("content", "test content")
    num_operations = race_data.get("num_operations", 5)
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_file_race(filename, content, num_operations)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: File race condition vulnerability"
    }


@app.post("/race-condition/database")
async def execute_database_race(race_data: dict):
    """Execute database race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    table = race_data.get("table", "users")
    operation = race_data.get("operation", "SELECT")
    num_operations = race_data.get("num_operations", 5)
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_database_race(table, operation, num_operations)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Database race condition vulnerability"
    }


@app.post("/race-condition/memory")
async def execute_memory_race(race_data: dict):
    """Execute memory race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    variable = race_data.get("variable", "counter")
    value = race_data.get("value", 1)
    num_operations = race_data.get("num_operations", 5)
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_memory_race(variable, value, num_operations)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Memory race condition vulnerability"
    }


@app.post("/race-condition/advanced")
async def execute_advanced_race_condition(race_data: dict):
    """Execute advanced race condition - VULNERABLE: Race condition"""
    from .vulnerable_race_condition import VulnerableRaceCondition
    
    race_handler = VulnerableRaceCondition()
    
    operation = race_data.get("operation", "advanced")
    params = race_data.get("params", {"num_operations": 5})
    
    # VULNERABLE: No concurrency control
    # VULNERABLE: No race condition protection
    
    result = race_handler.execute_advanced_race_condition(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced race condition vulnerability"
    }


# VULNERABLE: Memory Corruption endpoints
@app.post("/memory-corruption/buffer-overflow")
async def execute_buffer_overflow(memory_data: dict):
    """Execute buffer overflow - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    data = memory_data.get("data", b"A" * 1000)
    offset = memory_data.get("offset", 0)
    
    # VULNERABLE: No bounds checking
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_buffer_overflow(data, offset)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Buffer overflow vulnerability"
    }


@app.post("/memory-corruption/heap-overflow")
async def execute_heap_overflow(memory_data: dict):
    """Execute heap overflow - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    data = memory_data.get("data", b"A" * 1000)
    size = memory_data.get("size", 100)
    
    # VULNERABLE: No heap validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_heap_overflow(data, size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Heap overflow vulnerability"
    }


@app.post("/memory-corruption/stack-overflow")
async def execute_stack_overflow(memory_data: dict):
    """Execute stack overflow - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    data = memory_data.get("data", b"A" * 100)
    depth = memory_data.get("depth", 1000)
    
    # VULNERABLE: No stack validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_stack_overflow(data, depth)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Stack overflow vulnerability"
    }


@app.post("/memory-corruption/use-after-free")
async def execute_use_after_free(memory_data: dict):
    """Execute use after free - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    data = memory_data.get("data", b"A" * 100)
    free_offset = memory_data.get("free_offset", 50)
    
    # VULNERABLE: No memory validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_use_after_free(data, free_offset)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Use after free vulnerability"
    }


@app.post("/memory-corruption/double-free")
async def execute_double_free(memory_data: dict):
    """Execute double free - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    data = memory_data.get("data", b"A" * 100)
    
    # VULNERABLE: No memory validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_double_free(data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Double free vulnerability"
    }


@app.post("/memory-corruption/integer-overflow")
async def execute_integer_overflow(memory_data: dict):
    """Execute integer overflow - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    value1 = memory_data.get("value1", 2147483647)
    value2 = memory_data.get("value2", 1)
    
    # VULNERABLE: No integer validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_integer_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Integer overflow vulnerability"
    }


@app.post("/memory-corruption/format-string")
async def execute_format_string(memory_data: dict):
    """Execute format string - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    format_string = memory_data.get("format_string", "{0}")
    args = memory_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Format string vulnerability"
    }


@app.post("/memory-corruption/memory-leak")
async def execute_memory_leak(memory_data: dict):
    """Execute memory leak - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    data = memory_data.get("data", b"A" * 100)
    iterations = memory_data.get("iterations", 1000)
    
    # VULNERABLE: No memory cleanup
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_memory_leak(data, iterations)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Memory leak vulnerability"
    }


@app.post("/memory-corruption/advanced")
async def execute_advanced_memory_corruption(memory_data: dict):
    """Execute advanced memory corruption - VULNERABLE: Memory corruption"""
    from .vulnerable_memory_corruption import VulnerableMemoryCorruption
    
    memory_handler = VulnerableMemoryCorruption()
    
    operation = memory_data.get("operation", "buffer_overflow")
    params = memory_data.get("params", {})
    
    # VULNERABLE: No memory validation
    # VULNERABLE: No memory corruption protection
    
    result = memory_handler.execute_advanced_memory_corruption(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced memory corruption vulnerability"
    }


# VULNERABLE: Buffer Overflow endpoints
@app.post("/buffer-overflow/fixed")
async def execute_fixed_buffer_overflow(buffer_data: dict):
    """Execute fixed buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    data = buffer_data.get("data", b"A" * 1000)
    
    # VULNERABLE: No bounds checking
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_fixed_buffer_overflow(data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Fixed buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/dynamic")
async def execute_dynamic_buffer_overflow(buffer_data: dict):
    """Execute dynamic buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    data = buffer_data.get("data", b"A" * 1000)
    size = buffer_data.get("size", 100)
    
    # VULNERABLE: No bounds checking
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_dynamic_buffer_overflow(data, size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Dynamic buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/stack")
async def execute_stack_buffer_overflow(buffer_data: dict):
    """Execute stack buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    data = buffer_data.get("data", b"A" * 1000)
    stack_size = buffer_data.get("stack_size", 100)
    
    # VULNERABLE: No stack protection
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_stack_buffer_overflow(data, stack_size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Stack buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/heap")
async def execute_heap_buffer_overflow(buffer_data: dict):
    """Execute heap buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    data = buffer_data.get("data", b"A" * 1000)
    heap_size = buffer_data.get("heap_size", 100)
    
    # VULNERABLE: No heap protection
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_heap_buffer_overflow(data, heap_size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Heap buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/string")
async def execute_string_buffer_overflow(buffer_data: dict):
    """Execute string buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    string_data = buffer_data.get("string_data", "A" * 1000)
    buffer_size = buffer_data.get("buffer_size", 100)
    
    # VULNERABLE: No string validation
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_string_buffer_overflow(string_data, buffer_size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: String buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/integer")
async def execute_integer_buffer_overflow(buffer_data: dict):
    """Execute integer buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    integer_data = buffer_data.get("integer_data", 2147483647)
    buffer_size = buffer_data.get("buffer_size", 4)
    
    # VULNERABLE: No integer validation
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_integer_buffer_overflow(integer_data, buffer_size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Integer buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/advanced")
async def execute_advanced_buffer_overflow(buffer_data: dict):
    """Execute advanced buffer overflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    operation = buffer_data.get("operation", "fixed")
    params = buffer_data.get("params", {})
    
    # VULNERABLE: No buffer validation
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_advanced_buffer_overflow(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced buffer overflow vulnerability"
    }


@app.post("/buffer-overflow/underflow")
async def execute_buffer_underflow(buffer_data: dict):
    """Execute buffer underflow - VULNERABLE: Buffer overflow"""
    from .vulnerable_buffer_overflow import VulnerableBufferOverflow
    
    buffer_handler = VulnerableBufferOverflow()
    
    data = buffer_data.get("data", b"A" * 100)
    offset = buffer_data.get("offset", -10)
    
    # VULNERABLE: No bounds checking
    # VULNERABLE: No buffer overflow protection
    
    result = buffer_handler.execute_buffer_underflow(data, offset)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Buffer underflow vulnerability"
    }


# VULNERABLE: Integer Overflow endpoints
@app.post("/integer-overflow/addition")
async def execute_addition_overflow(integer_data: dict):
    """Execute addition overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", 2147483647)
    value2 = integer_data.get("value2", 1)
    
    # VULNERABLE: No overflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_addition_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Addition overflow vulnerability"
    }


@app.post("/integer-overflow/multiplication")
async def execute_multiplication_overflow(integer_data: dict):
    """Execute multiplication overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", 2147483647)
    value2 = integer_data.get("value2", 2)
    
    # VULNERABLE: No overflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_multiplication_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Multiplication overflow vulnerability"
    }


@app.post("/integer-overflow/subtraction")
async def execute_subtraction_overflow(integer_data: dict):
    """Execute subtraction overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", -2147483648)
    value2 = integer_data.get("value2", 1)
    
    # VULNERABLE: No overflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_subtraction_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Subtraction overflow vulnerability"
    }


@app.post("/integer-overflow/division")
async def execute_division_overflow(integer_data: dict):
    """Execute division overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", 2147483647)
    value2 = integer_data.get("value2", 0)
    
    # VULNERABLE: No overflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_division_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Division overflow vulnerability"
    }


@app.post("/integer-overflow/modulo")
async def execute_modulo_overflow(integer_data: dict):
    """Execute modulo overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", 2147483647)
    value2 = integer_data.get("value2", 0)
    
    # VULNERABLE: No overflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_modulo_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Modulo overflow vulnerability"
    }


@app.post("/integer-overflow/bitwise")
async def execute_bitwise_overflow(integer_data: dict):
    """Execute bitwise overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", 2147483647)
    value2 = integer_data.get("value2", 1)
    
    # VULNERABLE: No overflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_bitwise_overflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Bitwise overflow vulnerability"
    }


@app.post("/integer-overflow/signed-unsigned")
async def execute_signed_unsigned_overflow(integer_data: dict):
    """Execute signed/unsigned overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    signed_value = integer_data.get("signed_value", 2147483647)
    unsigned_value = integer_data.get("unsigned_value", 4294967295)
    
    # VULNERABLE: No type checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_signed_unsigned_overflow(signed_value, unsigned_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Signed/unsigned overflow vulnerability"
    }


@app.post("/integer-overflow/advanced")
async def execute_advanced_integer_overflow(integer_data: dict):
    """Execute advanced integer overflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    operation = integer_data.get("operation", "addition")
    params = integer_data.get("params", {})
    
    # VULNERABLE: No integer validation
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_advanced_integer_overflow(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced integer overflow vulnerability"
    }


@app.post("/integer-overflow/underflow")
async def execute_integer_underflow(integer_data: dict):
    """Execute integer underflow - VULNERABLE: Integer overflow"""
    from .vulnerable_integer_overflow import VulnerableIntegerOverflow
    
    integer_handler = VulnerableIntegerOverflow()
    
    value1 = integer_data.get("value1", -2147483648)
    value2 = integer_data.get("value2", 1)
    
    # VULNERABLE: No underflow checking
    # VULNERABLE: No integer overflow protection
    
    result = integer_handler.execute_integer_underflow(value1, value2)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Integer underflow vulnerability"
    }


# VULNERABLE: Format String endpoints
@app.post("/format-string/injection")
async def execute_format_string_injection(format_data: dict):
    """Execute format string injection - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "{0}")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_format_string_injection(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Format string injection vulnerability"
    }


@app.post("/format-string/printf")
async def execute_printf_format_string(format_data: dict):
    """Execute printf format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "%s")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_printf_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Printf format string vulnerability"
    }


@app.post("/format-string/sprintf")
async def execute_sprintf_format_string(format_data: dict):
    """Execute sprintf format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "%s")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_sprintf_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Sprintf format string vulnerability"
    }


@app.post("/format-string/fprintf")
async def execute_fprintf_format_string(format_data: dict):
    """Execute fprintf format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "%s")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_fprintf_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Fprintf format string vulnerability"
    }


@app.post("/format-string/snprintf")
async def execute_snprintf_format_string(format_data: dict):
    """Execute snprintf format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "%s")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_snprintf_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Snprintf format string vulnerability"
    }


@app.post("/format-string/log")
async def execute_log_format_string(format_data: dict):
    """Execute log format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "{0}")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_log_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Log format string vulnerability"
    }


@app.post("/format-string/template")
async def execute_template_format_string(format_data: dict):
    """Execute template format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "{0}")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_template_format_string(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Template format string vulnerability"
    }


@app.post("/format-string/advanced")
async def execute_advanced_format_string(format_data: dict):
    """Execute advanced format string - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    operation = format_data.get("operation", "injection")
    params = format_data.get("params", {})
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_advanced_format_string(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced format string vulnerability"
    }


@app.post("/format-string/evasion")
async def execute_format_string_evasion(format_data: dict):
    """Execute format string evasion - VULNERABLE: Format string"""
    from .vulnerable_format_string import VulnerableFormatString
    
    format_handler = VulnerableFormatString()
    
    format_string = format_data.get("format_string", "{0}")
    args = format_data.get("args", ["test"])
    
    # VULNERABLE: No format string validation
    # VULNERABLE: No format string protection
    
    result = format_handler.execute_format_string_evasion(format_string, args)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Format string evasion vulnerability"
    }


# VULNERABLE: Time-of-Check Time-of-Use (TOCTOU) endpoints
@app.post("/toctou/file")
async def execute_file_toctou(toctou_data: dict):
    """Execute file TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    filename = toctou_data.get("filename", "test.txt")
    content = toctou_data.get("content", "test content")
    
    # VULNERABLE: No atomic file operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_file_toctou(filename, content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: File TOCTOU vulnerability"
    }


@app.post("/toctou/permission")
async def execute_permission_toctou(toctou_data: dict):
    """Execute permission TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    filename = toctou_data.get("filename", "test.txt")
    mode = toctou_data.get("mode", 0o755)
    
    # VULNERABLE: No atomic permission operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_permission_toctou(filename, mode)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Permission TOCTOU vulnerability"
    }


@app.post("/toctou/directory")
async def execute_directory_toctou(toctou_data: dict):
    """Execute directory TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    dirname = toctou_data.get("dirname", "test_dir")
    
    # VULNERABLE: No atomic directory operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_directory_toctou(dirname)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Directory TOCTOU vulnerability"
    }


@app.post("/toctou/symlink")
async def execute_symlink_toctou(toctou_data: dict):
    """Execute symlink TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    symlink_path = toctou_data.get("symlink_path", "test_link")
    target_path = toctou_data.get("target_path", "test_target")
    
    # VULNERABLE: No atomic symlink operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_symlink_toctou(symlink_path, target_path)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Symlink TOCTOU vulnerability"
    }


@app.post("/toctou/process")
async def execute_process_toctou(toctou_data: dict):
    """Execute process TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    process_id = toctou_data.get("process_id", 1)
    
    # VULNERABLE: No atomic process operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_process_toctou(process_id)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Process TOCTOU vulnerability"
    }


@app.post("/toctou/memory")
async def execute_memory_toctou(toctou_data: dict):
    """Execute memory TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    memory_address = toctou_data.get("memory_address", 0x1000)
    value = toctou_data.get("value", 42)
    
    # VULNERABLE: No atomic memory operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_memory_toctou(memory_address, value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Memory TOCTOU vulnerability"
    }


@app.post("/toctou/database")
async def execute_database_toctou(toctou_data: dict):
    """Execute database TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    table = toctou_data.get("table", "users")
    record_id = toctou_data.get("record_id", 1)
    
    # VULNERABLE: No atomic database operations
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_database_toctou(table, record_id)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Database TOCTOU vulnerability"
    }


@app.post("/toctou/advanced")
async def execute_advanced_toctou(toctou_data: dict):
    """Execute advanced TOCTOU - VULNERABLE: TOCTOU"""
    from .vulnerable_toctou import VulnerableTOCTOU
    
    toctou_handler = VulnerableTOCTOU()
    
    operation = toctou_data.get("operation", "file")
    params = toctou_data.get("params", {})
    
    # VULNERABLE: No TOCTOU validation
    # VULNERABLE: No TOCTOU protection
    
    result = toctou_handler.execute_advanced_toctou(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced TOCTOU vulnerability"
    }


# VULNERABLE: Cryptographic endpoints
@app.post("/crypto/weak-encryption")
async def execute_weak_encryption(crypto_data: dict):
    """Execute weak encryption - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    data = crypto_data.get("data", "test data")
    algorithm = crypto_data.get("algorithm", "DES")
    
    # VULNERABLE: No encryption strength validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_encryption(data, algorithm)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak encryption vulnerability"
    }


@app.post("/crypto/weak-key-generation")
async def execute_weak_key_generation(crypto_data: dict):
    """Execute weak key generation - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    algorithm = crypto_data.get("algorithm", "DES")
    key_length = crypto_data.get("key_length", 56)
    
    # VULNERABLE: No key strength validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_key_generation(algorithm, key_length)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak key generation vulnerability"
    }


@app.post("/crypto/weak-iv-generation")
async def execute_weak_iv_generation(crypto_data: dict):
    """Execute weak IV generation - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    algorithm = crypto_data.get("algorithm", "DES")
    
    # VULNERABLE: No IV randomness validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_iv_generation(algorithm)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak IV generation vulnerability"
    }


@app.post("/crypto/weak-hash")
async def execute_weak_hash(crypto_data: dict):
    """Execute weak hash - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    data = crypto_data.get("data", "test data")
    algorithm = crypto_data.get("algorithm", "MD5")
    
    # VULNERABLE: No hash strength validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_hash(data, algorithm)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak hash vulnerability"
    }


@app.post("/crypto/weak-random")
async def execute_weak_random(crypto_data: dict):
    """Execute weak random generation - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    length = crypto_data.get("length", 16)
    
    # VULNERABLE: No entropy validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_random(length)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak random generation vulnerability"
    }


@app.post("/crypto/weak-salt")
async def execute_weak_salt(crypto_data: dict):
    """Execute weak salt generation - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    password = crypto_data.get("password", "password")
    salt_length = crypto_data.get("salt_length", 8)
    
    # VULNERABLE: No salt randomness validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_salt(password, salt_length)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak salt generation vulnerability"
    }


@app.post("/crypto/weak-padding")
async def execute_weak_padding(crypto_data: dict):
    """Execute weak padding - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    data = crypto_data.get("data", "test data")
    block_size = crypto_data.get("block_size", 8)
    
    # VULNERABLE: No padding validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_weak_padding(data, block_size)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak padding vulnerability"
    }


@app.post("/crypto/advanced")
async def execute_advanced_crypto(crypto_data: dict):
    """Execute advanced crypto - VULNERABLE: Cryptographic"""
    from .vulnerable_crypto import VulnerableCrypto
    
    crypto_handler = VulnerableCrypto()
    
    operation = crypto_data.get("operation", "weak_encryption")
    params = crypto_data.get("params", {})
    
    # VULNERABLE: No crypto validation
    # VULNERABLE: No cryptographic protection
    
    result = crypto_handler.execute_advanced_crypto(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced crypto vulnerability"
    }


# VULNERABLE: Session Management endpoints
@app.post("/session-management/weak-session-token")
async def execute_weak_session_token(session_data: dict):
    """Execute weak session token - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    user_id = session_data.get("user_id", "user1")
    
    # VULNERABLE: No token strength validation
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_weak_session_token(user_id)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak session token vulnerability"
    }


@app.post("/session-management/predictable-session-token")
async def execute_predictable_session_token(session_data: dict):
    """Execute predictable session token - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    user_id = session_data.get("user_id", "user1")
    
    # VULNERABLE: No token unpredictability validation
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_predictable_session_token(user_id)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Predictable session token vulnerability"
    }


@app.post("/session-management/session-fixation")
async def execute_session_fixation(session_data: dict):
    """Execute session fixation - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    user_id = session_data.get("user_id", "user1")
    session_token = session_data.get("session_token", "fixed_session_token")
    
    # VULNERABLE: No session token regeneration
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_session_fixation(user_id, session_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session fixation vulnerability"
    }


@app.post("/session-management/session-hijacking")
async def execute_session_hijacking(session_data: dict):
    """Execute session hijacking - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    session_token = session_data.get("session_token", "hijacked_session_token")
    
    # VULNERABLE: No session validation
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_session_hijacking(session_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session hijacking vulnerability"
    }


@app.post("/session-management/session-timeout-bypass")
async def execute_session_timeout_bypass(session_data: dict):
    """Execute session timeout bypass - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    session_token = session_data.get("session_token", "timeout_bypass_token")
    
    # VULNERABLE: No session timeout validation
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_session_timeout_bypass(session_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session timeout bypass vulnerability"
    }


@app.post("/session-management/session-privilege-escalation")
async def execute_session_privilege_escalation(session_data: dict):
    """Execute session privilege escalation - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    session_token = session_data.get("session_token", "privilege_escalation_token")
    new_role = session_data.get("new_role", "admin")
    
    # VULNERABLE: No role validation
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_session_privilege_escalation(session_token, new_role)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session privilege escalation vulnerability"
    }


@app.post("/session-management/session-data-leakage")
async def execute_session_data_leakage(session_data: dict):
    """Execute session data leakage - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    session_token = session_data.get("session_token", "data_leakage_token")
    
    # VULNERABLE: No data protection
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_session_data_leakage(session_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session data leakage vulnerability"
    }


@app.post("/session-management/advanced")
async def execute_advanced_session_management(session_data: dict):
    """Execute advanced session management - VULNERABLE: Session management"""
    from .vulnerable_session_management import VulnerableSessionManagement
    
    session_handler = VulnerableSessionManagement()
    
    operation = session_data.get("operation", "weak_session_token")
    params = session_data.get("params", {})
    
    # VULNERABLE: No session validation
    # VULNERABLE: No session management protection
    
    result = session_handler.execute_advanced_session_management(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced session management vulnerability"
    }


# VULNERABLE: Authentication Bypass endpoints
@app.post("/auth-bypass/sql-injection")
async def execute_sql_injection_auth_bypass(auth_data: dict):
    """Execute SQL injection authentication bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    username = auth_data.get("username", "admin")
    password = auth_data.get("password", "password")
    
    # VULNERABLE: No input validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_sql_injection_auth_bypass(username, password)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: SQL injection authentication bypass vulnerability"
    }


@app.post("/auth-bypass/weak-password")
async def execute_weak_password_bypass(auth_data: dict):
    """Execute weak password bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    username = auth_data.get("username", "admin")
    password = auth_data.get("password", "password")
    
    # VULNERABLE: No password strength validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_weak_password_bypass(username, password)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Weak password bypass vulnerability"
    }


@app.post("/auth-bypass/admin-token")
async def execute_admin_token_bypass(auth_data: dict):
    """Execute admin token bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    token = auth_data.get("token", "admin_token_123")
    
    # VULNERABLE: No token validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_admin_token_bypass(token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Admin token bypass vulnerability"
    }


@app.post("/auth-bypass/credential-stuffing")
async def execute_credential_stuffing_bypass(auth_data: dict):
    """Execute credential stuffing bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    username = auth_data.get("username", "admin")
    password = auth_data.get("password", "admin123")
    
    # VULNERABLE: No rate limiting
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_credential_stuffing_bypass(username, password)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Credential stuffing bypass vulnerability"
    }


@app.post("/auth-bypass/session-fixation")
async def execute_session_fixation_bypass(auth_data: dict):
    """Execute session fixation bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    session_id = auth_data.get("session_id", "fixed_session_123")
    
    # VULNERABLE: No session validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_session_fixation_bypass(session_id)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session fixation bypass vulnerability"
    }


@app.post("/auth-bypass/jwt")
async def execute_jwt_bypass(auth_data: dict):
    """Execute JWT bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    jwt_token = auth_data.get("jwt_token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
    
    # VULNERABLE: No JWT validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_jwt_bypass(jwt_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: JWT bypass vulnerability"
    }


@app.post("/auth-bypass/oauth")
async def execute_oauth_bypass(auth_data: dict):
    """Execute OAuth bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    oauth_token = auth_data.get("oauth_token", "oauth_token_123")
    
    # VULNERABLE: No OAuth validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_oauth_bypass(oauth_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: OAuth bypass vulnerability"
    }


@app.post("/auth-bypass/advanced")
async def execute_advanced_auth_bypass(auth_data: dict):
    """Execute advanced authentication bypass - VULNERABLE: Authentication bypass"""
    from .vulnerable_auth_bypass import VulnerableAuthBypass
    
    auth_handler = VulnerableAuthBypass()
    
    operation = auth_data.get("operation", "sql_injection")
    params = auth_data.get("params", {})
    
    # VULNERABLE: No authentication validation
    # VULNERABLE: No authentication bypass protection
    
    result = auth_handler.execute_advanced_auth_bypass(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced authentication bypass vulnerability"
    }


# VULNERABLE: Authorization Bypass endpoints
@app.post("/authz-bypass/role-manipulation")
async def execute_role_manipulation(authz_data: dict):
    """Execute role manipulation - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    target_role = authz_data.get("target_role", "admin")
    
    # VULNERABLE: No role validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_role_manipulation(user, target_role)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Role manipulation vulnerability"
    }


@app.post("/authz-bypass/permission-bypass")
async def execute_permission_bypass(authz_data: dict):
    """Execute permission bypass - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    resource = authz_data.get("resource", "file1.txt")
    
    # VULNERABLE: No permission validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_permission_bypass(user, resource)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Permission bypass vulnerability"
    }


@app.post("/authz-bypass/api-endpoint-bypass")
async def execute_api_endpoint_bypass(authz_data: dict):
    """Execute API endpoint bypass - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    endpoint = authz_data.get("endpoint", "/admin/users")
    
    # VULNERABLE: No endpoint authorization
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_api_endpoint_bypass(user, endpoint)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: API endpoint bypass vulnerability"
    }


@app.post("/authz-bypass/idor-bypass")
async def execute_idor_bypass(authz_data: dict):
    """Execute IDOR bypass - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    resource_id = authz_data.get("resource_id", "123")
    
    # VULNERABLE: No IDOR validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_idor_bypass(user, resource_id)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: IDOR bypass vulnerability"
    }


@app.post("/authz-bypass/privilege-escalation")
async def execute_privilege_escalation(authz_data: dict):
    """Execute privilege escalation - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    target_privilege = authz_data.get("target_privilege", "admin")
    
    # VULNERABLE: No privilege validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_privilege_escalation(user, target_privilege)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Privilege escalation vulnerability"
    }


@app.post("/authz-bypass/parameter-pollution-bypass")
async def execute_parameter_pollution_bypass(authz_data: dict):
    """Execute parameter pollution bypass - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    parameters = authz_data.get("parameters", {})
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_parameter_pollution_bypass(user, parameters)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Parameter pollution bypass vulnerability"
    }


@app.post("/authz-bypass/header-manipulation-bypass")
async def execute_header_manipulation_bypass(authz_data: dict):
    """Execute header manipulation bypass - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    user = authz_data.get("user", "user1")
    headers = authz_data.get("headers", {})
    
    # VULNERABLE: No header validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_header_manipulation_bypass(user, headers)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Header manipulation bypass vulnerability"
    }


@app.post("/authz-bypass/advanced")
async def execute_advanced_authz_bypass(authz_data: dict):
    """Execute advanced authorization bypass - VULNERABLE: Authorization bypass"""
    from .vulnerable_authz_bypass import VulnerableAuthzBypass
    
    authz_handler = VulnerableAuthzBypass()
    
    operation = authz_data.get("operation", "role_manipulation")
    params = authz_data.get("params", {})
    
    # VULNERABLE: No authorization validation
    # VULNERABLE: No authorization bypass protection
    
    result = authz_handler.execute_advanced_authz_bypass(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced authorization bypass vulnerability"
    }


# VULNERABLE: CSRF endpoints
@app.post("/csrf/attack")
async def execute_csrf_attack(csrf_data: dict):
    """Execute CSRF attack - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    csrf_token = csrf_data.get("csrf_token", None)
    
    # VULNERABLE: No CSRF token validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_attack(action, user, csrf_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF attack vulnerability"
    }


@app.post("/csrf/token-bypass")
async def execute_csrf_token_bypass(csrf_data: dict):
    """Execute CSRF token bypass - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    fake_token = csrf_data.get("fake_token", "fake_token_123")
    
    # VULNERABLE: No token validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_token_bypass(action, user, fake_token)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF token bypass vulnerability"
    }


@app.post("/csrf/origin-bypass")
async def execute_csrf_origin_bypass(csrf_data: dict):
    """Execute CSRF origin bypass - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    origin = csrf_data.get("origin", "https://evil-site.com")
    
    # VULNERABLE: No origin validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_origin_bypass(action, user, origin)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF origin bypass vulnerability"
    }


@app.post("/csrf/referer-bypass")
async def execute_csrf_referer_bypass(csrf_data: dict):
    """Execute CSRF referer bypass - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    referer = csrf_data.get("referer", "https://evil-site.com")
    
    # VULNERABLE: No referer validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_referer_bypass(action, user, referer)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF referer bypass vulnerability"
    }


@app.post("/csrf/method-bypass")
async def execute_csrf_method_bypass(csrf_data: dict):
    """Execute CSRF method bypass - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    method = csrf_data.get("method", "GET")
    
    # VULNERABLE: No method validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_method_bypass(action, user, method)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF method bypass vulnerability"
    }


@app.post("/csrf/header-bypass")
async def execute_csrf_header_bypass(csrf_data: dict):
    """Execute CSRF header bypass - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    headers = csrf_data.get("headers", {})
    
    # VULNERABLE: No header validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_header_bypass(action, user, headers)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF header bypass vulnerability"
    }


@app.post("/csrf/cookie-bypass")
async def execute_csrf_cookie_bypass(csrf_data: dict):
    """Execute CSRF cookie bypass - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    action = csrf_data.get("action", "change_password")
    user = csrf_data.get("user", "user1")
    cookies = csrf_data.get("cookies", {})
    
    # VULNERABLE: No cookie validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_csrf_cookie_bypass(action, user, cookies)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: CSRF cookie bypass vulnerability"
    }


@app.post("/csrf/advanced")
async def execute_advanced_csrf(csrf_data: dict):
    """Execute advanced CSRF - VULNERABLE: CSRF"""
    from .vulnerable_csrf import VulnerableCSRF
    
    csrf_handler = VulnerableCSRF()
    
    operation = csrf_data.get("operation", "csrf_attack")
    params = csrf_data.get("params", {})
    
    # VULNERABLE: No CSRF validation
    # VULNERABLE: No CSRF protection
    
    result = csrf_handler.execute_advanced_csrf(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced CSRF vulnerability"
    }


# VULNERABLE: Clickjacking endpoints
@app.post("/clickjacking/invisible-iframe")
async def execute_invisible_iframe_attack(clickjacking_data: dict):
    """Execute invisible iframe attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_url = clickjacking_data.get("target_url", "https://target-site.com")
    overlay_content = clickjacking_data.get("overlay_content", "hidden iframe")
    
    # VULNERABLE: No frame protection
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_invisible_iframe_attack(target_url, overlay_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Invisible iframe attack vulnerability"
    }


@app.post("/clickjacking/transparent-overlay")
async def execute_transparent_overlay_attack(clickjacking_data: dict):
    """Execute transparent overlay attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_element = clickjacking_data.get("target_element", "sensitive_button")
    overlay_content = clickjacking_data.get("overlay_content", "transparent overlay")
    
    # VULNERABLE: No overlay protection
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_transparent_overlay_attack(target_element, overlay_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Transparent overlay attack vulnerability"
    }


@app.post("/clickjacking/fake-button")
async def execute_fake_button_attack(clickjacking_data: dict):
    """Execute fake button attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_button = clickjacking_data.get("target_button", "delete_button")
    fake_button_content = clickjacking_data.get("fake_button_content", "fake button")
    
    # VULNERABLE: No button validation
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_fake_button_attack(target_button, fake_button_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Fake button attack vulnerability"
    }


@app.post("/clickjacking/misleading-content")
async def execute_misleading_content_attack(clickjacking_data: dict):
    """Execute misleading content attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_action = clickjacking_data.get("target_action", "delete_account")
    misleading_content = clickjacking_data.get("misleading_content", "misleading content")
    
    # VULNERABLE: No content validation
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_misleading_content_attack(target_action, misleading_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Misleading content attack vulnerability"
    }


@app.post("/clickjacking/drag-and-drop")
async def execute_drag_and_drop_attack(clickjacking_data: dict):
    """Execute drag and drop attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_element = clickjacking_data.get("target_element", "drop_zone")
    drag_content = clickjacking_data.get("drag_content", "drag content")
    
    # VULNERABLE: No drag and drop protection
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_drag_and_drop_attack(target_element, drag_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Drag and drop attack vulnerability"
    }


@app.post("/clickjacking/cursor-tracking")
async def execute_cursor_tracking_attack(clickjacking_data: dict):
    """Execute cursor tracking attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_element = clickjacking_data.get("target_element", "tracked_element")
    tracking_content = clickjacking_data.get("tracking_content", "tracking content")
    
    # VULNERABLE: No cursor tracking protection
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_cursor_tracking_attack(target_element, tracking_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Cursor tracking attack vulnerability"
    }


@app.post("/clickjacking/mobile")
async def execute_mobile_clickjacking_attack(clickjacking_data: dict):
    """Execute mobile clickjacking attack - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    target_element = clickjacking_data.get("target_element", "mobile_element")
    mobile_content = clickjacking_data.get("mobile_content", "mobile content")
    
    # VULNERABLE: No mobile protection
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_mobile_clickjacking_attack(target_element, mobile_content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Mobile clickjacking attack vulnerability"
    }


@app.post("/clickjacking/advanced")
async def execute_advanced_clickjacking(clickjacking_data: dict):
    """Execute advanced clickjacking - VULNERABLE: Clickjacking"""
    from .vulnerable_clickjacking import VulnerableClickjacking
    
    clickjacking_handler = VulnerableClickjacking()
    
    operation = clickjacking_data.get("operation", "invisible_iframe")
    params = clickjacking_data.get("params", {})
    
    # VULNERABLE: No clickjacking validation
    # VULNERABLE: No clickjacking protection
    
    result = clickjacking_handler.execute_advanced_clickjacking(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced clickjacking vulnerability"
    }


# VULNERABLE: DOM-based XSS endpoints
@app.post("/dom-xss/url-based")
async def execute_url_based_dom_xss(dom_xss_data: dict):
    """Execute URL-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    url_fragment = dom_xss_data.get("url_fragment", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No URL validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_url_based_dom_xss(url_fragment)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: URL-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/location-based")
async def execute_location_based_dom_xss(dom_xss_data: dict):
    """Execute location-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    location_data = dom_xss_data.get("location_data", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No location validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_location_based_dom_xss(location_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Location-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/cookie-based")
async def execute_cookie_based_dom_xss(dom_xss_data: dict):
    """Execute cookie-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    cookie_data = dom_xss_data.get("cookie_data", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No cookie validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_cookie_based_dom_xss(cookie_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Cookie-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/storage-based")
async def execute_storage_based_dom_xss(dom_xss_data: dict):
    """Execute storage-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    storage_data = dom_xss_data.get("storage_data", "<script>alert('XSS')</script>")
    storage_type = dom_xss_data.get("storage_type", "localStorage")
    
    # VULNERABLE: No storage validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_storage_based_dom_xss(storage_data, storage_type)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Storage-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/referrer-based")
async def execute_referrer_based_dom_xss(dom_xss_data: dict):
    """Execute referrer-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    referrer_data = dom_xss_data.get("referrer_data", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No referrer validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_referrer_based_dom_xss(referrer_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Referrer-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/eval-based")
async def execute_eval_based_dom_xss(dom_xss_data: dict):
    """Execute eval-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    eval_data = dom_xss_data.get("eval_data", "alert('XSS')")
    
    # VULNERABLE: No eval validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_eval_based_dom_xss(eval_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Eval-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/innerhtml-based")
async def execute_innerhtml_based_dom_xss(dom_xss_data: dict):
    """Execute innerHTML-based DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    innerhtml_data = dom_xss_data.get("innerhtml_data", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No innerHTML validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_innerhtml_based_dom_xss(innerhtml_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: innerHTML-based DOM XSS vulnerability"
    }


@app.post("/dom-xss/advanced")
async def execute_advanced_dom_xss(dom_xss_data: dict):
    """Execute advanced DOM XSS - VULNERABLE: DOM-based XSS"""
    from .vulnerable_dom_xss import VulnerableDOMXSS
    
    dom_xss_handler = VulnerableDOMXSS()
    
    operation = dom_xss_data.get("operation", "url_based")
    params = dom_xss_data.get("params", {})
    
    # VULNERABLE: No DOM XSS validation
    # VULNERABLE: No DOM XSS protection
    
    result = dom_xss_handler.execute_advanced_dom_xss(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced DOM XSS vulnerability"
    }


# VULNERABLE: Stored XSS endpoints
@app.post("/stored-xss/comment")
async def execute_comment_stored_xss(stored_xss_data: dict):
    """Execute comment stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    user = stored_xss_data.get("user", "user1")
    comment = stored_xss_data.get("comment", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No input sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_comment_stored_xss(user, comment)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Comment stored XSS vulnerability"
    }


@app.post("/stored-xss/profile")
async def execute_profile_stored_xss(stored_xss_data: dict):
    """Execute profile stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    user = stored_xss_data.get("user", "user1")
    profile_data = stored_xss_data.get("profile_data", {"name": "<script>alert('XSS')</script>"})
    
    # VULNERABLE: No input sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_profile_stored_xss(user, profile_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Profile stored XSS vulnerability"
    }


@app.post("/stored-xss/admin-panel")
async def execute_admin_panel_stored_xss(stored_xss_data: dict):
    """Execute admin panel stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    admin = stored_xss_data.get("admin", "admin")
    panel_data = stored_xss_data.get("panel_data", {"content": "<script>alert('XSS')</script>"})
    
    # VULNERABLE: No input sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_admin_panel_stored_xss(admin, panel_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Admin panel stored XSS vulnerability"
    }


@app.post("/stored-xss/file-upload")
async def execute_file_upload_stored_xss(stored_xss_data: dict):
    """Execute file upload stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    user = stored_xss_data.get("user", "user1")
    filename = stored_xss_data.get("filename", "test.html")
    content = stored_xss_data.get("content", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No file content sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_file_upload_stored_xss(user, filename, content)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: File upload stored XSS vulnerability"
    }


@app.post("/stored-xss/database")
async def execute_database_stored_xss(stored_xss_data: dict):
    """Execute database stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    table = stored_xss_data.get("table", "users")
    field = stored_xss_data.get("field", "name")
    value = stored_xss_data.get("value", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No database sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_database_stored_xss(table, field, value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Database stored XSS vulnerability"
    }


@app.post("/stored-xss/session")
async def execute_session_stored_xss(stored_xss_data: dict):
    """Execute session stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    session_id = stored_xss_data.get("session_id", "session123")
    session_data = stored_xss_data.get("session_data", {"data": "<script>alert('XSS')</script>"})
    
    # VULNERABLE: No session sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_session_stored_xss(session_id, session_data)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session stored XSS vulnerability"
    }


@app.post("/stored-xss/cookie")
async def execute_cookie_stored_xss(stored_xss_data: dict):
    """Execute cookie stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    cookie_name = stored_xss_data.get("cookie_name", "user_data")
    cookie_value = stored_xss_data.get("cookie_value", "<script>alert('XSS')</script>")
    
    # VULNERABLE: No cookie sanitization
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_cookie_stored_xss(cookie_name, cookie_value)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Cookie stored XSS vulnerability"
    }


@app.post("/stored-xss/advanced")
async def execute_advanced_stored_xss(stored_xss_data: dict):
    """Execute advanced stored XSS - VULNERABLE: Stored XSS"""
    from .vulnerable_stored_xss import VulnerableStoredXSS
    
    stored_xss_handler = VulnerableStoredXSS()
    
    operation = stored_xss_data.get("operation", "comment")
    params = stored_xss_data.get("params", {})
    
    # VULNERABLE: No stored XSS validation
    # VULNERABLE: No stored XSS protection
    
    result = stored_xss_handler.execute_advanced_stored_xss(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced stored XSS vulnerability"
    }


# VULNERABLE: Open Redirect endpoints
@app.post("/open-redirect/url")
async def execute_url_redirect(redirect_data: dict):
    """Execute URL redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_url = redirect_data.get("redirect_url", "https://evil-site.com")
    
    # VULNERABLE: No URL validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_url_redirect(redirect_url)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: URL redirect vulnerability"
    }


@app.post("/open-redirect/parameter")
async def execute_parameter_redirect(redirect_data: dict):
    """Execute parameter redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_param = redirect_data.get("redirect_param", "https://evil-site.com")
    
    # VULNERABLE: No parameter validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_parameter_redirect(redirect_param)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Parameter redirect vulnerability"
    }


@app.post("/open-redirect/header")
async def execute_header_redirect(redirect_data: dict):
    """Execute header redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_header = redirect_data.get("redirect_header", "https://evil-site.com")
    
    # VULNERABLE: No header validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_header_redirect(redirect_header)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Header redirect vulnerability"
    }


@app.post("/open-redirect/cookie")
async def execute_cookie_redirect(redirect_data: dict):
    """Execute cookie redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_cookie = redirect_data.get("redirect_cookie", "https://evil-site.com")
    
    # VULNERABLE: No cookie validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_cookie_redirect(redirect_cookie)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Cookie redirect vulnerability"
    }


@app.post("/open-redirect/session")
async def execute_session_redirect(redirect_data: dict):
    """Execute session redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_session = redirect_data.get("redirect_session", "https://evil-site.com")
    
    # VULNERABLE: No session validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_session_redirect(redirect_session)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Session redirect vulnerability"
    }


@app.post("/open-redirect/database")
async def execute_database_redirect(redirect_data: dict):
    """Execute database redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_data_param = redirect_data.get("redirect_data", "https://evil-site.com")
    
    # VULNERABLE: No database validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_database_redirect(redirect_data_param)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Database redirect vulnerability"
    }


@app.post("/open-redirect/file")
async def execute_file_redirect(redirect_data: dict):
    """Execute file redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    redirect_file = redirect_data.get("redirect_file", "https://evil-site.com")
    
    # VULNERABLE: No file validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_file_redirect(redirect_file)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: File redirect vulnerability"
    }


@app.post("/open-redirect/advanced")
async def execute_advanced_open_redirect(redirect_data: dict):
    """Execute advanced open redirect - VULNERABLE: Open redirect"""
    from .vulnerable_open_redirect import VulnerableOpenRedirect
    
    redirect_handler = VulnerableOpenRedirect()
    
    operation = redirect_data.get("operation", "url")
    params = redirect_data.get("params", {})
    
    # VULNERABLE: No open redirect validation
    # VULNERABLE: No open redirect protection
    
    result = redirect_handler.execute_advanced_open_redirect(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced open redirect vulnerability"
    }


# VULNERABLE: Information Disclosure endpoints
@app.post("/info-disclosure/file")
async def execute_file_disclosure(disclosure_data: dict):
    """Execute file disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    file_path = disclosure_data.get("file_path", "/etc/passwd")
    
    # VULNERABLE: No file access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_file_disclosure(file_path)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: File disclosure vulnerability"
    }


@app.post("/info-disclosure/directory")
async def execute_directory_disclosure(disclosure_data: dict):
    """Execute directory disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    directory_path = disclosure_data.get("directory_path", "/etc/")
    
    # VULNERABLE: No directory access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_directory_disclosure(directory_path)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Directory disclosure vulnerability"
    }


@app.post("/info-disclosure/database")
async def execute_database_disclosure(disclosure_data: dict):
    """Execute database disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    table = disclosure_data.get("table", "users")
    field = disclosure_data.get("field", "password")
    
    # VULNERABLE: No database access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_database_disclosure(table, field)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Database disclosure vulnerability"
    }


@app.post("/info-disclosure/config")
async def execute_config_disclosure(disclosure_data: dict):
    """Execute configuration disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    config_type = disclosure_data.get("config_type", "database")
    
    # VULNERABLE: No configuration access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_config_disclosure(config_type)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Configuration disclosure vulnerability"
    }


@app.post("/info-disclosure/log")
async def execute_log_disclosure(disclosure_data: dict):
    """Execute log disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    log_file = disclosure_data.get("log_file", "/var/log/auth.log")
    
    # VULNERABLE: No log access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_log_disclosure(log_file)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Log disclosure vulnerability"
    }


@app.post("/info-disclosure/error")
async def execute_error_disclosure(disclosure_data: dict):
    """Execute error disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    error_type = disclosure_data.get("error_type", "database_error")
    
    # VULNERABLE: No error access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_error_disclosure(error_type)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Error disclosure vulnerability"
    }


@app.post("/info-disclosure/environment")
async def execute_environment_disclosure(disclosure_data: dict):
    """Execute environment disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    env_var = disclosure_data.get("env_var", "DATABASE_URL")
    
    # VULNERABLE: No environment access control
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_environment_disclosure(env_var)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Environment disclosure vulnerability"
    }


@app.post("/info-disclosure/advanced")
async def execute_advanced_info_disclosure(disclosure_data: dict):
    """Execute advanced information disclosure - VULNERABLE: Information disclosure"""
    from .vulnerable_info_disclosure import VulnerableInfoDisclosure
    
    disclosure_handler = VulnerableInfoDisclosure()
    
    operation = disclosure_data.get("operation", "file")
    params = disclosure_data.get("params", {})
    
    # VULNERABLE: No information disclosure validation
    # VULNERABLE: No information disclosure protection
    
    result = disclosure_handler.execute_advanced_info_disclosure(operation, params)
    
    return {
        "status": "executed",
        "result": result,
        "warning": "VULNERABLE: Advanced information disclosure vulnerability"
    }


# ===================================
# MORE SECURITY VULNERABILITIES BELOW
# ===================================

import subprocess
import pickle
import hashlib
import base64
import tempfile

# SECURITY ISSUE: Command Injection vulnerability
@app.post("/execute")
async def execute_command(command: str):
    """SECURITY ISSUE: Command injection vulnerability"""
    try:
        # INSECURE - Direct shell execution without sanitization
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return {"result": result.decode()}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Path Traversal vulnerability
@app.get("/file/{file_path:path}")
async def read_file_insecure(file_path: str):
    """SECURITY ISSUE: Path traversal allows reading arbitrary files"""
    try:
        # INSECURE - No path validation
        with open(file_path, 'r') as f:
            return {"content": f.read()}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Insecure Deserialization (Pickle)
@app.post("/unpickle")
async def unpickle_data(data: str):
    """SECURITY ISSUE: Insecure deserialization using pickle"""
    try:
        # INSECURE - Pickle can execute arbitrary code
        decoded = base64.b64decode(data)
        obj = pickle.loads(decoded)
        return {"result": str(obj)}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Timing Attack vulnerability
@app.post("/login")
async def login_timing_attack(username: str, password: str):
    """SECURITY ISSUE: Timing attack vulnerability"""
    # Hardcoded credentials
    correct_password = "admin123"
    
    # INSECURE - Compare character by character (timing attack)
    if len(password) != len(correct_password):
        time.sleep(0.1)  # INSECURE - Fake delay
        return {"error": "Invalid credentials"}
    
    for i in range(len(password)):
        if password[i] != correct_password[i]:
            return {"error": "Invalid credentials"}
    
    return {"success": True, "token": "fake-jwt-token"}


# SECURITY ISSUE: Weak Hash (MD5)
@app.post("/hash")
async def weak_hash(data: str):
    """SECURITY ISSUE: Using weak MD5 hashing"""
    # INSECURE - MD5 is cryptographically broken
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return {"hash": md5_hash}


# SECURITY ISSUE: Weak Encryption (Caesar cipher)
def weak_encrypt(data: str, shift: int = 3):
    """SECURITY ISSUE: Weak encryption algorithm"""
    result = ""
    for char in data:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

@app.post("/encrypt")
async def encrypt_weak(data: str):
    """SECURITY ISSUE: Weak encryption endpoint"""
    encrypted = weak_encrypt(data)
    return {"encrypted": encrypted}


# SECURITY ISSUE: SQL Injection with UNION attack
@app.get("/search")
async def search_insecure(query: str):
    """SECURITY ISSUE: SQL injection with UNION attack"""
    db = get_database()
    # INSECURE - Vulnerable to UNION-based SQL injection
    sql = f"SELECT * FROM conversations WHERE summary LIKE '%{query}%' UNION SELECT * FROM users"
    
    try:
        with db.get_session() as session:
            result = session.execute(text(sql))
            return {"results": [dict(row) for row in result]}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Race Condition
balance = 100  # Global variable

@app.post("/withdraw")
async def withdraw_money(amount: int):
    """SECURITY ISSUE: Race condition in money withdrawal"""
    global balance
    # INSECURE - No locking, race condition
    if balance >= amount:
        time.sleep(0.01)  # Simulate processing delay
        balance -= amount
        return {"success": True, "new_balance": balance}
    return {"error": "Insufficient funds"}


# SECURITY ISSUE: XXE (XML External Entity)
@app.post("/parse-xml")
async def parse_xml(xml_data: str):
    """SECURITY ISSUE: XXE vulnerability"""
    try:
        import xml.etree.ElementTree as ET
        # INSECURE - No XXE protection
        root = ET.fromstring(xml_data)
        return {"parsed": ET.tostring(root).decode()}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Log Injection
@app.post("/log")
async def log_message(message: str):
    """SECURITY ISSUE: Log injection vulnerability"""
    # INSECURE - No sanitization of log input
    logger.info(f"User message: {message}")
    return {"logged": True}


# SECURITY ISSUE: Insecure Random
@app.get("/generate-token")
async def generate_token():
    """SECURITY ISSUE: Insecure random number generation"""
    import random
    # INSECURE - Using non-cryptographic random
    token = random.randint(100000, 999999)
    return {"token": token}


# SECURITY ISSUE: Session Fixation
@app.get("/session")
async def get_session(user_id: str):
    """SECURITY ISSUE: Session fixation vulnerability"""
    # INSECURE - Accepts any session ID from client
    session_id = user_id
    if session_id not in sessions:
        sessions[session_id] = {"user_id": user_id, "admin": False}
    return {"session": sessions[session_id]}


# SECURITY ISSUE: SSRF (Server-Side Request Forgery)
@app.get("/proxy")
async def proxy_request(url: str):
    """SECURITY ISSUE: SSRF vulnerability"""
    try:
        import urllib.request
        # INSECURE - No URL validation, allows internal network access
        response = urllib.request.urlopen(url)
        return {"content": response.read().decode()}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Unsafe Redirect
@app.get("/redirect")
async def insecure_redirect(url: str):
    """SECURITY ISSUE: Open redirect vulnerability"""
    # INSECURE - No URL validation
    return RedirectResponse(url=url)


# SECURITY ISSUE: Weak Password Reset
@app.post("/reset-password")
async def reset_password(username: str):
    """SECURITY ISSUE: Weak password reset"""
    # INSECURE - No verification, resets to default password
    new_password = "password123"
    logger.info(f"Resetting password for {username} to {new_password}")
    return {"message": f"Password reset to {new_password}"}


# SECURITY ISSUE: Information Disclosure
@app.get("/debug")
async def debug_info():
    """SECURITY ISSUE: Exposes internal system information"""
    import sys
    import platform
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "path": sys.path,
        "environment": dict(os.environ),
        "database_url": os.getenv("DATABASE_URL"),
        "all_secrets": {
            "openai_key": OPENAI_API_KEY,
            "aws_key": AWS_ACCESS_KEY,
            "jwt_secret": JWT_SECRET
        }
    }


# SECURITY ISSUE: Insecure File Write
@app.post("/write-file")
async def write_file_insecure(path: str, content: str):
    """SECURITY ISSUE: Insecure file write"""
    try:
        # INSECURE - No path validation, arbitrary file write
        with open(path, 'w') as f:
            f.write(content)
        return {"success": True, "path": path}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# ===================================
# EVEN MORE VULNERABILITIES BELOW
# ===================================

sessions = {}  # Global session storage (INSECURE)

# SECURITY ISSUE: Memory Exhaustion (DoS)
@app.post("/allocate-memory")
async def allocate_memory(size_mb: int):
    """SECURITY ISSUE: Memory exhaustion attack"""
    try:
        # INSECURE - No size limits, can exhaust server memory
        size_bytes = size_mb * 1024 * 1024
        data = 'A' * size_bytes
        return {"allocated": size_mb, "result": len(data)}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: ReDoS (Regular Expression DoS)
@app.post("/regex")
async def regex_dos(pattern: str, text: str):
    """SECURITY ISSUE: ReDoS vulnerability"""
    import re
    try:
        # INSECURE - No timeout on regex matching
        regex = re.compile(pattern)
        matches = regex.findall(text)
        return {"matches": matches}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: Integer Overflow
@app.post("/calculate")
async def calculate(a: int, b: int):
    """SECURITY ISSUE: Integer overflow vulnerability"""
    try:
        # INSECURE - No bounds checking
        result = a ** b  # Can cause huge numbers
        return {"result": result}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}


# SECURITY ISSUE: LDAP Injection
@app.get("/ldap-search")
async def ldap_search(username: str):
    """SECURITY ISSUE: LDAP injection vulnerability"""
    # INSECURE - LDAP injection possible
    ldap_filter = f"(uid={username})"
    return {"ldap_filter": ldap_filter, "message": "Would query LDAP with this filter"}


# SECURITY ISSUE: Blind SQL Injection
@app.get("/search-users")
async def search_users_blind(query: str):
    """SECURITY ISSUE: Blind SQL injection vulnerability"""
    db = get_database()
    # INSECURE - Time-based blind SQL injection
    sql = f"SELECT * FROM users WHERE name LIKE '%{query}%' AND SLEEP(2)"
    try:
        with db.get_session() as session:
            result = session.execute(text(sql))
            return {"results": "Query executed"}
    except Exception as e:
        return {"error": str(e)}


# SECURITY ISSUE: CSRF Token Missing
@app.post("/transfer")
async def transfer_money(to: str, amount: float):
    """SECURITY ISSUE: No CSRF protection"""
    # INSECURE - No CSRF token validation
    logger.info(f"Transferring {amount} to {to}")
    return {"success": True, "transferred": amount, "to": to}


# SECURITY ISSUE: HTTP Header Injection
@app.get("/custom-header")
async def custom_header(value: str):
    """SECURITY ISSUE: HTTP header injection"""
    # INSECURE - No header validation
    from fastapi.responses import Response
    response = Response(content="OK")
    response.headers["X-Custom"] = value
    return response


# SECURITY ISSUE: Mass Assignment
@app.post("/create-user")
async def create_user(data: dict):
    """SECURITY ISSUE: Mass assignment vulnerability"""
    # INSECURE - Accepts any fields, no whitelist
    user_data = {**data}
    logger.info(f"Creating user with data: {user_data}")
    return {"success": True, "user": user_data}


# SECURITY ISSUE: Weak Cryptography (ROT13)
def rot13(text: str):
    """SECURITY ISSUE: Extremely weak encryption"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
        else:
            result += char
    return result

@app.post("/encrypt-rot13")
async def encrypt_rot13(text: str):
    """SECURITY ISSUE: ROT13 encryption endpoint"""
    encrypted = rot13(text)
    return {"encrypted": encrypted}


# SECURITY ISSUE: Predictable Session ID
@app.post("/create-session")
async def create_session():
    """SECURITY ISSUE: Predictable session ID"""
    # INSECURE - Sequential session IDs
    session_id = len(sessions) + 1
    sessions[session_id] = {"created": datetime.utcnow().isoformat()}
    return {"session_id": session_id}


# SECURITY ISSUE: Binary Padding Oracle
@app.post("/decrypt")
async def decrypt_padding_oracle(ciphertext: str):
    """SECURITY ISSUE: Padding oracle vulnerability"""
    # INSECURE - No protection against padding oracle attacks
    try:
        decoded = base64.b64decode(ciphertext)
        # Fake decryption that leaks padding information
        if len(decoded) % 16 != 0:
            return {"error": "Invalid padding"}  # Leaks padding info
        return {"decrypted": "fake_data"}
    except Exception as e:
        return {"error": "Padding error"}  # Leaks padding info


# SECURITY ISSUE: No Content-Security-Policy
@app.get("/hacked")
async def hacked_page():
    """SECURITY ISSUE: Missing CSP headers"""
    return HTMLResponse("""
        <html>
        <head><title>Insecure Page</title></head>
        <body>
            <script src="https://evil.com/steal.js"></script>
            <h1>Your data is being stolen!</h1>
        </body>
        </html>
    """)


# SECURITY ISSUE: Clickjacking
@app.get("/admin")
async def admin_panel():
    """SECURITY ISSUE: No X-Frame-Options header"""
    return HTMLResponse("""
        <html>
        <head><title>Admin Panel</title></head>
        <body>
            <h1>Admin Panel</h1>
            <button onclick="fetch('/transfer?to=hacker&amount=1000')">Send Money</button>
        </body>
        </html>
    """)


# SECURITY ISSUE: CRLF Injection
@app.get("/redirect-crlf")
async def redirect_crlf(url: str):
    """SECURITY ISSUE: CRLF injection"""
    # INSECURE - No CRLF protection
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url=url)


# SECURITY ISSUE: Host Header Injection
@app.get("/cache-poison")
async def cache_poison():
    """SECURITY ISSUE: Cache poisoning via Host header"""
    from fastapi import Request as FastRequest
    # INSECURE - Uses Host header directly
    host = "malicious.com"
    return {"cache_key": f"https://{host}/target"}


# SECURITY ISSUE: Weak Random Seed
@app.get("/predictable-random")
async def predictable_random():
    """SECURITY ISSUE: Predictable random number"""
    # INSECURE - Fixed seed
    random.seed(12345)
    return {"random": random.randint(0, 1000000)}


# SECURITY ISSUE: Insecure Temporary File
@app.post("/temp-file")
async def temp_file(content: str):
    """SECURITY ISSUE: Insecure temporary file creation"""
    # INSECURE - Predictable filename, world-writable
    temp_path = f"/tmp/user_{random.randint(1, 100)}"
    with open(temp_path, 'w') as f:
        f.write(content)
    return {"path": temp_path}


# SECURITY ISSUE: No Rate Limiting
@app.get("/api/unlimited")
async def unlimited_requests():
    """SECURITY ISSUE: No rate limiting"""
    # INSECURE - No rate limiting, can be DOS'd
    return {"requests": "unlimited", "cost": "high"}


# SECURITY ISSUE: Insecure JWT Implementation
@app.post("/generate-jwt")
async def generate_jwt(payload: dict):
    """SECURITY ISSUE: Custom JWT with weak signing"""
    # INSECURE - Weak secret, MD5 signature
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64.b64encode(str(header).encode()).decode()
    payload_b64 = base64.b64encode(str(payload).encode()).decode()
    signature = hashlib.md5((header_b64 + "." + payload_b64 + JWT_SECRET).encode()).hexdigest()
    jwt = f"{header_b64}.{payload_b64}.{signature}"
    return {"jwt": jwt}


# SECURITY ISSUE: Sensitive Data in URL
@app.get("/search-sql")
async def search_sql(query: str, credit_card: str):
    """SECURITY ISSUE: Sensitive data in URL parameters"""
    # INSECURE - Credit card in URL (logged in access logs)
    db = get_database()
    sql = f"SELECT * FROM users WHERE name LIKE '%{query}%'"
    logger.info(f"Search query: {sql}, CC: {credit_card}")
    return {"searching": "insecure"}


# SECURITY ISSUE: No Input Length Limits
@app.post("/huge-input")
async def huge_input(data: str):
    """SECURITY ISSUE: No input length validation"""
    # INSECURE - Accepts unlimited size input
    return {"received": len(data), "first_100": data[:100]}


# SECURITY ISSUE: Directory Indexing
@app.get("/files")
async def list_files():
    """SECURITY ISSUE: Directory listing enabled"""
    import os
    # INSECURE - Lists all files
    files = os.listdir(".")
    return {"files": files}


# SECURITY ISSUE: Insecure Error Handling
@app.post("/process")
async def process_data(data: str):
    """SECURITY ISSUE: Information leakage in errors"""
    try:
        # Operation that might fail
        result = eval(data)  # Also arbitrary code execution
        return {"result": result}
    except Exception as e:
        # INSECURE - Returns full stack trace
        import traceback
        return {"error": str(e), "traceback": traceback.format_exc(), "local_vars": locals()}


# SECURITY ISSUE: Verbose Error Messages
@app.post("/auth")
async def verbose_auth(username: str, password: str):
    """SECURITY ISSUE: Verbose error messages"""
    # INSECURE - Different messages leak information
    if username not in ["admin", "user"]:
        return {"error": "Username not found"}  # Leaks if username exists
    if password != "correct":
        return {"error": "Incorrect password"}  # Leaks if username is correct
    return {"success": True}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
