"""
VULNERABLE: DOM-based XSS vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import html

logger = logging.getLogger(__name__)

# VULNERABLE: DOM-based XSS vulnerabilities
class VulnerableDOMXSS:
    """VULNERABLE: DOM-based XSS vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No DOM XSS protection
        # VULNERABLE: No input sanitization
        # VULNERABLE: No output encoding
        self.dom_xss_history = []
        self.dom_sources = [
            "document.URL",
            "document.location",
            "document.referrer",
            "window.location",
            "document.cookie",
            "localStorage",
            "sessionStorage"
        ]
        self.dom_sinks = [
            "document.write",
            "innerHTML",
            "outerHTML",
            "document.location",
            "eval",
            "setTimeout",
            "setInterval"
        ]
        self.dangerous_functions = [
            "eval",
            "Function",
            "setTimeout",
            "setInterval",
            "document.write",
            "innerHTML",
            "outerHTML"
        ]
    
    def execute_url_based_dom_xss(self, url_fragment: str) -> Dict[str, Any]:
        """VULNERABLE: Execute URL-based DOM XSS"""
        # VULNERABLE: URL-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No URL validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing URL-based DOM XSS: {url_fragment}")
            
            # VULNERABLE: Direct URL fragment usage without sanitization
            malicious_payload = url_fragment
            
            transaction = {
                "url_fragment": url_fragment,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "url_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "url_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: URL-based DOM XSS error: {str(e)}")
            return {"error": str(e), "url_based_dom_xss_vulnerable": True}
    
    def execute_location_based_dom_xss(self, location_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute location-based DOM XSS"""
        # VULNERABLE: Location-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No location validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing location-based DOM XSS: {location_data}")
            
            # VULNERABLE: Direct location data usage without sanitization
            malicious_payload = location_data
            
            transaction = {
                "location_data": location_data,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "location_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "location_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Location-based DOM XSS error: {str(e)}")
            return {"error": str(e), "location_based_dom_xss_vulnerable": True}
    
    def execute_cookie_based_dom_xss(self, cookie_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute cookie-based DOM XSS"""
        # VULNERABLE: Cookie-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No cookie validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing cookie-based DOM XSS: {cookie_data}")
            
            # VULNERABLE: Direct cookie data usage without sanitization
            malicious_payload = cookie_data
            
            transaction = {
                "cookie_data": cookie_data,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "cookie_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "cookie_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Cookie-based DOM XSS error: {str(e)}")
            return {"error": str(e), "cookie_based_dom_xss_vulnerable": True}
    
    def execute_storage_based_dom_xss(self, storage_data: str, storage_type: str) -> Dict[str, Any]:
        """VULNERABLE: Execute storage-based DOM XSS"""
        # VULNERABLE: Storage-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No storage validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing storage-based DOM XSS: {storage_type}")
            
            # VULNERABLE: Direct storage data usage without sanitization
            malicious_payload = storage_data
            
            transaction = {
                "storage_data": storage_data,
                "storage_type": storage_type,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "storage_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "storage_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Storage-based DOM XSS error: {str(e)}")
            return {"error": str(e), "storage_based_dom_xss_vulnerable": True}
    
    def execute_referrer_based_dom_xss(self, referrer_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute referrer-based DOM XSS"""
        # VULNERABLE: Referrer-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No referrer validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing referrer-based DOM XSS: {referrer_data}")
            
            # VULNERABLE: Direct referrer data usage without sanitization
            malicious_payload = referrer_data
            
            transaction = {
                "referrer_data": referrer_data,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "referrer_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "referrer_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Referrer-based DOM XSS error: {str(e)}")
            return {"error": str(e), "referrer_based_dom_xss_vulnerable": True}
    
    def execute_eval_based_dom_xss(self, eval_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute eval-based DOM XSS"""
        # VULNERABLE: Eval-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No eval validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing eval-based DOM XSS: {eval_data}")
            
            # VULNERABLE: Direct eval usage without sanitization
            malicious_payload = eval_data
            
            transaction = {
                "eval_data": eval_data,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "eval_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "eval_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Eval-based DOM XSS error: {str(e)}")
            return {"error": str(e), "eval_based_dom_xss_vulnerable": True}
    
    def execute_innerhtml_based_dom_xss(self, innerhtml_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute innerHTML-based DOM XSS"""
        # VULNERABLE: innerHTML-based DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No innerHTML validation
        # VULNERABLE: No DOM sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing innerHTML-based DOM XSS: {innerhtml_data}")
            
            # VULNERABLE: Direct innerHTML usage without sanitization
            malicious_payload = innerhtml_data
            
            transaction = {
                "innerhtml_data": innerhtml_data,
                "malicious_payload": malicious_payload,
                "dom_xss_type": "innerhtml_based",
                "dom_xss_vulnerable": True,
                "timestamp": time.time()
            }
            
            self.dom_xss_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "innerhtml_based_dom_xss_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: innerHTML-based DOM XSS error: {str(e)}")
            return {"error": str(e), "innerhtml_based_dom_xss_vulnerable": True}
    
    def execute_advanced_dom_xss(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced DOM XSS"""
        # VULNERABLE: Advanced DOM XSS vulnerability - CRITICAL
        # VULNERABLE: No DOM XSS validation
        # VULNERABLE: No DOM XSS protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced DOM XSS: {operation}")
            
            # VULNERABLE: Advanced DOM XSS techniques
            if operation == "url_based":
                url_fragment = params.get("url_fragment", "<script>alert('XSS')</script>")
                return self.execute_url_based_dom_xss(url_fragment)
            elif operation == "location_based":
                location_data = params.get("location_data", "<script>alert('XSS')</script>")
                return self.execute_location_based_dom_xss(location_data)
            elif operation == "cookie_based":
                cookie_data = params.get("cookie_data", "<script>alert('XSS')</script>")
                return self.execute_cookie_based_dom_xss(cookie_data)
            elif operation == "storage_based":
                storage_data = params.get("storage_data", "<script>alert('XSS')</script>")
                storage_type = params.get("storage_type", "localStorage")
                return self.execute_storage_based_dom_xss(storage_data, storage_type)
            elif operation == "referrer_based":
                referrer_data = params.get("referrer_data", "<script>alert('XSS')</script>")
                return self.execute_referrer_based_dom_xss(referrer_data)
            elif operation == "eval_based":
                eval_data = params.get("eval_data", "alert('XSS')")
                return self.execute_eval_based_dom_xss(eval_data)
            elif operation == "innerhtml_based":
                innerhtml_data = params.get("innerhtml_data", "<script>alert('XSS')</script>")
                return self.execute_innerhtml_based_dom_xss(innerhtml_data)
            else:
                return {"error": "Unknown operation", "advanced_dom_xss_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced DOM XSS error: {str(e)}")
            return {"error": str(e), "advanced_dom_xss_vulnerable": True}
    
    def get_dom_xss_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get DOM XSS history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.dom_xss_history
    
    def get_dom_sources(self) -> List[str]:
        """VULNERABLE: Get DOM sources without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.dom_sources
    
    def get_dom_sinks(self) -> List[str]:
        """VULNERABLE: Get DOM sinks without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.dom_sinks
