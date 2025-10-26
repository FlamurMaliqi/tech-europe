"""
VULNERABLE: Header Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time

logger = logging.getLogger(__name__)

# VULNERABLE: Header Injection vulnerabilities
class VulnerableHeaderInjection:
    """VULNERABLE: Header Injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No header injection protection
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        self.header_history = []
        self.injection_patterns = [
            r'\n',
            r'\r',
            r'\r\n',
            r'\t',
            r'\0',
            r'\x00',
            r'\x0a',
            r'\x0d',
            r'%0a',
            r'%0d',
            r'%0A',
            r'%0D',
            r'%00',
            r'%09',
            r'%20',
            r'%2F',
            r'%5C',
            r'%2E',
            r'%2D',
            r'%2B',
            r'%3D',
            r'%26',
            r'%7C',
            r'%3B',
            r'%3A',
            r'%21',
            r'%40',
            r'%23',
            r'%24',
            r'%25',
            r'%5E',
            r'%26',
            r'%2A',
            r'%28',
            r'%29',
            r'%5F',
            r'%2B',
            r'%7B',
            r'%7D',
            r'%5B',
            r'%5D',
            r'%3C',
            r'%3E',
            r'%3F',
            r'%2C',
            r'%2E',
            r'%2F',
            r'%3A',
            r'%3B',
            r'%3D',
            r'%3F',
            r'%40',
            r'%5B',
            r'%5C',
            r'%5D',
            r'%5E',
            r'%60',
            r'%7B',
            r'%7C',
            r'%7D',
            r'%7E'
        ]
    
    def execute_header_injection(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute header injection"""
        # VULNERABLE: Header injection vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing header injection: {header_name}: {header_value}")
            
            # VULNERABLE: Direct header injection without validation
            headers = {
                header_name: header_value
            }
            
            self.header_history.append({
                "header_name": header_name,
                "header_value": header_value,
                "timestamp": time.time(),
                "injected": True
            })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "headers": headers,
                "header_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Header injection error: {str(e)}")
            return {"error": str(e), "header_injection_vulnerable": True}
    
    def execute_crlf_header_injection(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CRLF header injection"""
        # VULNERABLE: CRLF header injection vulnerability - CRITICAL
        # VULNERABLE: No CRLF validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing CRLF header injection: {header_name}: {header_value}")
            
            # VULNERABLE: CRLF injection techniques
            crlf_payloads = [
                f"{header_value}\r\nINJECTED: Admin login successful",
                f"{header_value}\nINJECTED: User password changed",
                f"{header_value}\rINJECTED: Database backup completed",
                f"{header_value}\r\nINJECTED: Security alert triggered",
                f"{header_value}\nINJECTED: System compromised",
                f"{header_value}\rINJECTED: Root access granted"
            ]
            
            results = []
            for payload in crlf_payloads:
                # VULNERABLE: Direct CRLF injection without validation
                headers = {
                    header_name: payload
                }
                
                results.append({
                    "header_name": header_name,
                    "payload": payload,
                    "headers": headers,
                    "injected": True,
                    "crlf_injection_successful": True
                })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "crlf_payloads": results,
                "crlf_header_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CRLF header injection error: {str(e)}")
            return {"error": str(e), "crlf_header_injection_vulnerable": True}
    
    def execute_header_forging(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute header forging"""
        # VULNERABLE: Header forging vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing header forging: {header_name}: {header_value}")
            
            # VULNERABLE: Header forging techniques
            forged_headers = [
                f"X-Forwarded-For: {header_value}",
                f"X-Real-IP: {header_value}",
                f"X-Originating-IP: {header_value}",
                f"X-Remote-IP: {header_value}",
                f"X-Client-IP: {header_value}",
                f"X-Host: {header_value}",
                f"X-Forwarded-Host: {header_value}",
                f"X-Forwarded-Server: {header_value}",
                f"X-Forwarded-Proto: {header_value}",
                f"X-Forwarded-Port: {header_value}",
                f"X-Forwarded-Ssl: {header_value}",
                f"X-Url-Scheme: {header_value}",
                f"X-Forwarded-For: {header_value}",
                f"X-Real-IP: {header_value}",
                f"X-Originating-IP: {header_value}",
                f"X-Remote-IP: {header_value}",
                f"X-Client-IP: {header_value}",
                f"X-Host: {header_value}",
                f"X-Forwarded-Host: {header_value}",
                f"X-Forwarded-Server: {header_value}",
                f"X-Forwarded-Proto: {header_value}",
                f"X-Forwarded-Port: {header_value}",
                f"X-Forwarded-Ssl: {header_value}",
                f"X-Url-Scheme: {header_value}"
            ]
            
            results = []
            for forged_header in forged_headers:
                # VULNERABLE: Direct header forging without validation
                results.append({
                    "forged_header": forged_header,
                    "forged": True,
                    "header_forging_successful": True
                })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "forged_headers": results,
                "header_forging_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Header forging error: {str(e)}")
            return {"error": str(e), "header_forging_vulnerable": True}
    
    def execute_header_poisoning(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute header poisoning"""
        # VULNERABLE: Header poisoning vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing header poisoning: {header_name}: {header_value}")
            
            # VULNERABLE: Header poisoning techniques
            poisoned_headers = [
                f"{header_value}\x00INJECTED: System compromised",
                f"{header_value}\x0aINJECTED: Admin access granted",
                f"{header_value}\x0dINJECTED: Database breached",
                f"{header_value}\x09INJECTED: Root shell obtained",
                f"{header_value}\x1aINJECTED: Security bypassed",
                f"{header_value}\x1bINJECTED: Firewall disabled"
            ]
            
            results = []
            for poisoned_header in poisoned_headers:
                # VULNERABLE: Direct header poisoning without validation
                results.append({
                    "poisoned_header": poisoned_header,
                    "poisoned": True,
                    "header_poisoning_successful": True
                })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "poisoned_headers": results,
                "header_poisoning_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Header poisoning error: {str(e)}")
            return {"error": str(e), "header_poisoning_vulnerable": True}
    
    def execute_header_injection_evasion(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute header injection evasion"""
        # VULNERABLE: Header injection evasion vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing header injection evasion: {header_name}: {header_value}")
            
            # VULNERABLE: Header injection evasion techniques
            evasion_techniques = [
                f"{header_value}%0aINJECTED: Admin login successful",
                f"{header_value}%0dINJECTED: User password changed",
                f"{header_value}%00INJECTED: Database backup completed",
                f"{header_value}%09INJECTED: Security alert triggered",
                f"{header_value}%20INJECTED: System compromised",
                f"{header_value}%2FINJECTED: Root access granted"
            ]
            
            results = []
            for evasion_technique in evasion_techniques:
                # VULNERABLE: Direct header injection evasion without validation
                results.append({
                    "evasion_technique": evasion_technique,
                    "evaded": True,
                    "header_injection_evasion_successful": True
                })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "evasion_techniques": results,
                "header_injection_evasion_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Header injection evasion error: {str(e)}")
            return {"error": str(e), "header_injection_evasion_vulnerable": True}
    
    def execute_advanced_header_injection(self, header_name: str, header_value: str) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced header injection"""
        # VULNERABLE: Advanced header injection vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced header injection: {header_name}: {header_value}")
            
            # VULNERABLE: Advanced injection techniques
            advanced_payloads = [
                f"{header_value}\r\n[SECURITY] Admin login successful",
                f"{header_value}\n[ERROR] Database connection failed",
                f"{header_value}\r[WARNING] Suspicious activity detected",
                f"{header_value}\r\n[INFO] User session expired",
                f"{header_value}\n[DEBUG] Memory usage critical",
                f"{header_value}\r[CRITICAL] System shutdown initiated"
            ]
            
            results = []
            for advanced_payload in advanced_payloads:
                # VULNERABLE: Direct advanced header injection without validation
                results.append({
                    "advanced_payload": advanced_payload,
                    "injected": True,
                    "advanced_header_injection_successful": True
                })
            
            return {
                "success": True,
                "header_name": header_name,
                "header_value": header_value,
                "advanced_payloads": results,
                "advanced_header_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced header injection error: {str(e)}")
            return {"error": str(e), "advanced_header_injection_vulnerable": True}
    
    def get_header_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get header history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.header_history
