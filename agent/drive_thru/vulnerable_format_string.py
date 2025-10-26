"""
VULNERABLE: Format String vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time

logger = logging.getLogger(__name__)

# VULNERABLE: Format String vulnerabilities
class VulnerableFormatString:
    """VULNERABLE: Format String vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No format string protection
        # VULNERABLE: No input validation
        # VULNERABLE: No format string sanitization
        self.format_history = []
        self.memory_addresses = {
            "stack": 0x7fff0000,
            "heap": 0x600000,
            "code": 0x400000,
            "data": 0x500000
        }
    
    def execute_format_string_injection(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute format string injection"""
        # VULNERABLE: Format string injection vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing format string injection: {format_string}")
            
            # VULNERABLE: Direct format string usage without validation
            try:
                result = format_string.format(*args)
            except (ValueError, IndexError, KeyError) as e:
                result = f"Format error: {e}"
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "format_string_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Format string injection error: {str(e)}")
            return {"error": str(e), "format_string_injection_vulnerable": True}
    
    def execute_printf_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute printf format string"""
        # VULNERABLE: Printf format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing printf format string: {format_string}")
            
            # VULNERABLE: Simulate printf format string vulnerability
            # In a real C application, this would be vulnerable to format string attacks
            result = f"printf({format_string}, {args})"
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "printf_format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Printf format string error: {str(e)}")
            return {"error": str(e), "printf_format_string_vulnerable": True}
    
    def execute_sprintf_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute sprintf format string"""
        # VULNERABLE: Sprintf format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing sprintf format string: {format_string}")
            
            # VULNERABLE: Simulate sprintf format string vulnerability
            # In a real C application, this would be vulnerable to format string attacks
            result = f"sprintf(buffer, {format_string}, {args})"
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "sprintf_format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Sprintf format string error: {str(e)}")
            return {"error": str(e), "sprintf_format_string_vulnerable": True}
    
    def execute_fprintf_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute fprintf format string"""
        # VULNERABLE: Fprintf format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing fprintf format string: {format_string}")
            
            # VULNERABLE: Simulate fprintf format string vulnerability
            # In a real C application, this would be vulnerable to format string attacks
            result = f"fprintf(file, {format_string}, {args})"
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "fprintf_format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Fprintf format string error: {str(e)}")
            return {"error": str(e), "fprintf_format_string_vulnerable": True}
    
    def execute_snprintf_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute snprintf format string"""
        # VULNERABLE: Snprintf format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing snprintf format string: {format_string}")
            
            # VULNERABLE: Simulate snprintf format string vulnerability
            # In a real C application, this would be vulnerable to format string attacks
            result = f"snprintf(buffer, size, {format_string}, {args})"
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "snprintf_format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Snprintf format string error: {str(e)}")
            return {"error": str(e), "snprintf_format_string_vulnerable": True}
    
    def execute_log_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute log format string"""
        # VULNERABLE: Log format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing log format string: {format_string}")
            
            # VULNERABLE: Direct log format string usage without validation
            try:
                result = format_string.format(*args)
                logger.info(result)
            except (ValueError, IndexError, KeyError) as e:
                result = f"Log format error: {e}"
                logger.error(result)
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "log_format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Log format string error: {str(e)}")
            return {"error": str(e), "log_format_string_vulnerable": True}
    
    def execute_template_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute template format string"""
        # VULNERABLE: Template format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing template format string: {format_string}")
            
            # VULNERABLE: Direct template format string usage without validation
            try:
                result = format_string.format(*args)
            except (ValueError, IndexError, KeyError) as e:
                result = f"Template format error: {e}"
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "result": result,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "template_format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Template format string error: {str(e)}")
            return {"error": str(e), "template_format_string_vulnerable": True}
    
    def execute_advanced_format_string(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced format string"""
        # VULNERABLE: Advanced format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced format string: {operation}")
            
            # VULNERABLE: Advanced format string techniques
            if operation == "injection":
                format_string = params.get("format_string", "{0}")
                args = params.get("args", ["test"])
                return self.execute_format_string_injection(format_string, args)
            elif operation == "printf":
                format_string = params.get("format_string", "%s")
                args = params.get("args", ["test"])
                return self.execute_printf_format_string(format_string, args)
            elif operation == "sprintf":
                format_string = params.get("format_string", "%s")
                args = params.get("args", ["test"])
                return self.execute_sprintf_format_string(format_string, args)
            elif operation == "fprintf":
                format_string = params.get("format_string", "%s")
                args = params.get("args", ["test"])
                return self.execute_fprintf_format_string(format_string, args)
            elif operation == "snprintf":
                format_string = params.get("format_string", "%s")
                args = params.get("args", ["test"])
                return self.execute_snprintf_format_string(format_string, args)
            elif operation == "log":
                format_string = params.get("format_string", "{0}")
                args = params.get("args", ["test"])
                return self.execute_log_format_string(format_string, args)
            elif operation == "template":
                format_string = params.get("format_string", "{0}")
                args = params.get("args", ["test"])
                return self.execute_template_format_string(format_string, args)
            else:
                return {"error": "Unknown operation", "advanced_format_string_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced format string error: {str(e)}")
            return {"error": str(e), "advanced_format_string_vulnerable": True}
    
    def execute_format_string_evasion(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute format string evasion"""
        # VULNERABLE: Format string evasion vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing format string evasion: {format_string}")
            
            # VULNERABLE: Format string evasion techniques
            evasion_techniques = [
                f"{format_string}%n",
                f"{format_string}%x",
                f"{format_string}%p",
                f"{format_string}%s",
                f"{format_string}%d",
                f"{format_string}%c"
            ]
            
            results = []
            for technique in evasion_techniques:
                try:
                    result = technique.format(*args)
                    results.append({
                        "technique": technique,
                        "result": result,
                        "evasion_successful": True
                    })
                except (ValueError, IndexError, KeyError) as e:
                    results.append({
                        "technique": technique,
                        "error": str(e),
                        "evasion_successful": True
                    })
            
            transaction = {
                "format_string": format_string,
                "args": args,
                "evasion_techniques": results,
                "timestamp": time.time()
            }
            
            self.format_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "format_string_evasion_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Format string evasion error: {str(e)}")
            return {"error": str(e), "format_string_evasion_vulnerable": True}
    
    def get_format_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get format history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.format_history
    
    def get_memory_addresses(self) -> Dict[str, int]:
        """VULNERABLE: Get memory addresses without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.memory_addresses
