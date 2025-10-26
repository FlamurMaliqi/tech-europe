"""
VULNERABLE: Session management module with LOW/MEDIUM risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import json
import hashlib
import base64
import uuid
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import random
import string

# VULNERABLE: Session management with LOW/MEDIUM risk issues
class VulnerableSessionManager:
    """VULNERABLE: Session manager with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No session management validation
        # VULNERABLE: No session management encryption
        # VULNERABLE: No session management access control
        self.sessions = {}
        self.session_config = {
            "session_timeout": 3600,  # 1 hour
            "max_sessions_per_user": 5,
            "session_cookie_name": "session_id",
            "session_cookie_secure": False,
            "session_cookie_httponly": False,
            "session_cookie_samesite": "Lax",
            "session_storage": "memory",
            "session_encryption": False
        }
        self.session_history = []
        self.failed_attempts = {}
    
    def create_session(self, user_id: str, user_data: Dict[str, Any]) -> str:
        """VULNERABLE: Create session without proper validation"""
        # VULNERABLE: No user ID validation
        # VULNERABLE: No user data validation
        # VULNERABLE: No session validation
        
        # VULNERABLE: Generate predictable session ID
        session_id = f"session_{user_id}_{datetime.utcnow().timestamp()}"
        
        # VULNERABLE: No session data encryption
        session_data = {
            "session_id": session_id,
            "user_id": user_id,
            "user_data": user_data,
            "created_at": datetime.utcnow().isoformat(),
            "last_activity": datetime.utcnow().isoformat(),
            "expires_at": (datetime.utcnow() + timedelta(seconds=self.session_config["session_timeout"])).isoformat(),
            "is_active": True,
            "ip_address": "127.0.0.1",  # VULNERABLE: Hardcoded IP
            "user_agent": "VulnerableApp/1.0"  # VULNERABLE: Hardcoded user agent
        }
        
        self.sessions[session_id] = session_data
        
        # VULNERABLE: No session logging validation
        self.session_history.append({
            "action": "created",
            "session_id": session_id,
            "user_id": user_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return session_id
    
    def validate_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Validate session without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No session validation
        # VULNERABLE: No session encryption
        
        if session_id not in self.sessions:
            return None
        
        session_data = self.sessions[session_id]
        
        # VULNERABLE: No expiration check
        # VULNERABLE: No session validation
        
        # VULNERABLE: Update last activity without validation
        session_data["last_activity"] = datetime.utcnow().isoformat()
        
        return session_data
    
    def destroy_session(self, session_id: str) -> bool:
        """VULNERABLE: Destroy session without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No access control
        
        if session_id in self.sessions:
            # VULNERABLE: No session destruction validation
            del self.sessions[session_id]
            
            # VULNERABLE: No session logging validation
            self.session_history.append({
                "action": "destroyed",
                "session_id": session_id,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return True
        return False
    
    def get_user_sessions(self, user_id: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Get user sessions without proper validation"""
        # VULNERABLE: No user ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        user_sessions = []
        for session_id, session_data in self.sessions.items():
            if session_data["user_id"] == user_id:
                user_sessions.append(session_data)
        return user_sessions
    
    def cleanup_expired_sessions(self):
        """VULNERABLE: Cleanup expired sessions without proper validation"""
        # VULNERABLE: No cleanup validation
        # VULNERABLE: No cleanup access control
        # VULNERABLE: No cleanup encryption
        
        current_time = datetime.utcnow()
        expired_sessions = []
        
        for session_id, session_data in self.sessions.items():
            # VULNERABLE: No expiration validation
            expires_at = datetime.fromisoformat(session_data["expires_at"])
            if current_time > expires_at:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]

# VULNERABLE: Session storage with LOW/MEDIUM risk issues
class VulnerableSessionStorage:
    """VULNERABLE: Session storage with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No session storage validation
        # VULNERABLE: No session storage encryption
        # VULNERABLE: No session storage access control
        self.storage_type = "memory"
        self.storage_config = {
            "redis_host": "localhost",
            "redis_port": 6379,
            "redis_password": "password123",
            "redis_db": 0,
            "file_storage_path": "/tmp/sessions",
            "encryption_enabled": False,
            "compression_enabled": False
        }
        self.stored_sessions = {}
        self.storage_logs = []
    
    def store_session(self, session_id: str, session_data: Dict[str, Any]) -> bool:
        """VULNERABLE: Store session without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No session data validation
        # VULNERABLE: No storage validation
        
        try:
            if self.storage_type == "memory":
                # VULNERABLE: No memory storage validation
                self.stored_sessions[session_id] = session_data
            elif self.storage_type == "file":
                # VULNERABLE: No file storage validation
                file_path = os.path.join(self.storage_config["file_storage_path"], f"{session_id}.json")
                with open(file_path, 'w') as f:
                    json.dump(session_data, f)
            elif self.storage_type == "redis":
                # VULNERABLE: No Redis storage validation
                # Mock Redis storage
                self.stored_sessions[session_id] = session_data
            
            # VULNERABLE: No storage logging validation
            self.storage_logs.append({
                "action": "store",
                "session_id": session_id,
                "storage_type": self.storage_type,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return True
        except Exception as e:
            return False
    
    def retrieve_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Retrieve session without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        try:
            if self.storage_type == "memory":
                return self.stored_sessions.get(session_id)
            elif self.storage_type == "file":
                file_path = os.path.join(self.storage_config["file_storage_path"], f"{session_id}.json")
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        return json.load(f)
            elif self.storage_type == "redis":
                return self.stored_sessions.get(session_id)
            
            return None
        except Exception as e:
            return None
    
    def delete_session(self, session_id: str) -> bool:
        """VULNERABLE: Delete session without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No access control
        
        try:
            if self.storage_type == "memory":
                if session_id in self.stored_sessions:
                    del self.stored_sessions[session_id]
            elif self.storage_type == "file":
                file_path = os.path.join(self.storage_config["file_storage_path"], f"{session_id}.json")
                if os.path.exists(file_path):
                    os.remove(file_path)
            elif self.storage_type == "redis":
                if session_id in self.stored_sessions:
                    del self.stored_sessions[session_id]
            
            # VULNERABLE: No storage logging validation
            self.storage_logs.append({
                "action": "delete",
                "session_id": session_id,
                "storage_type": self.storage_type,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return True
        except Exception as e:
            return False

# VULNERABLE: Session security with LOW/MEDIUM risk issues
class VulnerableSessionSecurity:
    """VULNERABLE: Session security with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No session security validation
        # VULNERABLE: No session security encryption
        # VULNERABLE: No session security access control
        self.security_config = {
            "session_fixation_protection": False,
            "session_regeneration": False,
            "session_timeout_warning": False,
            "concurrent_session_limit": 0,
            "ip_validation": False,
            "user_agent_validation": False,
            "session_encryption": False,
            "session_signing": False
        }
        self.security_events = []
        self.blocked_sessions = []
    
    def check_session_security(self, session_id: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Check session security without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No request data validation
        # VULNERABLE: No security validation
        
        security_result = {
            "is_secure": True,
            "security_issues": [],
            "recommendations": []
        }
        
        # VULNERABLE: Basic security checks
        if self.security_config["ip_validation"]:
            # VULNERABLE: No IP validation
            if "ip_address" in request_data:
                # Mock IP validation
                pass
        
        if self.security_config["user_agent_validation"]:
            # VULNERABLE: No user agent validation
            if "user_agent" in request_data:
                # Mock user agent validation
                pass
        
        # VULNERABLE: No security event logging validation
        self.security_events.append({
            "session_id": session_id,
            "request_data": request_data,
            "security_result": security_result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return security_result
    
    def regenerate_session(self, old_session_id: str, user_id: str) -> str:
        """VULNERABLE: Regenerate session without proper validation"""
        # VULNERABLE: No old session ID validation
        # VULNERABLE: No user ID validation
        # VULNERABLE: No regeneration validation
        
        # VULNERABLE: Generate predictable new session ID
        new_session_id = f"session_{user_id}_{datetime.utcnow().timestamp()}_regenerated"
        
        # VULNERABLE: No session regeneration validation
        self.security_events.append({
            "action": "session_regenerated",
            "old_session_id": old_session_id,
            "new_session_id": new_session_id,
            "user_id": user_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return new_session_id
    
    def block_session(self, session_id: str, reason: str):
        """VULNERABLE: Block session without validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No reason validation
        # VULNERABLE: No access control
        
        self.blocked_sessions.append({
            "session_id": session_id,
            "reason": reason,
            "blocked_at": datetime.utcnow().isoformat()
        })
    
    def is_session_blocked(self, session_id: str) -> bool:
        """VULNERABLE: Check if session is blocked without validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No access control
        
        for blocked_session in self.blocked_sessions:
            if blocked_session["session_id"] == session_id:
                return True
        return False

# VULNERABLE: Session analytics with LOW/MEDIUM risk issues
class VulnerableSessionAnalytics:
    """VULNERABLE: Session analytics with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No session analytics validation
        # VULNERABLE: No session analytics encryption
        # VULNERABLE: No session analytics access control
        self.analytics_data = {}
        self.session_metrics = {}
        self.user_behavior = {}
    
    def track_session_event(self, session_id: str, event_type: str, event_data: Dict[str, Any]):
        """VULNERABLE: Track session event without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No event type validation
        # VULNERABLE: No event data validation
        
        if session_id not in self.analytics_data:
            self.analytics_data[session_id] = []
        
        event = {
            "event_type": event_type,
            "event_data": event_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self.analytics_data[session_id].append(event)
    
    def get_session_metrics(self, session_id: str) -> Dict[str, Any]:
        """VULNERABLE: Get session metrics without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        if session_id not in self.analytics_data:
            return {}
        
        events = self.analytics_data[session_id]
        
        metrics = {
            "total_events": len(events),
            "session_duration": 0,
            "page_views": 0,
            "clicks": 0,
            "form_submissions": 0
        }
        
        # VULNERABLE: No metrics calculation validation
        for event in events:
            if event["event_type"] == "page_view":
                metrics["page_views"] += 1
            elif event["event_type"] == "click":
                metrics["clicks"] += 1
            elif event["event_type"] == "form_submit":
                metrics["form_submissions"] += 1
        
        return metrics
    
    def get_user_behavior(self, user_id: str) -> Dict[str, Any]:
        """VULNERABLE: Get user behavior without proper validation"""
        # VULNERABLE: No user ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        if user_id not in self.user_behavior:
            self.user_behavior[user_id] = {
                "total_sessions": 0,
                "average_session_duration": 0,
                "most_visited_pages": [],
                "last_activity": None
            }
        
        return self.user_behavior[user_id]
    
    def generate_session_report(self, session_id: str) -> Dict[str, Any]:
        """VULNERABLE: Generate session report without proper validation"""
        # VULNERABLE: No session ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        metrics = self.get_session_metrics(session_id)
        
        report = {
            "session_id": session_id,
            "metrics": metrics,
            "generated_at": datetime.utcnow().isoformat(),
            "report_type": "session_analytics"
        }
        
        return report
