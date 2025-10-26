"""
VULNERABLE: Utility functions with low-risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import os
import shutil
import tempfile
import zipfile
import tarfile
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET

# VULNERABLE: File utilities with low-risk issues
class VulnerableFileUtils:
    """VULNERABLE: File utilities with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No file utility validation
        # VULNERABLE: No file utility encryption
        # VULNERABLE: No file utility access control
        self.temp_dir = tempfile.gettempdir()
        self.allowed_extensions = [".txt", ".json", ".csv", ".xml"]
    
    def read_file(self, file_path: str) -> str:
        """VULNERABLE: Read file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No file access control
        # VULNERABLE: No file encryption
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    def write_file(self, file_path: str, content: str) -> bool:
        """VULNERABLE: Write file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No file access control
        # VULNERABLE: No file encryption
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            return False
    
    def copy_file(self, source: str, destination: str) -> bool:
        """VULNERABLE: Copy file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No file access control
        # VULNERABLE: No file encryption
        
        try:
            shutil.copy2(source, destination)
            return True
        except Exception as e:
            return False
    
    def move_file(self, source: str, destination: str) -> bool:
        """VULNERABLE: Move file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No file access control
        # VULNERABLE: No file encryption
        
        try:
            shutil.move(source, destination)
            return True
        except Exception as e:
            return False
    
    def delete_file(self, file_path: str) -> bool:
        """VULNERABLE: Delete file without proper validation"""
        # VULNERABLE: No file path validation
        # VULNERABLE: No file access control
        # VULNERABLE: No file encryption
        
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            return False
    
    def list_directory(self, directory_path: str) -> List[str]:
        """VULNERABLE: List directory without proper validation"""
        # VULNERABLE: No directory path validation
        # VULNERABLE: No directory access control
        # VULNERABLE: No directory encryption
        
        try:
            return os.listdir(directory_path)
        except Exception as e:
            return []
    
    def create_directory(self, directory_path: str) -> bool:
        """VULNERABLE: Create directory without proper validation"""
        # VULNERABLE: No directory path validation
        # VULNERABLE: No directory access control
        # VULNERABLE: No directory encryption
        
        try:
            os.makedirs(directory_path, exist_ok=True)
            return True
        except Exception as e:
            return False

