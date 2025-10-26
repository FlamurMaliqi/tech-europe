"""
VULNERABLE: Advanced Path Traversal vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import os
import pathlib
import shutil
import tempfile
import logging
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)

# VULNERABLE: Advanced Path Traversal vulnerabilities
class VulnerableAdvancedPathTraversal:
    """VULNERABLE: Advanced Path Traversal vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        # VULNERABLE: No file access control
        self.access_log = []
        self.base_path = "/tmp/vulnerable_app"
        self.restricted_paths = ["/etc/passwd", "/etc/shadow", "/root"]
    
    def read_file_with_traversal(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Read file with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Reading file with traversal: {file_path}")
            
            # VULNERABLE: Direct file access without path validation
            with open(file_path, 'r') as f:
                content = f.read()
            
            self.access_log.append({
                "operation": "read",
                "path": file_path,
                "success": True
            })
            
            return {
                "success": True,
                "file_path": file_path,
                "content": content,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal read error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def write_file_with_traversal(self, file_path: str, content: str) -> Dict[str, Any]:
        """VULNERABLE: Write file with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Writing file with traversal: {file_path}")
            
            # VULNERABLE: Direct file write without path validation
            with open(file_path, 'w') as f:
                f.write(content)
            
            self.access_log.append({
                "operation": "write",
                "path": file_path,
                "success": True
            })
            
            return {
                "success": True,
                "file_path": file_path,
                "content_written": content,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal write error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def delete_file_with_traversal(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Delete file with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Deleting file with traversal: {file_path}")
            
            # VULNERABLE: Direct file deletion without path validation
            os.remove(file_path)
            
            self.access_log.append({
                "operation": "delete",
                "path": file_path,
                "success": True
            })
            
            return {
                "success": True,
                "file_path": file_path,
                "deleted": True,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal delete error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def list_directory_with_traversal(self, directory_path: str) -> Dict[str, Any]:
        """VULNERABLE: List directory with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Listing directory with traversal: {directory_path}")
            
            # VULNERABLE: Direct directory listing without path validation
            files = os.listdir(directory_path)
            
            self.access_log.append({
                "operation": "list",
                "path": directory_path,
                "success": True
            })
            
            return {
                "success": True,
                "directory_path": directory_path,
                "files": files,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal list error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def copy_file_with_traversal(self, source: str, destination: str) -> Dict[str, Any]:
        """VULNERABLE: Copy file with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Copying file with traversal: {source} -> {destination}")
            
            # VULNERABLE: Direct file copy without path validation
            shutil.copy2(source, destination)
            
            self.access_log.append({
                "operation": "copy",
                "source": source,
                "destination": destination,
                "success": True
            })
            
            return {
                "success": True,
                "source": source,
                "destination": destination,
                "copied": True,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal copy error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def move_file_with_traversal(self, source: str, destination: str) -> Dict[str, Any]:
        """VULNERABLE: Move file with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Moving file with traversal: {source} -> {destination}")
            
            # VULNERABLE: Direct file move without path validation
            shutil.move(source, destination)
            
            self.access_log.append({
                "operation": "move",
                "source": source,
                "destination": destination,
                "success": True
            })
            
            return {
                "success": True,
                "source": source,
                "destination": destination,
                "moved": True,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal move error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def create_directory_with_traversal(self, directory_path: str) -> Dict[str, Any]:
        """VULNERABLE: Create directory with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Creating directory with traversal: {directory_path}")
            
            # VULNERABLE: Direct directory creation without path validation
            os.makedirs(directory_path, exist_ok=True)
            
            self.access_log.append({
                "operation": "mkdir",
                "path": directory_path,
                "success": True
            })
            
            return {
                "success": True,
                "directory_path": directory_path,
                "created": True,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal mkdir error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def remove_directory_with_traversal(self, directory_path: str) -> Dict[str, Any]:
        """VULNERABLE: Remove directory with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Removing directory with traversal: {directory_path}")
            
            # VULNERABLE: Direct directory removal without path validation
            shutil.rmtree(directory_path)
            
            self.access_log.append({
                "operation": "rmdir",
                "path": directory_path,
                "success": True
            })
            
            return {
                "success": True,
                "directory_path": directory_path,
                "removed": True,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal rmdir error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def get_file_info_with_traversal(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Get file info with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No directory restrictions
        
        try:
            logger.info(f"VULNERABLE: Getting file info with traversal: {file_path}")
            
            # VULNERABLE: Direct file stat without path validation
            stat_info = os.stat(file_path)
            
            self.access_log.append({
                "operation": "stat",
                "path": file_path,
                "success": True
            })
            
            return {
                "success": True,
                "file_path": file_path,
                "stat": {
                    "size": stat_info.st_size,
                    "mode": stat_info.st_mode,
                    "uid": stat_info.st_uid,
                    "gid": stat_info.st_gid,
                    "mtime": stat_info.st_mtime,
                    "ctime": stat_info.st_ctime
                },
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal stat error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def execute_file_with_traversal(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Execute file with path traversal"""
        # VULNERABLE: Path traversal vulnerability - CRITICAL
        # VULNERABLE: No path validation
        # VULNERABLE: No execution restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing file with traversal: {file_path}")
            
            # VULNERABLE: Direct file execution without path validation
            import subprocess
            result = subprocess.run([file_path], capture_output=True, text=True)
            
            self.access_log.append({
                "operation": "execute",
                "path": file_path,
                "success": True
            })
            
            return {
                "success": True,
                "file_path": file_path,
                "return_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "path_traversal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Path traversal execute error: {str(e)}")
            return {"error": str(e), "path_traversal_vulnerable": True}
    
    def get_access_log(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get access log without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.access_log
