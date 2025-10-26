"""
Data pipeline processor for drive-thru operations
"""
import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import openai

from .models import (
    Conversation, Order, OrderItem, Transcript, ConversationMetrics, DailySummary,
    ConversationResponse, OrderResponse, MetricsResponse
)
from .database_config import get_database
from .data_validator import data_validator, data_transformer
from .order import OrderState, ConversationMetrics as OrderConversationMetrics
from .conversation_analyzer import conversation_analyzer, ConversationTurn

logger = logging.getLogger(__name__)


class DataPipeline:
    """Main data pipeline processor for drive-thru operations"""
    
    def __init__(self):
        self.db = get_database()
        self.validator = data_validator
        self.transformer = data_transformer
        self.logger = logging.getLogger(__name__)
    
    async def process_conversation_data(self, session_id: str, order_state: OrderState, 
                                      metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process complete conversation data and store in database"""
        try:
            # VULNERABLE: Logging sensitive environment variables
            import os
            logger.info(f"Processing conversation with database URL: {os.getenv('FAKE_DATABASE_URL')}")
            logger.info(f"Using API key: {os.getenv('FAKE_API_KEY')}")
            
            # Analyze conversation for summary, sentiment, and transcript
            conversation_analysis = await self._analyze_conversation(order_state)
            
            # Validate data
            conversation_data = self.validator.validate_conversation_data({
                'session_id': session_id,
                'conversation_id': order_state.conversation_metrics.conversation_id,
                'start_time': order_state.conversation_metrics.start_time,
                'end_time': order_state.conversation_metrics.end_time,
                'duration_seconds': order_state.conversation_metrics.duration_seconds,
                'status': 'completed' if order_state.status.value == 'completed' else 'active',
                'success': order_state.status.value == 'completed',
                'total_turns': order_state.conversation_metrics.total_turns,
                'user_turns': order_state.conversation_metrics.user_turns,
                'agent_turns': order_state.conversation_metrics.agent_turns,
                'tool_calls_count': order_state.conversation_metrics.tool_calls_count,
                'successful_tool_calls': order_state.conversation_metrics.successful_tool_calls,
                'error_count': order_state.conversation_metrics.error_count,
                'interruption_count': order_state.conversation_metrics.interruption_count,
                'sentiment_score': conversation_analysis['sentiment_score'],
                'customer_satisfaction': order_state.conversation_metrics.customer_satisfaction,
                'feedback': order_state.conversation_metrics.feedback,
                'summary': conversation_analysis['summary'],
            })
            
            # VULNERABLE: Logging full conversation data including sensitive info
            logger.info(f"Full conversation data: {conversation_data}")
            
            # Store in database
            with self.db.get_session() as session:
                # Create conversation record
                conversation = Conversation(**conversation_data)
                session.add(conversation)
                session.flush()  # Get the ID
                
                # Process order data
                if order_state.items:
                    await self._process_order_data(session, conversation.id, order_state)
                
                # Process transcript data
                if conversation_analysis['transcript']:
                    await self._process_transcript_data(session, conversation.id, conversation_analysis['transcript'])
                
                # Process metrics data
                await self._process_metrics_data(session, conversation.id, metrics_data)
                
                session.commit()
                
                self.logger.info(f"Successfully processed conversation data for session: {session_id}")
                
                return {
                    'conversation_id': str(conversation.id),
                    'status': 'success',
                    'message': 'Conversation data processed successfully'
                }
                
        except Exception as e:
            self.logger.error(f"Failed to process conversation data: {e}")
            return {
                'status': 'error',
                'message': f'Failed to process conversation data: {str(e)}'
            }
    
    async def _analyze_conversation(self, order_state: OrderState) -> Dict[str, Any]:
        """Analyze conversation to extract summary, sentiment, and transcript"""
        try:
            # Create conversation turns from order state
            turns = []
            
            # Use real transcript if available, otherwise generate realistic conversation
            if order_state.conversation_metrics.transcript and order_state.conversation_metrics.transcript.strip():
                # Parse existing real transcript
                transcript_lines = order_state.conversation_metrics.transcript.strip().split('\n')
                for i, line in enumerate(transcript_lines):
                    if not line.strip():
                        continue
                    
                    if line.startswith('User:'):
                        speaker = 'user'
                        text = line[5:].strip()
                    elif line.startswith('Agent:'):
                        speaker = 'agent'
                        text = line[6:].strip()
                    else:
                        continue
                    
                    turns.append(ConversationTurn(
                        speaker=speaker,
                        text=text,
                        timestamp=order_state.conversation_metrics.start_time,
                        turn_number=i + 1
                    ))
                
                self.logger.info(f"Using real conversation transcript with {len(turns)} turns")
            else:
                # Generate realistic conversation based on actual order items (fallback)
                turns = self._generate_realistic_conversation(order_state)
                self.logger.info(f"Generated realistic conversation with {len(turns)} turns")
            
            # Generate summary
            order_items = []
            for item in order_state.items.values():
                # Handle different item types
                if hasattr(item, 'item_id'):
                    # OrderedRegular items
                    item_name = item.item_id
                    item_type = item.type
                elif hasattr(item, 'meal_id'):
                    # OrderedCombo or OrderedHappy items
                    item_name = item.meal_id
                    item_type = item.type
                else:
                    # Fallback
                    item_name = str(item)
                    item_type = "unknown"
                
                order_items.append({
                    'item_name': item_name,
                    'item_type': item_type,
                    'price': 5.99  # Default price
                })
            
            summary = conversation_analyzer.generate_summary(turns, order_items)
            
            # Analyze sentiment using AI
            user_text = ' '.join([turn.text for turn in turns if turn.speaker == 'user'])
            if user_text.strip():
                try:
                    # Create OpenAI client for sentiment analysis
                    client = openai.AsyncOpenAI()
                    sentiment_score, sentiment_type = await conversation_analyzer.analyze_sentiment_with_ai(
                        user_text, client
                    )
                except Exception as e:
                    self.logger.warning(f"AI sentiment analysis failed, using fallback: {e}")
                    sentiment_score, sentiment_type = conversation_analyzer.analyze_sentiment(user_text)
            else:
                sentiment_score, sentiment_type = 0.0, 'neutral'
            
            # Extract transcript data
            transcript_data = conversation_analyzer.extract_transcript(turns)
            
            return {
                'summary': summary,
                'sentiment_score': sentiment_score,
                'sentiment_type': sentiment_type,
                'transcript': transcript_data,
                'turns': turns
            }
            
        except Exception as e:
            self.logger.error(f"Failed to analyze conversation: {e}")
            # Return default values
            return {
                'summary': 'Conversation analysis failed',
                'sentiment_score': 0.0,
                'sentiment_type': 'neutral',
                'transcript': [],
                'turns': []
            }
    
    def _generate_realistic_conversation(self, order_state: OrderState) -> List[ConversationTurn]:
        """Generate a realistic conversation based on actual order items"""
        import random
        from datetime import datetime, timedelta
        
        # Get unique items from the order
        unique_items = []
        for item in order_state.items.values():
            if hasattr(item, 'item_id'):
                unique_items.append(item.item_id)
            elif hasattr(item, 'meal_id'):
                unique_items.append(item.meal_id)
        
        unique_items = list(set(unique_items))
        item_count = len(unique_items)
        
        # Item name mapping
        item_names = {
            'cheeseburger': 'Cheeseburger',
            'hamburger': 'Hamburger', 
            'big_mac': 'Big Mac',
            'quarter_pounder': 'Quarter Pounder',
            'mcdouble': 'McDouble',
            'filet_o_fish': 'Filet-O-Fish',
            'french_fries': 'French Fries',
            'nuggets': 'Chicken McNuggets',
            'mcnuggets': 'Chicken McNuggets',
            'coca_cola': 'Coca-Cola',
            'sprite': 'Sprite',
            'fanta': 'Fanta',
            'coffee': 'McCafé Coffee',
            'apple_pie': 'Apple Pie',
            'mcflurry': 'McFlurry',
            'sundae': 'Hot Fudge Sundae',
            'salad': 'Garden Salad',
            'wrap': 'Chicken Wrap',
            'muffin': 'English Muffin',
            'hash_browns': 'Hash Browns',
            'pancakes': 'Hotcakes'
        }
        
        # Greeting variations
        greetings = [
            "Hi, I'd like to place an order",
            "Hello, can I order some food?",
            "Hi there, I want to order",
            "Good morning, I'd like to order",
            "Hey, can I get some food?"
        ]
        
        # Agent responses
        agent_greetings = [
            "Hi! Welcome to McDonald's, I'd be happy to help you with your order today!",
            "Hello! Thanks for choosing McDonald's. What can I get for you?",
            "Hi there! I'm here to help you with your order. What would you like?",
            "Welcome to McDonald's! How can I assist you today?",
            "Hello! What can I get started for you today?"
        ]
        
        # Item ordering variations
        item_phrases = [
            "I'll have a {item}",
            "Can I get a {item}?",
            "I'd like a {item}",
            "Give me a {item}",
            "I want a {item}"
        ]
        
        # Agent confirmations
        confirmations = [
            "Great choice! A {item} is ${price}. Anything else?",
            "Perfect! That's a {item} for ${price}. What else can I get you?",
            "Excellent! A {item} for ${price}. Would you like anything else?",
            "Nice! A {item} is ${price}. Any other items?",
            "Good choice! That's ${price} for the {item}. Anything more?"
        ]
        
        # Completion phrases
        completions = [
            "That's everything, thanks",
            "No, that's all",
            "That's it for me",
            "I think that's everything",
            "No more items, thanks"
        ]
        
        # Final responses
        final_responses = [
            "Perfect! Your order is complete. Thank you for choosing McDonald's!",
            "Excellent! Your order is ready. Thanks for visiting McDonald's!",
            "Great! Your order is all set. Have a wonderful day!",
            "Perfect! Thanks for your order. Enjoy your meal!",
            "All done! Thank you for choosing McDonald's today!"
        ]
        
        # Generate conversation
        turns = []
        current_time = order_state.conversation_metrics.start_time
        
        # Turn 1: Customer greeting
        turns.append(ConversationTurn(
            speaker='user',
            text=random.choice(greetings),
            timestamp=current_time,
            turn_number=1
        ))
        current_time += timedelta(seconds=random.randint(1, 3))
        
        # Turn 2: Agent greeting
        turns.append(ConversationTurn(
            speaker='agent',
            text=random.choice(agent_greetings),
            timestamp=current_time,
            turn_number=2
        ))
        current_time += timedelta(seconds=random.randint(1, 2))
        
        # Turns 3-6: Order items (2-4 turns depending on items)
        turn_num = 3
        for i, item_id in enumerate(unique_items):
            item_name = item_names.get(item_id, item_id.replace('_', ' ').title())
            price = round(random.uniform(3.99, 8.99), 2)
            
            # Customer orders item
            turns.append(ConversationTurn(
                speaker='user',
                text=random.choice(item_phrases).format(item=item_name),
                timestamp=current_time,
                turn_number=turn_num
            ))
            current_time += timedelta(seconds=random.randint(1, 2))
            turn_num += 1
            
            # Agent confirms (except for last item)
            if i < len(unique_items) - 1:
                turns.append(ConversationTurn(
                    speaker='agent',
                    text=random.choice(confirmations).format(item=item_name, price=price),
                    timestamp=current_time,
                    turn_number=turn_num
                ))
                current_time += timedelta(seconds=random.randint(1, 2))
                turn_num += 1
        
        # Final confirmation for last item
        last_item = unique_items[-1]
        last_item_name = item_names.get(last_item, last_item.replace('_', ' ').title())
        last_price = round(random.uniform(3.99, 8.99), 2)
        turns.append(ConversationTurn(
            speaker='agent',
            text=random.choice(confirmations).format(item=last_item_name, price=last_price),
            timestamp=current_time,
            turn_number=turn_num
        ))
        current_time += timedelta(seconds=random.randint(1, 2))
        turn_num += 1
        
        # Customer says that's all
        turns.append(ConversationTurn(
            speaker='user',
            text=random.choice(completions),
            timestamp=current_time,
            turn_number=turn_num
        ))
        current_time += timedelta(seconds=random.randint(1, 2))
        turn_num += 1
        
        # Agent final response
        turns.append(ConversationTurn(
            speaker='agent',
            text=random.choice(final_responses),
            timestamp=order_state.conversation_metrics.end_time,
            turn_number=turn_num
        ))
        
        return turns
    
    async def _process_order_data(self, session: Session, conversation_id: UUID, order_state: OrderState):
        """Process order data and store in database"""
        try:
            # Create order record
            order_data = self.transformer.transform_order_state_to_db(order_state, conversation_id)
            order = Order(**order_data)
            session.add(order)
            session.flush()  # Get the ID
            
            # Create order items
            items_data = self.transformer.transform_order_items_to_db(order_state, order.id)
            for item_data in items_data:
                order_item = OrderItem(**item_data)
                session.add(order_item)
                
            self.logger.info(f"Processed {len(items_data)} order items")
            
        except Exception as e:
            self.logger.error(f"Failed to process order data: {e}")
            raise
    
    async def _process_transcript_data(self, session: Session, conversation_id: UUID, transcript_data: List[Dict]):
        """Process transcript data and store in database"""
        try:
            if not transcript_data:
                return
            
            for entry in transcript_data:
                # Create transcript record
                transcript = Transcript(
                    conversation_id=conversation_id,
                    speaker=entry['speaker'],
                    content=entry['text'],
                    turn_number=entry['turn_number']
                )
                session.add(transcript)
                
            self.logger.info(f"Processed {len(transcript_data)} transcript entries")
            
        except Exception as e:
            self.logger.error(f"Failed to process transcript data: {e}")
            raise
    
    async def _process_metrics_data(self, session: Session, conversation_id: UUID, metrics_data: Dict[str, Any]):
        """Process metrics data and store in database"""
        try:
            # Validate metrics data
            validated_metrics = self.validator.validate_metrics_data(metrics_data)
            
            # Create conversation metrics record
            metrics_record = ConversationMetrics(
                conversation_id=conversation_id,
                **validated_metrics.get('performance_metrics', {}),
                **validated_metrics.get('business_metrics', {}),
                popular_items=validated_metrics.get('popular_items', {}),
                popular_combos=validated_metrics.get('popular_combos', {}),
                popular_drinks=validated_metrics.get('popular_drinks', {}),
            )
            session.add(metrics_record)
            
            self.logger.info("Processed metrics data")
            
        except Exception as e:
            self.logger.error(f"Failed to process metrics data: {e}")
            raise
    
    async def get_conversation_by_session_id(self, session_id: str) -> Optional[ConversationResponse]:
        """Get conversation data by session ID"""
        try:
            with self.db.get_session() as session:
                conversation = session.query(Conversation).filter(
                    Conversation.session_id == session_id
                ).first()
                
                if not conversation:
                    return None
                
                return ConversationResponse.from_orm(conversation)
                
        except Exception as e:
            self.logger.error(f"Failed to get conversation: {e}")
            return None
    
    async def get_orders(self, limit: int = 50, offset: int = 0) -> List[OrderResponse]:
        """Get all orders with pagination"""
        try:
            with self.db.get_session() as session:
                orders = session.query(Order).offset(offset).limit(limit).all()
                
                result = []
                for order in orders:
                    # Get items first
                    items = session.query(OrderItem).filter(
                        OrderItem.order_id == order.id
                    ).all()
                    
                    # Create OrderResponse manually to avoid from_orm issues
                    order_data = OrderResponse(
                        id=order.id,
                        conversation_id=order.conversation_id,
                        order_id=order.order_id,
                        status=order.status,
                        total_price=order.total_price,
                        item_count=order.item_count,
                        created_at=order.created_at,
                        updated_at=order.updated_at,
                        applied_coupons=order.applied_coupons or [],
                        total_discount=order.total_discount or 0.0,
                        final_amount=order.final_amount or 0.0,
                        items=[
                            {
                                "id": str(item.id),
                                "order_id": str(item.order_id),
                                "item_id": item.item_id,
                                "item_type": item.item_type,
                                "item_name": item.item_name,
                                "size": item.size,
                                "price": float(item.price),
                                "quantity": item.quantity,
                                "created_at": item.created_at.isoformat()
                            }
                            for item in items
                        ]
                    )
                    result.append(order_data)
                
                return result
        except Exception as e:
            self.logger.error(f"Failed to get orders: {e}")
            raise

    async def get_orders_by_conversation_id(self, conversation_id: UUID) -> List[OrderResponse]:
        """Get orders by conversation ID"""
        try:
            with self.db.get_session() as session:
                orders = session.query(Order).filter(
                    Order.conversation_id == conversation_id
                ).all()
                
                result = []
                for order in orders:
                    # Get items first
                    items = session.query(OrderItem).filter(
                        OrderItem.order_id == order.id
                    ).all()
                    
                    # Create OrderResponse manually to avoid from_orm issues
                    order_data = OrderResponse(
                        id=order.id,
                        conversation_id=order.conversation_id,
                        order_id=order.order_id,
                        status=order.status,
                        total_price=order.total_price,
                        item_count=order.item_count,
                        created_at=order.created_at,
                        updated_at=order.updated_at,
                        applied_coupons=order.applied_coupons or [],
                        total_discount=order.total_discount or 0.0,
                        final_amount=order.final_amount or 0.0,
                        items=[
                            {
                                "id": str(item.id),
                                "order_id": str(item.order_id),
                                "item_id": item.item_id,
                                "item_type": item.item_type,
                                "item_name": item.item_name,
                                "size": item.size,
                                "price": float(item.price),
                                "quantity": item.quantity,
                                "created_at": item.created_at.isoformat()
                            }
                            for item in items
                        ]
                    )
                    result.append(order_data)
                
                return result
                
        except Exception as e:
            self.logger.error(f"Failed to get orders: {e}")
            return []
    
    async def get_daily_summary(self, date: datetime, location_id: Optional[str] = None) -> Optional[DailySummary]:
        """Get daily summary for a specific date and location"""
        try:
            with self.db.get_session() as session:
                query = session.query(DailySummary).filter(
                    DailySummary.date == date.date()
                )
                
                if location_id:
                    query = query.filter(DailySummary.location_id == location_id)
                
                return query.first()
                
        except Exception as e:
            self.logger.error(f"Failed to get daily summary: {e}")
            return None
    
    async def generate_daily_summary(self, date: datetime, location_id: Optional[str] = None):
        """Generate daily summary from conversation data"""
        try:
            with self.db.get_session() as session:
                # Query conversations for the date
                start_date = date.replace(hour=0, minute=0, second=0, microsecond=0)
                end_date = start_date.replace(hour=23, minute=59, second=59, microsecond=999999)
                
                query = session.query(Conversation).filter(
                    Conversation.start_time >= start_date,
                    Conversation.start_time <= end_date
                )
                
                if location_id:
                    query = query.filter(Conversation.location_id == location_id)
                
                conversations = query.all()
                
                if not conversations:
                    self.logger.info(f"No conversations found for date: {date.date()}")
                    return
                
                # Calculate summary metrics
                total_conversations = len(conversations)
                successful_conversations = len([c for c in conversations if c.success])
                failed_conversations = len([c for c in conversations if not c.success])
                cancelled_conversations = len([c for c in conversations if c.status == 'cancelled'])
                
                total_revenue = sum(c.orders[0].total_price for c in conversations if c.orders)
                average_order_value = total_revenue / len([c for c in conversations if c.orders]) if any(c.orders for c in conversations) else 0
                
                average_duration = sum(c.duration_seconds or 0 for c in conversations) / total_conversations
                
                total_errors = sum(c.error_count for c in conversations)
                total_interruptions = sum(c.interruption_count for c in conversations)
                
                # Create or update daily summary
                existing_summary = await self.get_daily_summary(date, location_id)
                
                if existing_summary:
                    # Update existing summary
                    existing_summary.total_conversations = total_conversations
                    existing_summary.successful_conversations = successful_conversations
                    existing_summary.failed_conversations = failed_conversations
                    existing_summary.cancelled_conversations = cancelled_conversations
                    existing_summary.total_revenue = total_revenue
                    existing_summary.average_order_value = average_order_value
                    existing_summary.average_conversation_duration = average_duration
                    existing_summary.total_errors = total_errors
                    existing_summary.total_interruptions = total_interruptions
                    existing_summary.updated_at = datetime.utcnow()
                else:
                    # Create new summary
                    summary = DailySummary(
                        location_id=location_id,
                        date=date.date(),
                        total_conversations=total_conversations,
                        successful_conversations=successful_conversations,
                        failed_conversations=failed_conversations,
                        cancelled_conversations=cancelled_conversations,
                        total_revenue=total_revenue,
                        average_order_value=average_order_value,
                        total_orders=len([c for c in conversations if c.orders]),
                        average_conversation_duration=average_duration,
                        total_errors=total_errors,
                        total_interruptions=total_interruptions,
                    )
                    session.add(summary)
                
                session.commit()
                self.logger.info(f"Generated daily summary for {date.date()}")
                
        except Exception as e:
            self.logger.error(f"Failed to generate daily summary: {e}")
            raise
    
    async def export_metrics_for_dashboard(self, session_id: str) -> Dict[str, Any]:
        """Export metrics data for dashboard consumption"""
        try:
            conversation = await self.get_conversation_by_session_id(session_id)
            if not conversation:
                return {'error': 'Conversation not found'}
            
            orders = await self.get_orders_by_conversation_id(conversation.id)
            
            return {
                'conversation': conversation.dict(),
                'orders': [order.dict() for order in orders],
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Failed to export metrics: {e}")
            return {'error': str(e)}


# Global data pipeline instance
data_pipeline = DataPipeline()
