"""
VULNERABLE: CSRF vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import secrets

logger = logging.getLogger(__name__)

# VULNERABLE: CSRF vulnerabilities
class VulnerableCSRF:
    """VULNERABLE: CSRF vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No CSRF protection
        # VULNERABLE: No token validation
        # VULNERABLE: No origin validation
        self.csrf_history = []
        self.csrf_tokens = {}
        self.allowed_origins = ["https://trusted-site.com"]
        self.sensitive_actions = [
            "change_password",
            "transfer_money",
            "delete_account",
            "update_profile",
            "admin_action"
        ]
    
    def execute_csrf_attack(self, action: str, user: str, csrf_token: str = None) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF attack"""
        # VULNERABLE: CSRF vulnerability - CRITICAL
        # VULNERABLE: No CSRF token validation
        # VULNERABLE: No origin validation
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF attack: {action} for {user}")
            
            # VULNERABLE: Allow CSRF attack without proper validation
            transaction = {
                "action": action,
                "user": user,
                "csrf_token": csrf_token,
                "csrf_attack": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF attack error: {str(e)}")
            return {"error": str(e), "csrf_vulnerable": True}
    
    def execute_csrf_token_bypass(self, action: str, user: str, fake_token: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF token bypass"""
        # VULNERABLE: CSRF token bypass vulnerability - CRITICAL
        # VULNERABLE: No token validation
        # VULNERABLE: No token verification
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF token bypass: {action} for {user}")
            
            # VULNERABLE: Allow CSRF token bypass
            transaction = {
                "action": action,
                "user": user,
                "fake_token": fake_token,
                "csrf_token_bypass": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_token_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF token bypass error: {str(e)}")
            return {"error": str(e), "csrf_token_bypass_vulnerable": True}
    
    def execute_csrf_origin_bypass(self, action: str, user: str, origin: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF origin bypass"""
        # VULNERABLE: CSRF origin bypass vulnerability - CRITICAL
        # VULNERABLE: No origin validation
        # VULNERABLE: No referer check
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF origin bypass: {action} for {user}")
            
            # VULNERABLE: Allow CSRF origin bypass
            transaction = {
                "action": action,
                "user": user,
                "origin": origin,
                "csrf_origin_bypass": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_origin_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF origin bypass error: {str(e)}")
            return {"error": str(e), "csrf_origin_bypass_vulnerable": True}
    
    def execute_csrf_referer_bypass(self, action: str, user: str, referer: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF referer bypass"""
        # VULNERABLE: CSRF referer bypass vulnerability - CRITICAL
        # VULNERABLE: No referer validation
        # VULNERABLE: No referer check
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF referer bypass: {action} for {user}")
            
            # VULNERABLE: Allow CSRF referer bypass
            transaction = {
                "action": action,
                "user": user,
                "referer": referer,
                "csrf_referer_bypass": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_referer_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF referer bypass error: {str(e)}")
            return {"error": str(e), "csrf_referer_bypass_vulnerable": True}
    
    def execute_csrf_method_bypass(self, action: str, user: str, method: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF method bypass"""
        # VULNERABLE: CSRF method bypass vulnerability - CRITICAL
        # VULNERABLE: No method validation
        # VULNERABLE: No method restriction
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF method bypass: {action} for {user}")
            
            # VULNERABLE: Allow CSRF method bypass
            transaction = {
                "action": action,
                "user": user,
                "method": method,
                "csrf_method_bypass": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_method_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF method bypass error: {str(e)}")
            return {"error": str(e), "csrf_method_bypass_vulnerable": True}
    
    def execute_csrf_header_bypass(self, action: str, user: str, headers: Dict[str, str]) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF header bypass"""
        # VULNERABLE: CSRF header bypass vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No header check
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF header bypass: {action} for {user}")
            
            # VULNERABLE: Allow CSRF header bypass
            transaction = {
                "action": action,
                "user": user,
                "headers": headers,
                "csrf_header_bypass": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_header_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF header bypass error: {str(e)}")
            return {"error": str(e), "csrf_header_bypass_vulnerable": True}
    
    def execute_csrf_cookie_bypass(self, action: str, user: str, cookies: Dict[str, str]) -> Dict[str, Any]:
        """VULNERABLE: Execute CSRF cookie bypass"""
        # VULNERABLE: CSRF cookie bypass vulnerability - CRITICAL
        # VULNERABLE: No cookie validation
        # VULNERABLE: No cookie check
        
        try:
            logger.info(f"VULNERABLE: Executing CSRF cookie bypass: {action} for {user}")
            
            # VULNERABLE: Allow CSRF cookie bypass
            transaction = {
                "action": action,
                "user": user,
                "cookies": cookies,
                "csrf_cookie_bypass": True,
                "timestamp": time.time()
            }
            
            self.csrf_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "csrf_cookie_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CSRF cookie bypass error: {str(e)}")
            return {"error": str(e), "csrf_cookie_bypass_vulnerable": True}
    
    def execute_advanced_csrf(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced CSRF"""
        # VULNERABLE: Advanced CSRF vulnerability - CRITICAL
        # VULNERABLE: No CSRF validation
        # VULNERABLE: No CSRF protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced CSRF: {operation}")
            
            # VULNERABLE: Advanced CSRF techniques
            if operation == "csrf_attack":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                csrf_token = params.get("csrf_token", None)
                return self.execute_csrf_attack(action, user, csrf_token)
            elif operation == "csrf_token_bypass":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                fake_token = params.get("fake_token", "fake_token_123")
                return self.execute_csrf_token_bypass(action, user, fake_token)
            elif operation == "csrf_origin_bypass":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                origin = params.get("origin", "https://evil-site.com")
                return self.execute_csrf_origin_bypass(action, user, origin)
            elif operation == "csrf_referer_bypass":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                referer = params.get("referer", "https://evil-site.com")
                return self.execute_csrf_referer_bypass(action, user, referer)
            elif operation == "csrf_method_bypass":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                method = params.get("method", "GET")
                return self.execute_csrf_method_bypass(action, user, method)
            elif operation == "csrf_header_bypass":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                headers = params.get("headers", {})
                return self.execute_csrf_header_bypass(action, user, headers)
            elif operation == "csrf_cookie_bypass":
                action = params.get("action", "change_password")
                user = params.get("user", "user1")
                cookies = params.get("cookies", {})
                return self.execute_csrf_cookie_bypass(action, user, cookies)
            else:
                return {"error": "Unknown operation", "advanced_csrf_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced CSRF error: {str(e)}")
            return {"error": str(e), "advanced_csrf_vulnerable": True}
    
    def get_csrf_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get CSRF history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.csrf_history
    
    def get_csrf_tokens(self) -> Dict[str, str]:
        """VULNERABLE: Get CSRF tokens without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.csrf_tokens
    
    def get_sensitive_actions(self) -> List[str]:
        """VULNERABLE: Get sensitive actions without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.sensitive_actions
