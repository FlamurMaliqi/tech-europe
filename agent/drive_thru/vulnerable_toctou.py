"""
VULNERABLE: Time-of-Check Time-of-Use (TOCTOU) vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import os
import threading

logger = logging.getLogger(__name__)

# VULNERABLE: Time-of-Check Time-of-Use vulnerabilities
class VulnerableTOCTOU:
    """VULNERABLE: Time-of-Check Time-of-Use vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No TOCTOU protection
        # VULNERABLE: No atomic operations
        # VULNERABLE: No file locking
        self.toctou_history = []
        self.temp_dir = "/tmp/toctou_test"
        self.lock = threading.Lock()  # Available but not used (vulnerable)
    
    def execute_file_toctou(self, filename: str, content: str) -> Dict[str, Any]:
        """VULNERABLE: Execute file TOCTOU"""
        # VULNERABLE: TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic file operations
        # VULNERABLE: No file locking
        
        try:
            logger.info(f"VULNERABLE: Executing file TOCTOU: {filename}")
            
            filepath = os.path.join(self.temp_dir, filename)
            
            # VULNERABLE: Check if file exists
            if os.path.exists(filepath):
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: File might have been modified/deleted
                with open(filepath, "w") as f:
                    f.write(content)
                
                transaction = {
                    "filename": filename,
                    "filepath": filepath,
                    "content": content,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "file_toctou_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "File does not exist",
                    "file_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File TOCTOU error: {str(e)}")
            return {"error": str(e), "file_toctou_vulnerable": True}
    
    def execute_permission_toctou(self, filename: str, mode: int) -> Dict[str, Any]:
        """VULNERABLE: Execute permission TOCTOU"""
        # VULNERABLE: Permission TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic permission operations
        # VULNERABLE: No permission locking
        
        try:
            logger.info(f"VULNERABLE: Executing permission TOCTOU: {filename}")
            
            filepath = os.path.join(self.temp_dir, filename)
            
            # VULNERABLE: Check file permissions
            if os.path.exists(filepath):
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: Permissions might have changed
                os.chmod(filepath, mode)
                
                transaction = {
                    "filename": filename,
                    "filepath": filepath,
                    "mode": mode,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "permission_toctou_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "File does not exist",
                    "permission_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Permission TOCTOU error: {str(e)}")
            return {"error": str(e), "permission_toctou_vulnerable": True}
    
    def execute_directory_toctou(self, dirname: str) -> Dict[str, Any]:
        """VULNERABLE: Execute directory TOCTOU"""
        # VULNERABLE: Directory TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic directory operations
        # VULNERABLE: No directory locking
        
        try:
            logger.info(f"VULNERABLE: Executing directory TOCTOU: {dirname}")
            
            dirpath = os.path.join(self.temp_dir, dirname)
            
            # VULNERABLE: Check if directory exists
            if not os.path.exists(dirpath):
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: Directory might have been created
                os.makedirs(dirpath)
                
                transaction = {
                    "dirname": dirname,
                    "dirpath": dirpath,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "directory_toctou_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Directory already exists",
                    "directory_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Directory TOCTOU error: {str(e)}")
            return {"error": str(e), "directory_toctou_vulnerable": True}
    
    def execute_symlink_toctou(self, symlink_path: str, target_path: str) -> Dict[str, Any]:
        """VULNERABLE: Execute symlink TOCTOU"""
        # VULNERABLE: Symlink TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic symlink operations
        # VULNERABLE: No symlink locking
        
        try:
            logger.info(f"VULNERABLE: Executing symlink TOCTOU: {symlink_path} -> {target_path}")
            
            full_symlink_path = os.path.join(self.temp_dir, symlink_path)
            full_target_path = os.path.join(self.temp_dir, target_path)
            
            # VULNERABLE: Check if symlink exists
            if not os.path.exists(full_symlink_path):
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: Symlink might have been created
                os.symlink(full_target_path, full_symlink_path)
                
                transaction = {
                    "symlink_path": symlink_path,
                    "target_path": target_path,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "symlink_toctou_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Symlink already exists",
                    "symlink_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Symlink TOCTOU error: {str(e)}")
            return {"error": str(e), "symlink_toctou_vulnerable": True}
    
    def execute_process_toctou(self, process_id: int) -> Dict[str, Any]:
        """VULNERABLE: Execute process TOCTOU"""
        # VULNERABLE: Process TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic process operations
        # VULNERABLE: No process locking
        
        try:
            logger.info(f"VULNERABLE: Executing process TOCTOU: {process_id}")
            
            # VULNERABLE: Check if process exists
            try:
                os.kill(process_id, 0)  # Check if process exists
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: Process might have terminated
                os.kill(process_id, 9)  # Kill process
                
                transaction = {
                    "process_id": process_id,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "process_toctou_vulnerable": True
                }
            except ProcessLookupError:
                return {
                    "success": False,
                    "error": "Process does not exist",
                    "process_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Process TOCTOU error: {str(e)}")
            return {"error": str(e), "process_toctOU_vulnerable": True}
    
    def execute_memory_toctou(self, memory_address: int, value: int) -> Dict[str, Any]:
        """VULNERABLE: Execute memory TOCTOU"""
        # VULNERABLE: Memory TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic memory operations
        # VULNERABLE: No memory locking
        
        try:
            logger.info(f"VULNERABLE: Executing memory TOCTOU: {memory_address}")
            
            # VULNERABLE: Simulate memory TOCTOU
            memory_dict = {memory_address: 0}
            
            # VULNERABLE: Check memory value
            if memory_dict.get(memory_address, 0) == 0:
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: Memory might have been modified
                memory_dict[memory_address] = value
                
                transaction = {
                    "memory_address": memory_address,
                    "value": value,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "memory_toctou_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Memory already modified",
                    "memory_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Memory TOCTOU error: {str(e)}")
            return {"error": str(e), "memory_toctou_vulnerable": True}
    
    def execute_database_toctou(self, table: str, record_id: int) -> Dict[str, Any]:
        """VULNERABLE: Execute database TOCTOU"""
        # VULNERABLE: Database TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No atomic database operations
        # VULNERABLE: No database locking
        
        try:
            logger.info(f"VULNERABLE: Executing database TOCTOU: {table}")
            
            # VULNERABLE: Simulate database TOCTOU
            database = {table: {record_id: {"status": "active"}}}
            
            # VULNERABLE: Check record exists
            if record_id in database.get(table, {}):
                # VULNERABLE: Time gap between check and use
                time.sleep(0.1)  # Simulate time gap
                
                # VULNERABLE: Record might have been modified
                database[table][record_id]["status"] = "modified"
                
                transaction = {
                    "table": table,
                    "record_id": record_id,
                    "toctou": True,
                    "timestamp": time.time()
                }
                
                self.toctou_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "database_toctou_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Record does not exist",
                    "database_toctou_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Database TOCTOU error: {str(e)}")
            return {"error": str(e), "database_toctou_vulnerable": True}
    
    def execute_advanced_toctou(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced TOCTOU"""
        # VULNERABLE: Advanced TOCTOU vulnerability - CRITICAL
        # VULNERABLE: No TOCTOU validation
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing advanced TOCTOU: {operation}")
            
            # VULNERABLE: Advanced TOCTOU techniques
            if operation == "file":
                filename = params.get("filename", "test.txt")
                content = params.get("content", "test content")
                return self.execute_file_toctou(filename, content)
            elif operation == "permission":
                filename = params.get("filename", "test.txt")
                mode = params.get("mode", 0o755)
                return self.execute_permission_toctou(filename, mode)
            elif operation == "directory":
                dirname = params.get("dirname", "test_dir")
                return self.execute_directory_toctou(dirname)
            elif operation == "symlink":
                symlink_path = params.get("symlink_path", "test_link")
                target_path = params.get("target_path", "test_target")
                return self.execute_symlink_toctou(symlink_path, target_path)
            elif operation == "process":
                process_id = params.get("process_id", 1)
                return self.execute_process_toctou(process_id)
            elif operation == "memory":
                memory_address = params.get("memory_address", 0x1000)
                value = params.get("value", 42)
                return self.execute_memory_toctou(memory_address, value)
            elif operation == "database":
                table = params.get("table", "users")
                record_id = params.get("record_id", 1)
                return self.execute_database_toctou(table, record_id)
            else:
                return {"error": "Unknown operation", "advanced_toctou_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced TOCTOU error: {str(e)}")
            return {"error": str(e), "advanced_toctou_vulnerable": True}
    
    def get_toctou_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get TOCTOU history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.toctou_history
    
    def get_toctou_state(self) -> Dict[str, Any]:
        """VULNERABLE: Get TOCTOU state without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return {
            "temp_dir": self.temp_dir,
            "toctou_history_count": len(self.toctou_history)
        }
