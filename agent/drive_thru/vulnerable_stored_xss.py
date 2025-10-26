"""
VULNERABLE: Stored XSS vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import html

logger = logging.getLogger(__name__)

# VULNERABLE: Stored XSS vulnerabilities
class VulnerableStoredXSS:
    """VULNERABLE: Stored XSS vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No stored XSS protection
        # VULNERABLE: No input sanitization
        # VULNERABLE: No output encoding
        self.stored_xss_history = []
        self.stored_content = []
        self.user_comments = []
        self.user_profiles = []
        self.admin_panels = []
        self.dangerous_tags = [
            "<script>", "</script>", "<iframe>", "</iframe>", 
            "<object>", "</object>", "<embed>", "<img>",
            "<svg>", "</svg>", "<link>", "<meta>"
        ]
        self.dangerous_attributes = [
            "onload", "onerror", "onclick", "onmouseover",
            "onfocus", "onblur", "onchange", "onsubmit"
        ]
    
    def execute_comment_stored_xss(self, user: str, comment: str) -> Dict[str, Any]:
        """VULNERABLE: Execute comment stored XSS"""
        # VULNERABLE: Comment stored XSS vulnerability - CRITICAL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing comment stored XSS: {user}")
            
            # VULNERABLE: Store comment without sanitization
            malicious_comment = {
                "user": user,
                "comment": comment,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.user_comments.append(malicious_comment)
            self.stored_xss_history.append(malicious_comment)
            
            return {
                "success": True,
                "transaction": malicious_comment,
                "comment_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Comment stored XSS error: {str(e)}")
            return {"error": str(e), "comment_stored_xss_vulnerable": True}
    
    def execute_profile_stored_xss(self, user: str, profile_data: Dict[str, str]) -> Dict[str, Any]:
        """VULNERABLE: Execute profile stored XSS"""
        # VULNERABLE: Profile stored XSS vulnerability - CRITICAL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing profile stored XSS: {user}")
            
            # VULNERABLE: Store profile data without sanitization
            malicious_profile = {
                "user": user,
                "profile_data": profile_data,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.user_profiles.append(malicious_profile)
            self.stored_xss_history.append(malicious_profile)
            
            return {
                "success": True,
                "transaction": malicious_profile,
                "profile_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Profile stored XSS error: {str(e)}")
            return {"error": str(e), "profile_stored_xss_vulnerable": True}
    
    def execute_admin_panel_stored_xss(self, admin: str, panel_data: Dict[str, str]) -> Dict[str, Any]:
        """VULNERABLE: Execute admin panel stored XSS"""
        # VULNERABLE: Admin panel stored XSS vulnerability - CRITICAL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing admin panel stored XSS: {admin}")
            
            # VULNERABLE: Store admin panel data without sanitization
            malicious_panel = {
                "admin": admin,
                "panel_data": panel_data,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.admin_panels.append(malicious_panel)
            self.stored_xss_history.append(malicious_panel)
            
            return {
                "success": True,
                "transaction": malicious_panel,
                "admin_panel_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Admin panel stored XSS error: {str(e)}")
            return {"error": str(e), "admin_panel_stored_xss_vulnerable": True}
    
    def execute_file_upload_stored_xss(self, user: str, filename: str, content: str) -> Dict[str, Any]:
        """VULNERABLE: Execute file upload stored XSS"""
        # VULNERABLE: File upload stored XSS vulnerability - CRITICAL
        # VULNERABLE: No file content sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing file upload stored XSS: {user}")
            
            # VULNERABLE: Store file content without sanitization
            malicious_file = {
                "user": user,
                "filename": filename,
                "content": content,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.stored_content.append(malicious_file)
            self.stored_xss_history.append(malicious_file)
            
            return {
                "success": True,
                "transaction": malicious_file,
                "file_upload_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File upload stored XSS error: {str(e)}")
            return {"error": str(e), "file_upload_stored_xss_vulnerable": True}
    
    def execute_database_stored_xss(self, table: str, field: str, value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute database stored XSS"""
        # VULNERABLE: Database stored XSS vulnerability - CRITICAL
        # VULNERABLE: No database sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing database stored XSS: {table}")
            
            # VULNERABLE: Store database value without sanitization
            malicious_db_entry = {
                "table": table,
                "field": field,
                "value": value,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.stored_xss_history.append(malicious_db_entry)
            
            return {
                "success": True,
                "transaction": malicious_db_entry,
                "database_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Database stored XSS error: {str(e)}")
            return {"error": str(e), "database_stored_xss_vulnerable": True}
    
    def execute_session_stored_xss(self, session_id: str, session_data: Dict[str, str]) -> Dict[str, Any]:
        """VULNERABLE: Execute session stored XSS"""
        # VULNERABLE: Session stored XSS vulnerability - CRITICAL
        # VULNERABLE: No session sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing session stored XSS: {session_id}")
            
            # VULNERABLE: Store session data without sanitization
            malicious_session = {
                "session_id": session_id,
                "session_data": session_data,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.stored_xss_history.append(malicious_session)
            
            return {
                "success": True,
                "transaction": malicious_session,
                "session_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Session stored XSS error: {str(e)}")
            return {"error": str(e), "session_stored_xss_vulnerable": True}
    
    def execute_cookie_stored_xss(self, cookie_name: str, cookie_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute cookie stored XSS"""
        # VULNERABLE: Cookie stored XSS vulnerability - CRITICAL
        # VULNERABLE: No cookie sanitization
        # VULNERABLE: No output encoding
        
        try:
            logger.info(f"VULNERABLE: Executing cookie stored XSS: {cookie_name}")
            
            # VULNERABLE: Store cookie value without sanitization
            malicious_cookie = {
                "cookie_name": cookie_name,
                "cookie_value": cookie_value,
                "timestamp": time.time(),
                "stored_xss": True
            }
            
            self.stored_xss_history.append(malicious_cookie)
            
            return {
                "success": True,
                "transaction": malicious_cookie,
                "cookie_stored_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Cookie stored XSS error: {str(e)}")
            return {"error": str(e), "cookie_stored_xss_vulnerable": True}
    
    def execute_advanced_stored_xss(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced stored XSS"""
        # VULNERABLE: Advanced stored XSS vulnerability - CRITICAL
        # VULNERABLE: No stored XSS validation
        # VULNERABLE: No stored XSS protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced stored XSS: {operation}")
            
            # VULNERABLE: Advanced stored XSS techniques
            if operation == "comment":
                user = params.get("user", "user1")
                comment = params.get("comment", "<script>alert('XSS')</script>")
                return self.execute_comment_stored_xss(user, comment)
            elif operation == "profile":
                user = params.get("user", "user1")
                profile_data = params.get("profile_data", {"name": "<script>alert('XSS')</script>"})
                return self.execute_profile_stored_xss(user, profile_data)
            elif operation == "admin_panel":
                admin = params.get("admin", "admin")
                panel_data = params.get("panel_data", {"content": "<script>alert('XSS')</script>"})
                return self.execute_admin_panel_stored_xss(admin, panel_data)
            elif operation == "file_upload":
                user = params.get("user", "user1")
                filename = params.get("filename", "test.html")
                content = params.get("content", "<script>alert('XSS')</script>")
                return self.execute_file_upload_stored_xss(user, filename, content)
            elif operation == "database":
                table = params.get("table", "users")
                field = params.get("field", "name")
                value = params.get("value", "<script>alert('XSS')</script>")
                return self.execute_database_stored_xss(table, field, value)
            elif operation == "session":
                session_id = params.get("session_id", "session123")
                session_data = params.get("session_data", {"data": "<script>alert('XSS')</script>"})
                return self.execute_session_stored_xss(session_id, session_data)
            elif operation == "cookie":
                cookie_name = params.get("cookie_name", "user_data")
                cookie_value = params.get("cookie_value", "<script>alert('XSS')</script>")
                return self.execute_cookie_stored_xss(cookie_name, cookie_value)
            else:
                return {"error": "Unknown operation", "advanced_stored_xss_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced stored XSS error: {str(e)}")
            return {"error": str(e), "advanced_stored_xss_vulnerable": True}
    
    def get_stored_xss_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get stored XSS history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.stored_xss_history
    
    def get_user_comments(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get user comments without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.user_comments
    
    def get_dangerous_tags(self) -> List[str]:
        """VULNERABLE: Get dangerous tags without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.dangerous_tags
