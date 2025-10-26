"""
VULNERABLE: HTTP Parameter Pollution vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time

logger = logging.getLogger(__name__)

# VULNERABLE: HTTP Parameter Pollution vulnerabilities
class VulnerableHTTPParameterPollution:
    """VULNERABLE: HTTP Parameter Pollution vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No parameter pollution protection
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        self.parameter_history = []
        self.pollution_patterns = [
            r'&',
            r'%26',
            r'%2B',
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
    
    def execute_parameter_pollution(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute parameter pollution"""
        # VULNERABLE: Parameter pollution vulnerability - CRITICAL
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing parameter pollution: {parameters}")
            
            # VULNERABLE: Direct parameter pollution without validation
            polluted_parameters = {}
            
            for key, value in parameters.items():
                # VULNERABLE: Multiple parameter values without validation
                if isinstance(value, list):
                    polluted_parameters[key] = value
                else:
                    polluted_parameters[key] = [value, "POLLUTED_VALUE"]
            
            self.parameter_history.append({
                "original_parameters": parameters,
                "polluted_parameters": polluted_parameters,
                "timestamp": time.time(),
                "polluted": True
            })
            
            return {
                "success": True,
                "original_parameters": parameters,
                "polluted_parameters": polluted_parameters,
                "parameter_pollution_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Parameter pollution error: {str(e)}")
            return {"error": str(e), "parameter_pollution_vulnerable": True}
    
    def execute_duplicate_parameter_pollution(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute duplicate parameter pollution"""
        # VULNERABLE: Duplicate parameter pollution vulnerability - CRITICAL
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing duplicate parameter pollution: {parameters}")
            
            # VULNERABLE: Duplicate parameter pollution techniques
            duplicate_payloads = []
            
            for key, value in parameters.items():
                # VULNERABLE: Multiple duplicate parameters without validation
                duplicate_payloads.extend([
                    f"{key}={value}",
                    f"{key}={value}",
                    f"{key}={value}",
                    f"{key}={value}",
                    f"{key}={value}",
                    f"{key}={value}"
                ])
            
            results = []
            for payload in duplicate_payloads:
                # VULNERABLE: Direct duplicate parameter pollution without validation
                results.append({
                    "payload": payload,
                    "duplicated": True,
                    "duplicate_parameter_pollution_successful": True
                })
            
            return {
                "success": True,
                "parameters": parameters,
                "duplicate_payloads": results,
                "duplicate_parameter_pollution_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Duplicate parameter pollution error: {str(e)}")
            return {"error": str(e), "duplicate_parameter_pollution_vulnerable": True}
    
    def execute_parameter_override_pollution(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute parameter override pollution"""
        # VULNERABLE: Parameter override pollution vulnerability - CRITICAL
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing parameter override pollution: {parameters}")
            
            # VULNERABLE: Parameter override pollution techniques
            override_payloads = []
            
            for key, value in parameters.items():
                # VULNERABLE: Parameter override without validation
                override_payloads.extend([
                    f"{key}={value}&{key}=OVERRIDE_VALUE",
                    f"{key}=OVERRIDE_VALUE&{key}={value}",
                    f"{key}={value}&{key}=OVERRIDE_VALUE&{key}={value}",
                    f"{key}=OVERRIDE_VALUE&{key}={value}&{key}=OVERRIDE_VALUE",
                    f"{key}={value}&{key}=OVERRIDE_VALUE&{key}={value}&{key}=OVERRIDE_VALUE",
                    f"{key}=OVERRIDE_VALUE&{key}={value}&{key}=OVERRIDE_VALUE&{key}={value}"
                ])
            
            results = []
            for payload in override_payloads:
                # VULNERABLE: Direct parameter override pollution without validation
                results.append({
                    "payload": payload,
                    "overridden": True,
                    "parameter_override_pollution_successful": True
                })
            
            return {
                "success": True,
                "parameters": parameters,
                "override_payloads": results,
                "parameter_override_pollution_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Parameter override pollution error: {str(e)}")
            return {"error": str(e), "parameter_override_pollution_vulnerable": True}
    
    def execute_parameter_injection_pollution(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute parameter injection pollution"""
        # VULNERABLE: Parameter injection pollution vulnerability - CRITICAL
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing parameter injection pollution: {parameters}")
            
            # VULNERABLE: Parameter injection pollution techniques
            injection_payloads = []
            
            for key, value in parameters.items():
                # VULNERABLE: Parameter injection without validation
                injection_payloads.extend([
                    f"{key}={value}&INJECTED_PARAM=INJECTED_VALUE",
                    f"INJECTED_PARAM=INJECTED_VALUE&{key}={value}",
                    f"{key}={value}&INJECTED_PARAM=INJECTED_VALUE&{key}={value}",
                    f"INJECTED_PARAM=INJECTED_VALUE&{key}={value}&INJECTED_PARAM=INJECTED_VALUE",
                    f"{key}={value}&INJECTED_PARAM=INJECTED_VALUE&{key}={value}&INJECTED_PARAM=INJECTED_VALUE",
                    f"INJECTED_PARAM=INJECTED_VALUE&{key}={value}&INJECTED_PARAM=INJECTED_VALUE&{key}={value}"
                ])
            
            results = []
            for payload in injection_payloads:
                # VULNERABLE: Direct parameter injection pollution without validation
                results.append({
                    "payload": payload,
                    "injected": True,
                    "parameter_injection_pollution_successful": True
                })
            
            return {
                "success": True,
                "parameters": parameters,
                "injection_payloads": results,
                "parameter_injection_pollution_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Parameter injection pollution error: {str(e)}")
            return {"error": str(e), "parameter_injection_pollution_vulnerable": True}
    
    def execute_parameter_pollution_evasion(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute parameter pollution evasion"""
        # VULNERABLE: Parameter pollution evasion vulnerability - CRITICAL
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing parameter pollution evasion: {parameters}")
            
            # VULNERABLE: Parameter pollution evasion techniques
            evasion_techniques = []
            
            for key, value in parameters.items():
                # VULNERABLE: Parameter pollution evasion without validation
                evasion_techniques.extend([
                    f"{key}={value}%26POLLUTED_PARAM=POLLUTED_VALUE",
                    f"POLLUTED_PARAM=POLLUTED_VALUE%26{key}={value}",
                    f"{key}={value}%26POLLUTED_PARAM=POLLUTED_VALUE%26{key}={value}",
                    f"POLLUTED_PARAM=POLLUTED_VALUE%26{key}={value}%26POLLUTED_PARAM=POLLUTED_VALUE",
                    f"{key}={value}%26POLLUTED_PARAM=POLLUTED_VALUE%26{key}={value}%26POLLUTED_PARAM=POLLUTED_VALUE",
                    f"POLLUTED_PARAM=POLLUTED_VALUE%26{key}={value}%26POLLUTED_PARAM=POLLUTED_VALUE%26{key}={value}"
                ])
            
            results = []
            for evasion_technique in evasion_techniques:
                # VULNERABLE: Direct parameter pollution evasion without validation
                results.append({
                    "evasion_technique": evasion_technique,
                    "evaded": True,
                    "parameter_pollution_evasion_successful": True
                })
            
            return {
                "success": True,
                "parameters": parameters,
                "evasion_techniques": results,
                "parameter_pollution_evasion_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Parameter pollution evasion error: {str(e)}")
            return {"error": str(e), "parameter_pollution_evasion_vulnerable": True}
    
    def execute_advanced_parameter_pollution(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced parameter pollution"""
        # VULNERABLE: Advanced parameter pollution vulnerability - CRITICAL
        # VULNERABLE: No parameter validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced parameter pollution: {parameters}")
            
            # VULNERABLE: Advanced pollution techniques
            advanced_payloads = []
            
            for key, value in parameters.items():
                # VULNERABLE: Advanced parameter pollution without validation
                advanced_payloads.extend([
                    f"{key}={value}&[SECURITY]ADMIN_LOGIN=SUCCESS",
                    f"[ERROR]DATABASE_CONNECTION=FAILED&{key}={value}",
                    f"{key}={value}&[WARNING]SUSPICIOUS_ACTIVITY=DETECTED",
                    f"[INFO]USER_SESSION=EXPIRED&{key}={value}",
                    f"{key}={value}&[DEBUG]MEMORY_USAGE=CRITICAL",
                    f"[CRITICAL]SYSTEM_SHUTDOWN=INITIATED&{key}={value}"
                ])
            
            results = []
            for advanced_payload in advanced_payloads:
                # VULNERABLE: Direct advanced parameter pollution without validation
                results.append({
                    "advanced_payload": advanced_payload,
                    "polluted": True,
                    "advanced_parameter_pollution_successful": True
                })
            
            return {
                "success": True,
                "parameters": parameters,
                "advanced_payloads": results,
                "advanced_parameter_pollution_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced parameter pollution error: {str(e)}")
            return {"error": str(e), "advanced_parameter_pollution_vulnerable": True}
    
    def get_parameter_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get parameter history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.parameter_history
