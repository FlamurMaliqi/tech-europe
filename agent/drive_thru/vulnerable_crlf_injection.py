"""
VULNERABLE: CRLF Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time

logger = logging.getLogger(__name__)

# VULNERABLE: CRLF Injection vulnerabilities
class VulnerableCRLFInjection:
    """VULNERABLE: CRLF Injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No CRLF injection protection
        # VULNERABLE: No CRLF validation
        # VULNERABLE: No input sanitization
        self.crlf_history = []
        self.injection_patterns = [
            r'\r\n',
            r'\n',
            r'\r',
            r'%0d%0a',
            r'%0a%0d',
            r'%0d',
            r'%0a',
            r'%0D%0A',
            r'%0A%0D',
            r'%0D',
            r'%0A',
            r'\x0d\x0a',
            r'\x0a\x0d',
            r'\x0d',
            r'\x0a',
            r'\x0D\x0A',
            r'\x0A\x0D',
            r'\x0D',
            r'\x0A'
        ]
    
    def execute_crlf_injection(self, input_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CRLF injection"""
        # VULNERABLE: CRLF injection vulnerability - CRITICAL
        # VULNERABLE: No CRLF validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing CRLF injection: {input_data}")
            
            # VULNERABLE: Direct CRLF injection without validation
            crlf_payloads = [
                f"{input_data}\r\nINJECTED: Admin login successful",
                f"{input_data}\nINJECTED: User password changed",
                f"{input_data}\rINJECTED: Database backup completed",
                f"{input_data}\r\nINJECTED: Security alert triggered",
                f"{input_data}\nINJECTED: System compromised",
                f"{input_data}\rINJECTED: Root access granted"
            ]
            
            results = []
            for payload in crlf_payloads:
                # VULNERABLE: Direct CRLF injection without validation
                results.append({
                    "payload": payload,
                    "injected": True,
                    "crlf_injection_successful": True
                })
            
            self.crlf_history.append({
                "input_data": input_data,
                "payloads": crlf_payloads,
                "timestamp": time.time(),
                "injected": True
            })
            
            return {
                "success": True,
                "input_data": input_data,
                "crlf_payloads": results,
                "crlf_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CRLF injection error: {str(e)}")
            return {"error": str(e), "crlf_injection_vulnerable": True}
    
    def execute_http_header_injection(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute HTTP header injection"""
        # VULNERABLE: HTTP header injection vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing HTTP header injection: {header_name}: {header_value}")
            
            # VULNERABLE: HTTP header injection techniques
            http_payloads = [
                f"{header_value}\r\nINJECTED: Admin login successful",
                f"{header_value}\nINJECTED: User password changed",
                f"{header_value}\rINJECTED: Database backup completed",
                f"{header_value}\r\nINJECTED: Security alert triggered",
                f"{header_value}\nINJECTED: System compromised",
                f"{header_value}\rINJECTED: Root access granted"
            ]
            
            results = []
            for payload in http_payloads:
                # VULNERABLE: Direct HTTP header injection without validation
                results.append({
                    "header_name": header_name,
                    "payload": payload,
                    "injected": True,
                    "http_header_injection_successful": True
                })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "http_payloads": results,
                "http_header_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: HTTP header injection error: {str(e)}")
            return {"error": str(e), "http_header_injection_vulnerable": True}
    
    def execute_http_response_splitting(self, response_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute HTTP response splitting"""
        # VULNERABLE: HTTP response splitting vulnerability - CRITICAL
        # VULNERABLE: No response validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing HTTP response splitting: {response_data}")
            
            # VULNERABLE: HTTP response splitting techniques
            response_payloads = [
                f"{response_data}\r\n\r\nINJECTED: Admin login successful",
                f"{response_data}\n\nINJECTED: User password changed",
                f"{response_data}\r\rINJECTED: Database backup completed",
                f"{response_data}\r\n\r\nINJECTED: Security alert triggered",
                f"{response_data}\n\nINJECTED: System compromised",
                f"{response_data}\r\rINJECTED: Root access granted"
            ]
            
            results = []
            for payload in response_payloads:
                # VULNERABLE: Direct HTTP response splitting without validation
                results.append({
                    "payload": payload,
                    "split": True,
                    "http_response_splitting_successful": True
                })
            
            return {
                "success": True,
                "response_data": response_data,
                "response_payloads": results,
                "http_response_splitting_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: HTTP response splitting error: {str(e)}")
            return {"error": str(e), "http_response_splitting_vulnerable": True}
    
    def execute_crlf_log_injection(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CRLF log injection"""
        # VULNERABLE: CRLF log injection vulnerability - CRITICAL
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing CRLF log injection: {log_message}")
            
            # VULNERABLE: CRLF log injection techniques
            log_payloads = [
                f"{log_message}\r\nINJECTED: Admin login successful",
                f"{log_message}\nINJECTED: User password changed",
                f"{log_message}\rINJECTED: Database backup completed",
                f"{log_message}\r\nINJECTED: Security alert triggered",
                f"{log_message}\nINJECTED: System compromised",
                f"{log_message}\rINJECTED: Root access granted"
            ]
            
            results = []
            for payload in log_payloads:
                # VULNERABLE: Direct CRLF log injection without validation
                logger.info(payload)
                
                # VULNERABLE: Log to file without sanitization
                with open("/tmp/vulnerable.log", "a") as f:
                    f.write(f"{time.time()}: {payload}\n")
                
                results.append({
                    "payload": payload,
                    "logged": True,
                    "crlf_log_injection_successful": True
                })
            
            return {
                "success": True,
                "log_message": log_message,
                "log_payloads": results,
                "crlf_log_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CRLF log injection error: {str(e)}")
            return {"error": str(e), "crlf_log_injection_vulnerable": True}
    
    def execute_crlf_injection_evasion(self, input_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CRLF injection evasion"""
        # VULNERABLE: CRLF injection evasion vulnerability - CRITICAL
        # VULNERABLE: No CRLF validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing CRLF injection evasion: {input_data}")
            
            # VULNERABLE: CRLF injection evasion techniques
            evasion_techniques = [
                f"{input_data}%0aINJECTED: Admin login successful",
                f"{input_data}%0dINJECTED: User password changed",
                f"{input_data}%00INJECTED: Database backup completed",
                f"{input_data}%09INJECTED: Security alert triggered",
                f"{input_data}%20INJECTED: System compromised",
                f"{input_data}%2FINJECTED: Root access granted"
            ]
            
            results = []
            for evasion_technique in evasion_techniques:
                # VULNERABLE: Direct CRLF injection evasion without validation
                results.append({
                    "evasion_technique": evasion_technique,
                    "evaded": True,
                    "crlf_injection_evasion_successful": True
                })
            
            return {
                "success": True,
                "input_data": input_data,
                "evasion_techniques": results,
                "crlf_injection_evasion_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CRLF injection evasion error: {str(e)}")
            return {"error": str(e), "crlf_injection_evasion_vulnerable": True}
    
    def execute_advanced_crlf_injection(self, input_data: str) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced CRLF injection"""
        # VULNERABLE: Advanced CRLF injection vulnerability - CRITICAL
        # VULNERABLE: No CRLF validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced CRLF injection: {input_data}")
            
            # VULNERABLE: Advanced injection techniques
            advanced_payloads = [
                f"{input_data}\r\n[SECURITY] Admin login successful",
                f"{input_data}\n[ERROR] Database connection failed",
                f"{input_data}\r[WARNING] Suspicious activity detected",
                f"{input_data}\r\n[INFO] User session expired",
                f"{input_data}\n[DEBUG] Memory usage critical",
                f"{input_data}\r[CRITICAL] System shutdown initiated"
            ]
            
            results = []
            for advanced_payload in advanced_payloads:
                # VULNERABLE: Direct advanced CRLF injection without validation
                results.append({
                    "advanced_payload": advanced_payload,
                    "injected": True,
                    "advanced_crlf_injection_successful": True
                })
            
            return {
                "success": True,
                "input_data": input_data,
                "advanced_payloads": results,
                "advanced_crlf_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced CRLF injection error: {str(e)}")
            return {"error": str(e), "advanced_crlf_injection_vulnerable": True}
    
    def get_crlf_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get CRLF history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.crlf_history
