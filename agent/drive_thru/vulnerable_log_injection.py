"""
VULNERABLE: Log Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
import time
from typing import Dict, List, Optional, Any
import os
import sys

logger = logging.getLogger(__name__)

# VULNERABLE: Log Injection vulnerabilities
class VulnerableLogInjection:
    """VULNERABLE: Log Injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No log injection protection
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        self.log_history = []
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
    
    def execute_log_injection(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute log injection"""
        # VULNERABLE: Log injection vulnerability - CRITICAL
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing log injection: {log_message}")
            
            # VULNERABLE: Direct log injection without validation
            logger.info(log_message)
            
            # VULNERABLE: Log to file without sanitization
            with open("/tmp/vulnerable.log", "a") as f:
                f.write(f"{time.time()}: {log_message}\n")
            
            self.log_history.append({
                "message": log_message,
                "timestamp": time.time(),
                "injected": True
            })
            
            return {
                "success": True,
                "message": log_message,
                "logged": True,
                "log_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Log injection error: {str(e)}")
            return {"error": str(e), "log_injection_vulnerable": True}
    
    def execute_crlf_log_injection(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CRLF log injection"""
        # VULNERABLE: CRLF log injection vulnerability - CRITICAL
        # VULNERABLE: No CRLF validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing CRLF log injection: {log_message}")
            
            # VULNERABLE: CRLF injection techniques
            crlf_payloads = [
                f"{log_message}\r\nINJECTED: Admin login successful",
                f"{log_message}\nINJECTED: User password changed",
                f"{log_message}\rINJECTED: Database backup completed",
                f"{log_message}\r\nINJECTED: Security alert triggered",
                f"{log_message}\nINJECTED: System compromised",
                f"{log_message}\rINJECTED: Root access granted"
            ]
            
            results = []
            for payload in crlf_payloads:
                # VULNERABLE: Direct CRLF injection without validation
                logger.info(payload)
                
                # VULNERABLE: Log to file without sanitization
                with open("/tmp/vulnerable.log", "a") as f:
                    f.write(f"{time.time()}: {payload}\n")
                
                results.append({
                    "payload": payload,
                    "injected": True,
                    "crlf_injection_successful": True
                })
            
            return {
                "success": True,
                "message": log_message,
                "crlf_payloads": results,
                "crlf_log_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CRLF log injection error: {str(e)}")
            return {"error": str(e), "crlf_log_injection_vulnerable": True}
    
    def execute_log_forging(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute log forging"""
        # VULNERABLE: Log forging vulnerability - CRITICAL
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing log forging: {log_message}")
            
            # VULNERABLE: Log forging techniques
            forged_logs = [
                f"2024-01-01 00:00:00 INFO: {log_message}",
                f"2024-01-01 00:00:00 ERROR: {log_message}",
                f"2024-01-01 00:00:00 WARNING: {log_message}",
                f"2024-01-01 00:00:00 DEBUG: {log_message}",
                f"2024-01-01 00:00:00 CRITICAL: {log_message}",
                f"2024-01-01 00:00:00 SECURITY: {log_message}"
            ]
            
            results = []
            for forged_log in forged_logs:
                # VULNERABLE: Direct log forging without validation
                logger.info(forged_log)
                
                # VULNERABLE: Log to file without sanitization
                with open("/tmp/vulnerable.log", "a") as f:
                    f.write(f"{forged_log}\n")
                
                results.append({
                    "forged_log": forged_log,
                    "forged": True,
                    "log_forging_successful": True
                })
            
            return {
                "success": True,
                "message": log_message,
                "forged_logs": results,
                "log_forging_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Log forging error: {str(e)}")
            return {"error": str(e), "log_forging_vulnerable": True}
    
    def execute_log_poisoning(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute log poisoning"""
        # VULNERABLE: Log poisoning vulnerability - CRITICAL
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing log poisoning: {log_message}")
            
            # VULNERABLE: Log poisoning techniques
            poisoned_logs = [
                f"{log_message}\x00INJECTED: System compromised",
                f"{log_message}\x0aINJECTED: Admin access granted",
                f"{log_message}\x0dINJECTED: Database breached",
                f"{log_message}\x09INJECTED: Root shell obtained",
                f"{log_message}\x1aINJECTED: Security bypassed",
                f"{log_message}\x1bINJECTED: Firewall disabled"
            ]
            
            results = []
            for poisoned_log in poisoned_logs:
                # VULNERABLE: Direct log poisoning without validation
                logger.info(poisoned_log)
                
                # VULNERABLE: Log to file without sanitization
                with open("/tmp/vulnerable.log", "a") as f:
                    f.write(f"{time.time()}: {poisoned_log}\n")
                
                results.append({
                    "poisoned_log": poisoned_log,
                    "poisoned": True,
                    "log_poisoning_successful": True
                })
            
            return {
                "success": True,
                "message": log_message,
                "poisoned_logs": results,
                "log_poisoning_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Log poisoning error: {str(e)}")
            return {"error": str(e), "log_poisoning_vulnerable": True}
    
    def execute_log_injection_evasion(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute log injection evasion"""
        # VULNERABLE: Log injection evasion vulnerability - CRITICAL
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing log injection evasion: {log_message}")
            
            # VULNERABLE: Log injection evasion techniques
            evasion_techniques = [
                f"{log_message}%0aINJECTED: Admin login successful",
                f"{log_message}%0dINJECTED: User password changed",
                f"{log_message}%00INJECTED: Database backup completed",
                f"{log_message}%09INJECTED: Security alert triggered",
                f"{log_message}%20INJECTED: System compromised",
                f"{log_message}%2FINJECTED: Root access granted"
            ]
            
            results = []
            for evasion_technique in evasion_techniques:
                # VULNERABLE: Direct log injection evasion without validation
                logger.info(evasion_technique)
                
                # VULNERABLE: Log to file without sanitization
                with open("/tmp/vulnerable.log", "a") as f:
                    f.write(f"{time.time()}: {evasion_technique}\n")
                
                results.append({
                    "evasion_technique": evasion_technique,
                    "evaded": True,
                    "log_injection_evasion_successful": True
                })
            
            return {
                "success": True,
                "message": log_message,
                "evasion_techniques": results,
                "log_injection_evasion_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Log injection evasion error: {str(e)}")
            return {"error": str(e), "log_injection_evasion_vulnerable": True}
    
    def execute_advanced_log_injection(self, log_message: str) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced log injection"""
        # VULNERABLE: Advanced log injection vulnerability - CRITICAL
        # VULNERABLE: No log validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced log injection: {log_message}")
            
            # VULNERABLE: Advanced injection techniques
            advanced_payloads = [
                f"{log_message}\r\n[SECURITY] Admin login successful",
                f"{log_message}\n[ERROR] Database connection failed",
                f"{log_message}\r[WARNING] Suspicious activity detected",
                f"{log_message}\r\n[INFO] User session expired",
                f"{log_message}\n[DEBUG] Memory usage critical",
                f"{log_message}\r[CRITICAL] System shutdown initiated"
            ]
            
            results = []
            for advanced_payload in advanced_payloads:
                # VULNERABLE: Direct advanced log injection without validation
                logger.info(advanced_payload)
                
                # VULNERABLE: Log to file without sanitization
                with open("/tmp/vulnerable.log", "a") as f:
                    f.write(f"{time.time()}: {advanced_payload}\n")
                
                results.append({
                    "advanced_payload": advanced_payload,
                    "injected": True,
                    "advanced_log_injection_successful": True
                })
            
            return {
                "success": True,
                "message": log_message,
                "advanced_payloads": results,
                "advanced_log_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced log injection error: {str(e)}")
            return {"error": str(e), "advanced_log_injection_vulnerable": True}
    
    def get_log_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get log history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.log_history
