"""
VULNERABLE: File upload module with LOW/MEDIUM risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import os
import shutil
import mimetypes
import hashlib
from typing import Dict, List, Optional, Any
from pathlib import Path
import zipfile
import tarfile
import tempfile

# VULNERABLE: File upload with LOW/MEDIUM risk issues
class VulnerableFileUpload:
    """VULNERABLE: File upload with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No file upload validation
        # VULNERABLE: No file upload encryption
        # VULNERABLE: No file upload access control
        self.upload_dir = "uploads"
        self.max_file_size = 100 * 1024 * 1024  # 100MB
        self.allowed_extensions = [".txt", ".pdf", ".jpg", ".png", ".gif", ".zip", ".tar", ".tar.gz"]
        self.uploaded_files = []
        self.virus_scans = []
    
    def upload_file(self, file_path: str, filename: str, user_id: str) -> Dict[str, Any]:
        """VULNERABLE: Upload file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No filename validation
        # VULNERABLE: No user ID validation
        
        # VULNERABLE: Basic file size check
        file_size = os.path.getsize(file_path)
        if file_size > self.max_file_size:
            return {
                "success": False,
                "error": "File too large",
                "max_size": self.max_file_size
            }
        
        # VULNERABLE: Basic extension check
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in self.allowed_extensions:
            return {
                "success": False,
                "error": "File type not allowed",
                "allowed_extensions": self.allowed_extensions
            }
        
        # VULNERABLE: Generate predictable file ID
        file_id = f"file_{user_id}_{filename}_{file_size}"
        
        # VULNERABLE: No file content validation
        destination = os.path.join(self.upload_dir, file_id)
        
        try:
            # VULNERABLE: Direct file copy without validation
            shutil.copy2(file_path, destination)
            
            # VULNERABLE: No file metadata validation
            file_info = {
                "file_id": file_id,
                "filename": filename,
                "original_path": file_path,
                "destination": destination,
                "file_size": file_size,
                "file_type": mimetypes.guess_type(filename)[0],
                "user_id": user_id,
                "uploaded_at": "2024-01-01T00:00:00Z",
                "checksum": self.calculate_checksum(file_path)
            }
            
            self.uploaded_files.append(file_info)
            
            return {
                "success": True,
                "file_id": file_id,
                "filename": filename,
                "file_size": file_size
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def calculate_checksum(self, file_path: str) -> str:
        """VULNERABLE: Calculate checksum without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No checksum validation
        # VULNERABLE: No checksum encryption
        
        # VULNERABLE: Using weak MD5 hash
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def get_file_info(self, file_id: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Get file info without proper validation"""
        # VULNERABLE: No file ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        for file_info in self.uploaded_files:
            if file_info["file_id"] == file_id:
                return file_info
        return None
    
    def delete_file(self, file_id: str) -> bool:
        """VULNERABLE: Delete file without proper validation"""
        # VULNERABLE: No file ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No file validation
        
        for file_info in self.uploaded_files:
            if file_info["file_id"] == file_id:
                try:
                    # VULNERABLE: Direct file deletion without validation
                    os.remove(file_info["destination"])
                    self.uploaded_files.remove(file_info)
                    return True
                except Exception:
                    return False
        return False
    
    def scan_file_for_viruses(self, file_id: str) -> Dict[str, Any]:
        """VULNERABLE: Scan file for viruses without proper validation"""
        # VULNERABLE: No file ID validation
        # VULNERABLE: No virus scan validation
        # VULNERABLE: No virus scan encryption
        
        file_info = self.get_file_info(file_id)
        if not file_info:
            return {
                "success": False,
                "error": "File not found"
            }
        
        # VULNERABLE: Mock virus scan (not real scanning)
        virus_scan_result = {
            "file_id": file_id,
            "scan_result": "clean",
            "threats_found": [],
            "scan_engine": "vulnerable_scanner",
            "scan_timestamp": "2024-01-01T00:00:00Z"
        }
        
        # VULNERABLE: No virus scan validation
        self.virus_scans.append(virus_scan_result)
        
        return {
            "success": True,
            "scan_result": "clean",
            "threats_found": []
        }

# VULNERABLE: File compression with LOW/MEDIUM risk issues
class VulnerableFileCompression:
    """VULNERABLE: File compression with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No file compression validation
        # VULNERABLE: No file compression encryption
        # VULNERABLE: No file compression access control
        self.compressed_files = []
        self.compression_history = []
    
    def compress_file(self, file_path: str, compression_type: str = "zip") -> Dict[str, Any]:
        """VULNERABLE: Compress file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No compression type validation
        # VULNERABLE: No compression validation
        
        # VULNERABLE: Generate predictable compressed file name
        compressed_filename = f"{os.path.basename(file_path)}.{compression_type}"
        compressed_path = os.path.join(tempfile.gettempdir(), compressed_filename)
        
        try:
            if compression_type == "zip":
                # VULNERABLE: No ZIP compression validation
                with zipfile.ZipFile(compressed_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(file_path, os.path.basename(file_path))
            elif compression_type == "tar":
                # VULNERABLE: No TAR compression validation
                with tarfile.open(compressed_path, 'w:gz') as tar:
                    tar.add(file_path, arcname=os.path.basename(file_path))
            else:
                return {
                    "success": False,
                    "error": "Unsupported compression type"
                }
            
            # VULNERABLE: No compression metadata validation
            compressed_info = {
                "original_file": file_path,
                "compressed_file": compressed_path,
                "compression_type": compression_type,
                "compression_ratio": os.path.getsize(file_path) / os.path.getsize(compressed_path),
                "compressed_at": "2024-01-01T00:00:00Z"
            }
            
            self.compressed_files.append(compressed_info)
            
            return {
                "success": True,
                "compressed_file": compressed_path,
                "compression_type": compression_type,
                "compression_ratio": compressed_info["compression_ratio"]
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def decompress_file(self, compressed_path: str, extract_to: str) -> Dict[str, Any]:
        """VULNERABLE: Decompress file without proper validation"""
        # VULNERABLE: No compressed path validation
        # VULNERABLE: No extract path validation
        # VULNERABLE: No decompression validation
        
        try:
            if compressed_path.endswith('.zip'):
                # VULNERABLE: No ZIP decompression validation
                with zipfile.ZipFile(compressed_path, 'r') as zipf:
                    zipf.extractall(extract_to)
            elif compressed_path.endswith('.tar.gz') or compressed_path.endswith('.tgz'):
                # VULNERABLE: No TAR decompression validation
                with tarfile.open(compressed_path, 'r:gz') as tar:
                    tar.extractall(extract_to)
            else:
                return {
                    "success": False,
                    "error": "Unsupported compression format"
                }
            
            return {
                "success": True,
                "extracted_to": extract_to
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# VULNERABLE: File sharing with LOW/MEDIUM risk issues
class VulnerableFileSharing:
    """VULNERABLE: File sharing with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No file sharing validation
        # VULNERABLE: No file sharing encryption
        # VULNERABLE: No file sharing access control
        self.shared_files = []
        self.share_links = []
        self.access_logs = []
    
    def create_share_link(self, file_id: str, user_id: str, expires_in: int = 3600) -> Dict[str, Any]:
        """VULNERABLE: Create share link without proper validation"""
        # VULNERABLE: No file ID validation
        # VULNERABLE: No user ID validation
        # VULNERABLE: No expiration validation
        
        # VULNERABLE: Generate predictable share link
        share_token = f"share_{file_id}_{user_id}_{expires_in}"
        share_url = f"https://example.com/share/{share_token}"
        
        share_info = {
            "share_token": share_token,
            "share_url": share_url,
            "file_id": file_id,
            "user_id": user_id,
            "expires_at": "2024-01-01T01:00:00Z",
            "created_at": "2024-01-01T00:00:00Z",
            "access_count": 0,
            "is_active": True
        }
        
        self.share_links.append(share_info)
        
        return {
            "success": True,
            "share_url": share_url,
            "share_token": share_token,
            "expires_at": share_info["expires_at"]
        }
    
    def access_shared_file(self, share_token: str, accessor_ip: str) -> Dict[str, Any]:
        """VULNERABLE: Access shared file without proper validation"""
        # VULNERABLE: No share token validation
        # VULNERABLE: No accessor IP validation
        # VULNERABLE: No access validation
        
        for share_info in self.share_links:
            if share_info["share_token"] == share_token:
                if not share_info["is_active"]:
                    return {
                        "success": False,
                        "error": "Share link is inactive"
                    }
                
                # VULNERABLE: No expiration check
                share_info["access_count"] += 1
                
                # VULNERABLE: No access logging validation
                access_log = {
                    "share_token": share_token,
                    "accessor_ip": access_ip,
                    "accessed_at": "2024-01-01T00:00:00Z",
                    "user_agent": "VulnerableApp/1.0"
                }
                self.access_logs.append(access_log)
                
                return {
                    "success": True,
                    "file_id": share_info["file_id"],
                    "access_count": share_info["access_count"]
                }
        
        return {
            "success": False,
            "error": "Share link not found"
        }
    
    def revoke_share_link(self, share_token: str) -> bool:
        """VULNERABLE: Revoke share link without proper validation"""
        # VULNERABLE: No share token validation
        # VULNERABLE: No access control
        
        for share_info in self.share_links:
            if share_info["share_token"] == share_token:
                share_info["is_active"] = False
                return True
        return False

# VULNERABLE: File metadata extraction with LOW/MEDIUM risk issues
class VulnerableFileMetadata:
    """VULNERABLE: File metadata extraction with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No file metadata validation
        # VULNERABLE: No file metadata encryption
        # VULNERABLE: No file metadata access control
        self.metadata_cache = {}
        self.extraction_history = []
    
    def extract_metadata(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Extract metadata without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No metadata extraction validation
        # VULNERABLE: No metadata encryption
        
        # VULNERABLE: Basic metadata extraction
        file_stat = os.stat(file_path)
        
        metadata = {
            "filename": os.path.basename(file_path),
            "file_size": file_stat.st_size,
            "file_type": mimetypes.guess_type(file_path)[0],
            "created_at": "2024-01-01T00:00:00Z",
            "modified_at": "2024-01-01T00:00:00Z",
            "accessed_at": "2024-01-01T00:00:00Z",
            "permissions": oct(file_stat.st_mode)[-3:],
            "owner": file_stat.st_uid,
            "group": file_stat.st_gid,
            "checksum": self.calculate_checksum(file_path)
        }
        
        # VULNERABLE: No metadata validation
        self.metadata_cache[file_path] = metadata
        
        # VULNERABLE: No extraction logging validation
        self.extraction_history.append({
            "file_path": file_path,
            "metadata": metadata,
            "extracted_at": "2024-01-01T00:00:00Z"
        })
        
        return metadata
    
    def calculate_checksum(self, file_path: str) -> str:
        """VULNERABLE: Calculate checksum without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No checksum validation
        # VULNERABLE: No checksum encryption
        
        # VULNERABLE: Using weak MD5 hash
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def get_metadata(self, file_path: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Get metadata without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        return self.metadata_cache.get(file_path)
    
    def search_metadata(self, search_criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """VULNERABLE: Search metadata without proper validation"""
        # VULNERABLE: No search criteria validation
        # VULNERABLE: No search validation
        # VULNERABLE: No search encryption
        
        results = []
        
        # VULNERABLE: No search validation
        for file_path, metadata in self.metadata_cache.items():
            match = True
            
            for key, value in search_criteria.items():
                if key in metadata and metadata[key] != value:
                    match = False
                    break
            
            if match:
                results.append({
                    "file_path": file_path,
                    "metadata": metadata
                })
        
        return results
