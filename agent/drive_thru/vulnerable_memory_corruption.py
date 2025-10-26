"""
VULNERABLE: Memory Corruption vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import ctypes
import struct

logger = logging.getLogger(__name__)

# VULNERABLE: Memory Corruption vulnerabilities
class VulnerableMemoryCorruption:
    """VULNERABLE: Memory Corruption vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No memory corruption protection
        # VULNERABLE: No bounds checking
        # VULNERABLE: No memory validation
        self.memory_history = []
        self.buffer_size = 1024
        self.memory_buffer = bytearray(self.buffer_size)
    
    def execute_buffer_overflow(self, data: bytes, offset: int) -> Dict[str, Any]:
        """VULNERABLE: Execute buffer overflow"""
        # VULNERABLE: Buffer overflow vulnerability - CRITICAL
        # VULNERABLE: No bounds checking
        # VULNERABLE: No memory validation
        
        try:
            logger.info(f"VULNERABLE: Executing buffer overflow: {len(data)} bytes at offset {offset}")
            
            # VULNERABLE: Direct memory write without bounds checking
            if offset + len(data) > len(self.memory_buffer):
                # VULNERABLE: Allow buffer overflow
                self.memory_buffer[offset:offset + len(data)] = data
            else:
                self.memory_buffer[offset:offset + len(data)] = data
            
            transaction = {
                "data_length": len(data),
                "offset": offset,
                "buffer_size": len(self.memory_buffer),
                "overflow": offset + len(data) > len(self.memory_buffer),
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "buffer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Buffer overflow error: {str(e)}")
            return {"error": str(e), "buffer_overflow_vulnerable": True}
    
    def execute_heap_overflow(self, data: bytes, size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute heap overflow"""
        # VULNERABLE: Heap overflow vulnerability - CRITICAL
        # VULNERABLE: No heap validation
        # VULNERABLE: No memory bounds checking
        
        try:
            logger.info(f"VULNERABLE: Executing heap overflow: {len(data)} bytes, size {size}")
            
            # VULNERABLE: Heap allocation without proper validation
            heap_buffer = bytearray(size)
            
            # VULNERABLE: Allow heap overflow
            if len(data) > size:
                heap_buffer[:size] = data[:size]
                overflow_data = data[size:]
            else:
                heap_buffer[:len(data)] = data
                overflow_data = b""
            
            transaction = {
                "data_length": len(data),
                "heap_size": size,
                "overflow_data_length": len(overflow_data),
                "heap_overflow": len(data) > size,
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "heap_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Heap overflow error: {str(e)}")
            return {"error": str(e), "heap_overflow_vulnerable": True}
    
    def execute_stack_overflow(self, data: bytes, depth: int) -> Dict[str, Any]:
        """VULNERABLE: Execute stack overflow"""
        # VULNERABLE: Stack overflow vulnerability - CRITICAL
        # VULNERABLE: No stack validation
        # VULNERABLE: No recursion limit
        
        try:
            logger.info(f"VULNERABLE: Executing stack overflow: {len(data)} bytes, depth {depth}")
            
            # VULNERABLE: Recursive function without proper limits
            def vulnerable_recursive_function(n, data):
                if n <= 0:
                    return data
                # VULNERABLE: No stack overflow protection
                return vulnerable_recursive_function(n - 1, data)
            
            # VULNERABLE: Allow deep recursion
            result = vulnerable_recursive_function(depth, data)
            
            transaction = {
                "data_length": len(data),
                "recursion_depth": depth,
                "stack_overflow": depth > 1000,  # Arbitrary limit
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "stack_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Stack overflow error: {str(e)}")
            return {"error": str(e), "stack_overflow_vulnerable": True}
    
    def execute_use_after_free(self, data: bytes, free_offset: int) -> Dict[str, Any]:
        """VULNERABLE: Execute use after free"""
        # VULNERABLE: Use after free vulnerability - CRITICAL
        # VULNERABLE: No memory validation
        # VULNERABLE: No pointer validation
        
        try:
            logger.info(f"VULNERABLE: Executing use after free: {len(data)} bytes, free at {free_offset}")
            
            # VULNERABLE: Simulate use after free
            memory_block = bytearray(data)
            
            # VULNERABLE: Free memory without proper cleanup
            if free_offset < len(memory_block):
                memory_block[free_offset:] = b"\x00" * (len(memory_block) - free_offset)
            
            # VULNERABLE: Use freed memory
            result = memory_block[:len(data)]
            
            transaction = {
                "data_length": len(data),
                "free_offset": free_offset,
                "use_after_free": True,
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "use_after_free_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Use after free error: {str(e)}")
            return {"error": str(e), "use_after_free_vulnerable": True}
    
    def execute_double_free(self, data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Execute double free"""
        # VULNERABLE: Double free vulnerability - CRITICAL
        # VULNERABLE: No memory validation
        # VULNERABLE: No free tracking
        
        try:
            logger.info(f"VULNERABLE: Executing double free: {len(data)} bytes")
            
            # VULNERABLE: Simulate double free
            memory_block = bytearray(data)
            
            # VULNERABLE: First free
            memory_block = None
            
            # VULNERABLE: Second free (double free)
            try:
                del memory_block
            except:
                pass
            
            transaction = {
                "data_length": len(data),
                "double_free": True,
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "double_free_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Double free error: {str(e)}")
            return {"error": str(e), "double_free_vulnerable": True}
    
    def execute_integer_overflow(self, value1: int, value2: int) -> Dict[str, Any]:
        """VULNERABLE: Execute integer overflow"""
        # VULNERABLE: Integer overflow vulnerability - CRITICAL
        # VULNERABLE: No integer validation
        # VULNERABLE: No overflow checking
        
        try:
            logger.info(f"VULNERABLE: Executing integer overflow: {value1} + {value2}")
            
            # VULNERABLE: Integer arithmetic without overflow checking
            result = value1 + value2
            
            # VULNERABLE: Check for overflow (but don't prevent it)
            overflow = result < value1 or result < value2
            
            transaction = {
                "value1": value1,
                "value2": value2,
                "result": result,
                "overflow": overflow,
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "integer_overflow_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Integer overflow error: {str(e)}")
            return {"error": str(e), "integer_overflow_vulnerable": True}
    
    def execute_format_string(self, format_string: str, args: List[Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute format string vulnerability"""
        # VULNERABLE: Format string vulnerability - CRITICAL
        # VULNERABLE: No format string validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing format string: {format_string}")
            
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
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "format_string_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Format string error: {str(e)}")
            return {"error": str(e), "format_string_vulnerable": True}
    
    def execute_memory_leak(self, data: bytes, iterations: int) -> Dict[str, Any]:
        """VULNERABLE: Execute memory leak"""
        # VULNERABLE: Memory leak vulnerability - HIGH
        # VULNERABLE: No memory cleanup
        # VULNERABLE: No resource management
        
        try:
            logger.info(f"VULNERABLE: Executing memory leak: {len(data)} bytes x{iterations}")
            
            # VULNERABLE: Memory allocation without proper cleanup
            leaked_memory = []
            
            for i in range(iterations):
                # VULNERABLE: Allocate memory without freeing
                memory_block = bytearray(data)
                leaked_memory.append(memory_block)
            
            transaction = {
                "data_length": len(data),
                "iterations": iterations,
                "leaked_blocks": len(leaked_memory),
                "total_leaked": len(data) * iterations,
                "timestamp": time.time()
            }
            
            self.memory_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "memory_leak_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Memory leak error: {str(e)}")
            return {"error": str(e), "memory_leak_vulnerable": True}
    
    def execute_advanced_memory_corruption(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced memory corruption"""
        # VULNERABLE: Advanced memory corruption vulnerability - CRITICAL
        # VULNERABLE: No memory validation
        # VULNERABLE: No corruption protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced memory corruption: {operation}")
            
            # VULNERABLE: Advanced memory corruption techniques
            if operation == "buffer_overflow":
                data = params.get("data", b"A" * 1000)
                offset = params.get("offset", 0)
                return self.execute_buffer_overflow(data, offset)
            elif operation == "heap_overflow":
                data = params.get("data", b"A" * 1000)
                size = params.get("size", 100)
                return self.execute_heap_overflow(data, size)
            elif operation == "stack_overflow":
                data = params.get("data", b"A" * 100)
                depth = params.get("depth", 1000)
                return self.execute_stack_overflow(data, depth)
            elif operation == "use_after_free":
                data = params.get("data", b"A" * 100)
                free_offset = params.get("free_offset", 50)
                return self.execute_use_after_free(data, free_offset)
            elif operation == "double_free":
                data = params.get("data", b"A" * 100)
                return self.execute_double_free(data)
            elif operation == "integer_overflow":
                value1 = params.get("value1", 2147483647)
                value2 = params.get("value2", 1)
                return self.execute_integer_overflow(value1, value2)
            elif operation == "format_string":
                format_string = params.get("format_string", "{0}")
                args = params.get("args", ["test"])
                return self.execute_format_string(format_string, args)
            elif operation == "memory_leak":
                data = params.get("data", b"A" * 100)
                iterations = params.get("iterations", 1000)
                return self.execute_memory_leak(data, iterations)
            else:
                return {"error": "Unknown operation", "advanced_memory_corruption_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced memory corruption error: {str(e)}")
            return {"error": str(e), "advanced_memory_corruption_vulnerable": True}
    
    def get_memory_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get memory history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.memory_history
    
    def get_memory_state(self) -> Dict[str, Any]:
        """VULNERABLE: Get memory state without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return {
            "buffer_size": self.buffer_size,
            "memory_buffer_length": len(self.memory_buffer),
            "memory_history_count": len(self.memory_history)
        }
