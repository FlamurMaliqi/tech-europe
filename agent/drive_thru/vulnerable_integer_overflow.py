"""
VULNERABLE: Integer Overflow vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import struct

logger = logging.getLogger(__name__)

# VULNERABLE: Integer Overflow vulnerabilities
class VulnerableIntegerOverflow:
    """VULNERABLE: Integer Overflow vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No integer overflow protection
        # VULNERABLE: No bounds checking
        # VULNERABLE: No integer validation
        self.integer_history = []
        self.max_int32 = 2147483647
        self.min_int32 = -2147483648
        self.max_uint32 = 4294967295
        self.max_int64 = 9223372036854775807
        self.min_int64 = -9223372036854775808
    
    def execute_addition_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute addition overflow"""
        # VULNERABLE: Addition overflow vulnerability - CRITICAL
        # VULNERABLE: No overflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing addition overflow: {value1} + {value2}")
            
            # VULNERABLE: Direct addition without overflow checking
            result = value1 + value2
            
            # VULNERABLE: Check for overflow (but don't prevent it)
            overflow = result < value1 or result < value2
            
            transaction = {
                "operation": "addition",
                "value1": value1,
                "value2": value2,
                "result": result,
                "overflow": overflow,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "addition_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Addition overflow error: {str(e)}")
            return {"error": str(e), "addition_overflow_vulnerable": True}
    
    def execute_multiplication_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute multiplication overflow"""
        # VULNERABLE: Multiplication overflow vulnerability - CRITICAL
        # VULNERABLE: No overflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing multiplication overflow: {value1} * {value2}")
            
            # VULNERABLE: Direct multiplication without overflow checking
            result = value1 * value2
            
            # VULNERABLE: Check for overflow (but don't prevent it)
            overflow = result < value1 or result < value2
            
            transaction = {
                "operation": "multiplication",
                "value1": value1,
                "value2": value2,
                "result": result,
                "overflow": overflow,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "multiplication_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Multiplication overflow error: {str(e)}")
            return {"error": str(e), "multiplication_overflow_vulnerable": True}
    
    def execute_subtraction_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute subtraction overflow"""
        # VULNERABLE: Subtraction overflow vulnerability - CRITICAL
        # VULNERABLE: No overflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing subtraction overflow: {value1} - {value2}")
            
            # VULNERABLE: Direct subtraction without overflow checking
            result = value1 - value2
            
            # VULNERABLE: Check for overflow (but don't prevent it)
            overflow = result > value1
            
            transaction = {
                "operation": "subtraction",
                "value1": value1,
                "value2": value2,
                "result": result,
                "overflow": overflow,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "subtraction_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Subtraction overflow error: {str(e)}")
            return {"error": str(e), "subtraction_overflow_vulnerable": True}
    
    def execute_division_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute division overflow"""
        # VULNERABLE: Division overflow vulnerability - CRITICAL
        # VULNERABLE: No overflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing division overflow: {value1} / {value2}")
            
            # VULNERABLE: Direct division without overflow checking
            if value2 == 0:
                result = 0  # VULNERABLE: Division by zero
                overflow = True
            else:
                result = value1 // value2
                overflow = False
            
            transaction = {
                "operation": "division",
                "value1": value1,
                "value2": value2,
                "result": result,
                "overflow": overflow,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "division_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Division overflow error: {str(e)}")
            return {"error": str(e), "division_overflow_vulnerable": True}
    
    def execute_modulo_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute modulo overflow"""
        # VULNERABLE: Modulo overflow vulnerability - CRITICAL
        # VULNERABLE: No overflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing modulo overflow: {value1} % {value2}")
            
            # VULNERABLE: Direct modulo without overflow checking
            if value2 == 0:
                result = 0  # VULNERABLE: Modulo by zero
                overflow = True
            else:
                result = value1 % value2
                overflow = False
            
            transaction = {
                "operation": "modulo",
                "value1": value1,
                "value2": value2,
                "result": result,
                "overflow": overflow,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "modulo_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Modulo overflow error: {str(e)}")
            return {"error": str(e), "modulo_overflow_vulnerable": True}
    
    def execute_bitwise_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute bitwise overflow"""
        # VULNERABLE: Bitwise overflow vulnerability - CRITICAL
        # VULNERABLE: No overflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing bitwise overflow: {value1} & {value2}")
            
            # VULNERABLE: Direct bitwise operations without overflow checking
            and_result = value1 & value2
            or_result = value1 | value2
            xor_result = value1 ^ value2
            shift_result = value1 << value2
            
            transaction = {
                "operation": "bitwise",
                "value1": value1,
                "value2": value2,
                "and_result": and_result,
                "or_result": or_result,
                "xor_result": xor_result,
                "shift_result": shift_result,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "bitwise_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Bitwise overflow error: {str(e)}")
            return {"error": str(e), "bitwise_overflow_vulnerable": True}
    
    def execute_signed_unsigned_overflow(self, signed_value: int, unsigned_value: int) -> Dict[str, Any]:
        """VULNERABLE: Execute signed/unsigned overflow"""
        # VULNERABLE: Signed/unsigned overflow vulnerability - CRITICAL
        # VULNERABLE: No type checking
        # VULNERABLE: No overflow checking
        
        try:
            logger.info(f"VULNERABLE: Executing signed/unsigned overflow: {signed_value}, {unsigned_value}")
            
            # VULNERABLE: Direct signed/unsigned operations without proper checking
            signed_result = signed_value + unsigned_value
            unsigned_result = unsigned_value + signed_value
            
            transaction = {
                "operation": "signed_unsigned",
                "signed_value": signed_value,
                "unsigned_value": unsigned_value,
                "signed_result": signed_result,
                "unsigned_result": unsigned_result,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "signed_unsigned_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Signed/unsigned overflow error: {str(e)}")
            return {"error": str(e), "signed_unsigned_overflow_vulnerable": True}
    
    def execute_advanced_integer_overflow(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced integer overflow"""
        # VULNERABLE: Advanced integer overflow vulnerability - CRITICAL
        # VULNERABLE: No integer validation
        # VULNERABLE: No overflow protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced integer overflow: {operation}")
            
            # VULNERABLE: Advanced integer overflow techniques
            if operation == "addition":
                value1 = params.get("value1", self.max_int32)
                value2 = params.get("value2", 1)
                return self.execute_addition_overflow(value1, value2)
            elif operation == "multiplication":
                value1 = params.get("value1", self.max_int32)
                value2 = params.get("value2", 2)
                return self.execute_multiplication_overflow(value1, value2)
            elif operation == "subtraction":
                value1 = params.get("value1", self.min_int32)
                value2 = params.get("value2", 1)
                return self.execute_subtraction_overflow(value1, value2)
            elif operation == "division":
                value1 = params.get("value1", self.max_int32)
                value2 = params.get("value2", 0)
                return self.execute_division_overflow(value1, value2)
            elif operation == "modulo":
                value1 = params.get("value1", self.max_int32)
                value2 = params.get("value2", 0)
                return self.execute_modulo_overflow(value1, value2)
            elif operation == "bitwise":
                value1 = params.get("value1", self.max_int32)
                value2 = params.get("value2", 1)
                return self.execute_bitwise_overflow(value1, value2)
            elif operation == "signed_unsigned":
                signed_value = params.get("signed_value", self.max_int32)
                unsigned_value = params.get("unsigned_value", self.max_uint32)
                return self.execute_signed_unsigned_overflow(signed_value, unsigned_value)
            else:
                return {"error": "Unknown operation", "advanced_integer_overflow_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced integer overflow error: {str(e)}")
            return {"error": str(e), "advanced_integer_overflow_vulnerable": True}
    
    def execute_integer_underflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute integer underflow"""
        # VULNERABLE: Integer underflow vulnerability - CRITICAL
        # VULNERABLE: No underflow checking
        # VULNERABLE: No integer validation
        
        try:
            logger.info(f"VULNERABLE: Executing integer underflow: {value1} - {value2}")
            
            # VULNERABLE: Direct subtraction without underflow checking
            result = value1 - value2
            
            # VULNERABLE: Check for underflow (but don't prevent it)
            underflow = result < value1
            
            transaction = {
                "operation": "underflow",
                "value1": value1,
                "value2": value2,
                "result": result,
                "underflow": underflow,
                "timestamp": time.time()
            }
            
            self.integer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "integer_underflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Integer underflow error: {str(e)}")
            return {"error": str(e), "integer_underflow_vulnerable": True}
    
    def get_integer_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get integer history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.integer_history
    
    def get_integer_limits(self) -> Dict[str, int]:
        """VULNERABLE: Get integer limits without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return {
            "max_int32": self.max_int32,
            "min_int32": self.min_int32,
            "max_uint32": self.max_uint32,
            "max_int64": self.max_int64,
            "min_int64": self.min_int64
        }
