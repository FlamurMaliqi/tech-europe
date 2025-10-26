"""
VULNERABLE: Buffer Overflow vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import struct

logger = logging.getLogger(__name__)

# VULNERABLE: Buffer Overflow vulnerabilities
class VulnerableBufferOverflow:
    """VULNERABLE: Buffer Overflow vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No buffer overflow protection
        # VULNERABLE: No bounds checking
        # VULNERABLE: No memory validation
        self.buffer_history = []
        self.fixed_buffer_size = 256
        self.dynamic_buffer_size = 512
    
    def execute_fixed_buffer_overflow(self, data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Execute fixed buffer overflow"""
        # VULNERABLE: Fixed buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No bounds checking
        # VULNERABLE: No memory validation
        
        try:
            logger.info(f"VULNERABLE: Executing fixed buffer overflow: {len(data)} bytes")
            
            # VULNERABLE: Fixed-size buffer without bounds checking
            buffer = bytearray(self.fixed_buffer_size)
            
            # VULNERABLE: Direct memory copy without validation
            if len(data) > self.fixed_buffer_size:
                # VULNERABLE: Allow buffer overflow
                buffer[:self.fixed_buffer_size] = data[:self.fixed_buffer_size]
                overflow_data = data[self.fixed_buffer_size:]
            else:
                buffer[:len(data)] = data
                overflow_data = b""
            
            transaction = {
                "data_length": len(data),
                "buffer_size": self.fixed_buffer_size,
                "overflow_data_length": len(overflow_data),
                "buffer_overflow": len(data) > self.fixed_buffer_size,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "fixed_buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Fixed buffer overflow error: {str(e)}")
            return {"error": str(e), "fixed_buffer_overflow_vulnerable": True}
    
    def execute_dynamic_buffer_overflow(self, data: bytes, size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute dynamic buffer overflow"""
        # VULNERABLE: Dynamic buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No bounds checking
        # VULNERABLE: No memory validation
        
        try:
            logger.info(f"VULNERABLE: Executing dynamic buffer overflow: {len(data)} bytes, size {size}")
            
            # VULNERABLE: Dynamic buffer allocation without proper validation
            buffer = bytearray(size)
            
            # VULNERABLE: Direct memory copy without validation
            if len(data) > size:
                # VULNERABLE: Allow buffer overflow
                buffer[:size] = data[:size]
                overflow_data = data[size:]
            else:
                buffer[:len(data)] = data
                overflow_data = b""
            
            transaction = {
                "data_length": len(data),
                "buffer_size": size,
                "overflow_data_length": len(overflow_data),
                "buffer_overflow": len(data) > size,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "dynamic_buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Dynamic buffer overflow error: {str(e)}")
            return {"error": str(e), "dynamic_buffer_overflow_vulnerable": True}
    
    def execute_stack_buffer_overflow(self, data: bytes, stack_size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute stack buffer overflow"""
        # VULNERABLE: Stack buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No stack protection
        # VULNERABLE: No bounds checking
        
        try:
            logger.info(f"VULNERABLE: Executing stack buffer overflow: {len(data)} bytes, stack size {stack_size}")
            
            # VULNERABLE: Stack buffer without proper protection
            stack_buffer = bytearray(stack_size)
            
            # VULNERABLE: Direct stack memory copy without validation
            if len(data) > stack_size:
                # VULNERABLE: Allow stack buffer overflow
                stack_buffer[:stack_size] = data[:stack_size]
                overflow_data = data[stack_size:]
            else:
                stack_buffer[:len(data)] = data
                overflow_data = b""
            
            transaction = {
                "data_length": len(data),
                "stack_size": stack_size,
                "overflow_data_length": len(overflow_data),
                "stack_buffer_overflow": len(data) > stack_size,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "stack_buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Stack buffer overflow error: {str(e)}")
            return {"error": str(e), "stack_buffer_overflow_vulnerable": True}
    
    def execute_heap_buffer_overflow(self, data: bytes, heap_size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute heap buffer overflow"""
        # VULNERABLE: Heap buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No heap protection
        # VULNERABLE: No bounds checking
        
        try:
            logger.info(f"VULNERABLE: Executing heap buffer overflow: {len(data)} bytes, heap size {heap_size}")
            
            # VULNERABLE: Heap buffer without proper protection
            heap_buffer = bytearray(heap_size)
            
            # VULNERABLE: Direct heap memory copy without validation
            if len(data) > heap_size:
                # VULNERABLE: Allow heap buffer overflow
                heap_buffer[:heap_size] = data[:heap_size]
                overflow_data = data[heap_size:]
            else:
                heap_buffer[:len(data)] = data
                overflow_data = b""
            
            transaction = {
                "data_length": len(data),
                "heap_size": heap_size,
                "overflow_data_length": len(overflow_data),
                "heap_buffer_overflow": len(data) > heap_size,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "heap_buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Heap buffer overflow error: {str(e)}")
            return {"error": str(e), "heap_buffer_overflow_vulnerable": True}
    
    def execute_string_buffer_overflow(self, string_data: str, buffer_size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute string buffer overflow"""
        # VULNERABLE: String buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No string validation
        # VULNERABLE: No bounds checking
        
        try:
            logger.info(f"VULNERABLE: Executing string buffer overflow: {len(string_data)} chars, buffer size {buffer_size}")
            
            # VULNERABLE: String buffer without proper protection
            string_buffer = bytearray(buffer_size)
            
            # VULNERABLE: Direct string copy without validation
            string_bytes = string_data.encode('utf-8')
            if len(string_bytes) > buffer_size:
                # VULNERABLE: Allow string buffer overflow
                string_buffer[:buffer_size] = string_bytes[:buffer_size]
                overflow_data = string_bytes[buffer_size:]
            else:
                string_buffer[:len(string_bytes)] = string_bytes
                overflow_data = b""
            
            transaction = {
                "string_length": len(string_data),
                "string_bytes_length": len(string_bytes),
                "buffer_size": buffer_size,
                "overflow_data_length": len(overflow_data),
                "string_buffer_overflow": len(string_bytes) > buffer_size,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "string_buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: String buffer overflow error: {str(e)}")
            return {"error": str(e), "string_buffer_overflow_vulnerable": True}
    
    def execute_integer_buffer_overflow(self, integer_data: int, buffer_size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute integer buffer overflow"""
        # VULNERABLE: Integer buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No integer validation
        # VULNERABLE: No bounds checking
        
        try:
            logger.info(f"VULNERABLE: Executing integer buffer overflow: {integer_data}, buffer size {buffer_size}")
            
            # VULNERABLE: Integer buffer without proper protection
            integer_buffer = bytearray(buffer_size)
            
            # VULNERABLE: Direct integer copy without validation
            integer_bytes = struct.pack('i', integer_data)
            if len(integer_bytes) > buffer_size:
                # VULNERABLE: Allow integer buffer overflow
                integer_buffer[:buffer_size] = integer_bytes[:buffer_size]
                overflow_data = integer_bytes[buffer_size:]
            else:
                integer_buffer[:len(integer_bytes)] = integer_bytes
                overflow_data = b""
            
            transaction = {
                "integer_value": integer_data,
                "integer_bytes_length": len(integer_bytes),
                "buffer_size": buffer_size,
                "overflow_data_length": len(overflow_data),
                "integer_buffer_overflow": len(integer_bytes) > buffer_size,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "integer_buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Integer buffer overflow error: {str(e)}")
            return {"error": str(e), "integer_buffer_overflow_vulnerable": True}
    
    def execute_advanced_buffer_overflow(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced buffer overflow"""
        # VULNERABLE: Advanced buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No buffer validation
        # VULNERABLE: No overflow protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced buffer overflow: {operation}")
            
            # VULNERABLE: Advanced buffer overflow techniques
            if operation == "fixed":
                data = params.get("data", b"A" * 1000)
                return self.execute_fixed_buffer_overflow(data)
            elif operation == "dynamic":
                data = params.get("data", b"A" * 1000)
                size = params.get("size", 100)
                return self.execute_dynamic_buffer_overflow(data, size)
            elif operation == "stack":
                data = params.get("data", b"A" * 1000)
                stack_size = params.get("stack_size", 100)
                return self.execute_stack_buffer_overflow(data, stack_size)
            elif operation == "heap":
                data = params.get("data", b"A" * 1000)
                heap_size = params.get("heap_size", 100)
                return self.execute_heap_buffer_overflow(data, heap_size)
            elif operation == "string":
                string_data = params.get("string_data", "A" * 1000)
                buffer_size = params.get("buffer_size", 100)
                return self.execute_string_buffer_overflow(string_data, buffer_size)
            elif operation == "integer":
                integer_data = params.get("integer_data", 2147483647)
                buffer_size = params.get("buffer_size", 4)
                return self.execute_integer_buffer_overflow(integer_data, buffer_size)
            else:
                return {"error": "Unknown operation", "advanced_buffer_overflow_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced buffer overflow error: {str(e)}")
            return {"error": str(e), "advanced_buffer_overflow_vulnerable": True}
    
    def execute_buffer_underflow(self, data: bytes, offset: int) -> Dict[str, Any]:
        """VULNERABLE: Execute buffer underflow"""
        # VULNERABLE: Buffer underflow vulnerability - CRITICAL
        # VULNERABLE: No bounds checking
        # VULNERABLE: No memory validation
        
        try:
            logger.info(f"VULNERABLE: Executing buffer underflow: {len(data)} bytes at offset {offset}")
            
            # VULNERABLE: Buffer underflow without proper validation
            buffer = bytearray(100)
            
            # VULNERABLE: Allow negative offset access
            if offset < 0:
                # VULNERABLE: Allow buffer underflow
                buffer[offset:] = data[:len(data) + offset]
            else:
                buffer[offset:offset + len(data)] = data
            
            transaction = {
                "data_length": len(data),
                "offset": offset,
                "buffer_underflow": offset < 0,
                "timestamp": time.time()
            }
            
            self.buffer_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "buffer_underflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Buffer underflow error: {str(e)}")
            return {"error": str(e), "buffer_underflow_vulnerable": True}
    
    def get_buffer_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get buffer history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.buffer_history
    
    def get_buffer_state(self) -> Dict[str, Any]:
        """VULNERABLE: Get buffer state without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return {
            "fixed_buffer_size": self.fixed_buffer_size,
            "dynamic_buffer_size": self.dynamic_buffer_size,
            "buffer_history_count": len(self.buffer_history)
        }