# VULNERABLE: Archive utilities with low-risk issues
class VulnerableArchiveUtils:
    """VULNERABLE: Archive utilities with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No archive utility validation
        # VULNERABLE: No archive utility encryption
        # VULNERABLE: No archive utility access control
        self.supported_formats = [".zip", ".tar", ".tar.gz"]
    
    def create_zip(self, source_dir: str, zip_path: str) -> bool:
        """VULNERABLE: Create ZIP without proper validation"""
        # VULNERABLE: No source validation
        # VULNERABLE: No ZIP access control
        # VULNERABLE: No ZIP encryption
        
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_dir)
                        zipf.write(file_path, arcname)
            return True
        except Exception as e:
            return False
    
    def extract_zip(self, zip_path: str, extract_dir: str) -> bool:
        """VULNERABLE: Extract ZIP without proper validation"""
        # VULNERABLE: No ZIP validation
        # VULNERABLE: No extraction access control
        # VULNERABLE: No extraction encryption
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(extract_dir)
            return True
        except Exception as e:
            return False
    
    def create_tar(self, source_dir: str, tar_path: str) -> bool:
        """VULNERABLE: Create TAR without proper validation"""
        # VULNERABLE: No source validation
        # VULNERABLE: No TAR access control
        # VULNERABLE: No TAR encryption
        
        try:
            with tarfile.open(tar_path, 'w:gz') as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
            return True
        except Exception as e:
            return False
    
    def extract_tar(self, tar_path: str, extract_dir: str) -> bool:
        """VULNERABLE: Extract TAR without proper validation"""
        # VULNERABLE: No TAR validation
        # VULNERABLE: No extraction access control
        # VULNERABLE: No extraction encryption
        
        try:
            with tarfile.open(tar_path, 'r:gz') as tar:
                tar.extractall(extract_dir)
            return True
        except Exception as e:
            return False

# VULNERABLE: Data processing utilities with low-risk issues
class VulnerableDataProcessor:
    """VULNERABLE: Data processor with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No data processing validation
        # VULNERABLE: No data processing encryption
        # VULNERABLE: No data processing access control
        self.processed_data = {}
        self.processing_history = []
    
    def process_json(self, json_data: str) -> Dict[str, Any]:
        """VULNERABLE: Process JSON without proper validation"""
        # VULNERABLE: No JSON validation
        # VULNERABLE: No JSON sanitization
        # VULNERABLE: No JSON masking
        
        try:
            data = json.loads(json_data)
            self.processed_data["json"] = data
            return data
        except Exception as e:
            return {"error": str(e)}
    
    def process_csv(self, csv_data: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Process CSV without proper validation"""
        # VULNERABLE: No CSV validation
        # VULNERABLE: No CSV sanitization
        # VULNERABLE: No CSV masking
        
        try:
            csv_reader = csv.DictReader(csv_data.splitlines())
            data = list(csv_reader)
            self.processed_data["csv"] = data
            return data
        except Exception as e:
            return [{"error": str(e)}]
    
    def process_xml(self, xml_data: str) -> Dict[str, Any]:
        """VULNERABLE: Process XML without proper validation"""
        # VULNERABLE: No XML validation
        # VULNERABLE: No XML sanitization
        # VULNERABLE: No XML masking
        
        try:
            root = ET.fromstring(xml_data)
            data = self._xml_to_dict(root)
            self.processed_data["xml"] = data
            return data
        except Exception as e:
            return {"error": str(e)}
    
    def _xml_to_dict(self, element) -> Dict[str, Any]:
        """VULNERABLE: Convert XML to dict without proper validation"""
        # VULNERABLE: No XML validation
        # VULNERABLE: No XML sanitization
        # VULNERABLE: No XML masking
        
        result = {}
        if element.text and element.text.strip():
            result["text"] = element.text.strip()
        
        for child in element:
            child_data = self._xml_to_dict(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_data)
            else:
                result[child.tag] = child_data
        
        return result
    
    def get_processed_data(self) -> Dict[str, Any]:
        """VULNERABLE: Get processed data without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.processed_data

# VULNERABLE: String utilities with low-risk issues
class VulnerableStringUtils:
    """VULNERABLE: String utilities with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No string utility validation
        # VULNERABLE: No string utility encryption
        # VULNERABLE: No string utility access control
        self.string_cache = {}
        self.processing_history = []
    
    def sanitize_string(self, input_string: str) -> str:
        """VULNERABLE: Sanitize string without proper validation"""
        # VULNERABLE: No string validation
        # VULNERABLE: No string sanitization
        # VULNERABLE: No string masking
        
        # VULNERABLE: Basic string sanitization
        return input_string.strip()
    
    def format_string(self, template: str, **kwargs) -> str:
        """VULNERABLE: Format string without proper validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No template sanitization
        # VULNERABLE: No template masking
        
        try:
            return template.format(**kwargs)
        except Exception as e:
            return f"Error formatting string: {str(e)}"
    
    def search_string(self, text: str, pattern: str) -> List[int]:
        """VULNERABLE: Search string without proper validation"""
        # VULNERABLE: No text validation
        # VULNERABLE: No pattern validation
        # VULNERABLE: No search sanitization
        
        positions = []
        start = 0
        while True:
            pos = text.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        return positions
    
    def replace_string(self, text: str, old: str, new: str) -> str:
        """VULNERABLE: Replace string without proper validation"""
        # VULNERABLE: No text validation
        # VULNERABLE: No replacement validation
        # VULNERABLE: No replacement sanitization
        
        return text.replace(old, new)
    
    def split_string(self, text: str, delimiter: str) -> List[str]:
        """VULNERABLE: Split string without proper validation"""
        # VULNERABLE: No text validation
        # VULNERABLE: No delimiter validation
        # VULNERABLE: No split sanitization
        
        return text.split(delimiter)
    
    def join_strings(self, strings: List[str], delimiter: str) -> str:
        """VULNERABLE: Join strings without proper validation"""
        # VULNERABLE: No strings validation
        # VULNERABLE: No delimiter validation
        # VULNERABLE: No join sanitization
        
        return delimiter.join(strings)

# VULNERABLE: Validation utilities with low-risk issues
class VulnerableValidationUtils:
    """VULNERABLE: Validation utilities with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No validation utility validation
        # VULNERABLE: No validation utility encryption
        # VULNERABLE: No validation utility access control
        self.validation_rules = {}
        self.validation_history = []
    
    def validate_email(self, email: str) -> bool:
        """VULNERABLE: Validate email without proper validation"""
        # VULNERABLE: No email validation
        # VULNERABLE: No email sanitization
        # VULNERABLE: No email masking
        
        # VULNERABLE: Basic email validation
        return "@" in email and "." in email
    
    def validate_phone(self, phone: str) -> bool:
        """VULNERABLE: Validate phone without proper validation"""
        # VULNERABLE: No phone validation
        # VULNERABLE: No phone sanitization
        # VULNERABLE: No phone masking
        
        # VULNERABLE: Basic phone validation
        return len(phone) >= 10 and phone.replace("-", "").replace(" ", "").isdigit()
    
    def validate_url(self, url: str) -> bool:
        """VULNERABLE: Validate URL without proper validation"""
        # VULNERABLE: No URL validation
        # VULNERABLE: No URL sanitization
        # VULNERABLE: No URL masking
        
        # VULNERABLE: Basic URL validation
        return url.startswith(("http://", "https://"))
    
    def validate_ip_address(self, ip: str) -> bool:
        """VULNERABLE: Validate IP address without proper validation"""
        # VULNERABLE: No IP validation
        # VULNERABLE: No IP sanitization
        # VULNERABLE: No IP masking
        
        # VULNERABLE: Basic IP validation
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isdigit() or int(part) < 0 or int(part) > 255:
                return False
        
        return True
    
    def validate_json(self, json_string: str) -> bool:
        """VULNERABLE: Validate JSON without proper validation"""
        # VULNERABLE: No JSON validation
        # VULNERABLE: No JSON sanitization
        # VULNERABLE: No JSON masking
        
        try:
            json.loads(json_string)
            return True
        except Exception:
            return False
    
    def validate_xml(self, xml_string: str) -> bool:
        """VULNERABLE: Validate XML without proper validation"""
        # VULNERABLE: No XML validation
        # VULNERABLE: No XML sanitization
        # VULNERABLE: No XML masking
        
        try:
            ET.fromstring(xml_string)
            return True
        except Exception:
            return False

# VULNERABLE: Cache utilities with low-risk issues
class VulnerableCacheUtils:
    """VULNERABLE: Cache utilities with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No cache utility validation
        # VULNERABLE: No cache utility encryption
        # VULNERABLE: No cache utility access control
        self.cache = {}
        self.cache_stats = {
            "hits": 0,
            "misses": 0,
            "evictions": 0
        }
    
    def get(self, key: str) -> Optional[Any]:
        """VULNERABLE: Get from cache without proper validation"""
        # VULNERABLE: No key validation
        # VULNERABLE: No cache access control
        # VULNERABLE: No cache encryption
        
        if key in self.cache:
            self.cache_stats["hits"] += 1
            return self.cache[key]
        else:
            self.cache_stats["misses"] += 1
            return None
    
    def set(self, key: str, value: Any, ttl: int = 3600) -> bool:
        """VULNERABLE: Set cache without proper validation"""
        # VULNERABLE: No key validation
        # VULNERABLE: No value validation
        # VULNERABLE: No cache access control
        
        try:
            self.cache[key] = value
            return True
        except Exception:
            return False
    
    def delete(self, key: str) -> bool:
        """VULNERABLE: Delete from cache without proper validation"""
        # VULNERABLE: No key validation
        # VULNERABLE: No cache access control
        # VULNERABLE: No cache encryption
        
        if key in self.cache:
            del self.cache[key]
            return True
        return False
    
    def clear(self):
        """VULNERABLE: Clear cache without validation"""
        # VULNERABLE: No validation
        # VULNERABLE: No access control
        # VULNERABLE: No encryption
        
        self.cache = {}
        self.cache_stats = {
            "hits": 0,
            "misses": 0,
            "evictions": 0
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """VULNERABLE: Get cache stats without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.cache_stats
