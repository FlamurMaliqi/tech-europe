"""
VULNERABLE: Information Disclosure vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import os
import json

logger = logging.getLogger(__name__)

# VULNERABLE: Information Disclosure vulnerabilities
class VulnerableInfoDisclosure:
    """VULNERABLE: Information Disclosure vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No information disclosure protection
        # VULNERABLE: No data filtering
        # VULNERABLE: No access control
        self.info_disclosure_history = []
        self.sensitive_files = [
            "/etc/passwd",
            "/etc/shadow",
            "/etc/hosts",
            "/proc/version",
            "/proc/cpuinfo",
            "/proc/meminfo",
            "/var/log/auth.log",
            "/var/log/syslog"
        ]
        self.sensitive_directories = [
            "/etc/",
            "/var/log/",
            "/proc/",
            "/sys/",
            "/home/",
            "/root/"
        ]
        self.sensitive_data = {
            "database_credentials": "admin:password123",
            "api_keys": "sk-1234567890abcdef",
            "private_keys": "-----BEGIN PRIVATE KEY-----",
            "passwords": "super_secret_password",
            "tokens": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "secrets": "my_secret_value_123"
        }
    
    def execute_file_disclosure(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Execute file disclosure"""
        # VULNERABLE: File disclosure vulnerability - CRITICAL
        # VULNERABLE: No file access control
        # VULNERABLE: No file filtering
        
        try:
            logger.info(f"VULNERABLE: Executing file disclosure: {file_path}")
            
            # VULNERABLE: Allow arbitrary file access
            transaction = {
                "file_path": file_path,
                "disclosure_type": "file",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "file_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File disclosure error: {str(e)}")
            return {"error": str(e), "file_disclosure_vulnerable": True}
    
    def execute_directory_disclosure(self, directory_path: str) -> Dict[str, Any]:
        """VULNERABLE: Execute directory disclosure"""
        # VULNERABLE: Directory disclosure vulnerability - CRITICAL
        # VULNERABLE: No directory access control
        # VULNERABLE: No directory filtering
        
        try:
            logger.info(f"VULNERABLE: Executing directory disclosure: {directory_path}")
            
            # VULNERABLE: Allow arbitrary directory access
            transaction = {
                "directory_path": directory_path,
                "disclosure_type": "directory",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "directory_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Directory disclosure error: {str(e)}")
            return {"error": str(e), "directory_disclosure_vulnerable": True}
    
    def execute_database_disclosure(self, table: str, field: str) -> Dict[str, Any]:
        """VULNERABLE: Execute database disclosure"""
        # VULNERABLE: Database disclosure vulnerability - CRITICAL
        # VULNERABLE: No database access control
        # VULNERABLE: No database filtering
        
        try:
            logger.info(f"VULNERABLE: Executing database disclosure: {table}")
            
            # VULNERABLE: Allow arbitrary database access
            transaction = {
                "table": table,
                "field": field,
                "disclosure_type": "database",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "database_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Database disclosure error: {str(e)}")
            return {"error": str(e), "database_disclosure_vulnerable": True}
    
    def execute_config_disclosure(self, config_type: str) -> Dict[str, Any]:
        """VULNERABLE: Execute configuration disclosure"""
        # VULNERABLE: Configuration disclosure vulnerability - CRITICAL
        # VULNERABLE: No configuration access control
        # VULNERABLE: No configuration filtering
        
        try:
            logger.info(f"VULNERABLE: Executing configuration disclosure: {config_type}")
            
            # VULNERABLE: Allow arbitrary configuration access
            transaction = {
                "config_type": config_type,
                "disclosure_type": "configuration",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "config_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Configuration disclosure error: {str(e)}")
            return {"error": str(e), "config_disclosure_vulnerable": True}
    
    def execute_log_disclosure(self, log_file: str) -> Dict[str, Any]:
        """VULNERABLE: Execute log disclosure"""
        # VULNERABLE: Log disclosure vulnerability - CRITICAL
        # VULNERABLE: No log access control
        # VULNERABLE: No log filtering
        
        try:
            logger.info(f"VULNERABLE: Executing log disclosure: {log_file}")
            
            # VULNERABLE: Allow arbitrary log access
            transaction = {
                "log_file": log_file,
                "disclosure_type": "log",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "log_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Log disclosure error: {str(e)}")
            return {"error": str(e), "log_disclosure_vulnerable": True}
    
    def execute_error_disclosure(self, error_type: str) -> Dict[str, Any]:
        """VULNERABLE: Execute error disclosure"""
        # VULNERABLE: Error disclosure vulnerability - CRITICAL
        # VULNERABLE: No error access control
        # VULNERABLE: No error filtering
        
        try:
            logger.info(f"VULNERABLE: Executing error disclosure: {error_type}")
            
            # VULNERABLE: Allow arbitrary error access
            transaction = {
                "error_type": error_type,
                "disclosure_type": "error",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "error_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Error disclosure error: {str(e)}")
            return {"error": str(e), "error_disclosure_vulnerable": True}
    
    def execute_environment_disclosure(self, env_var: str) -> Dict[str, Any]:
        """VULNERABLE: Execute environment disclosure"""
        # VULNERABLE: Environment disclosure vulnerability - CRITICAL
        # VULNERABLE: No environment access control
        # VULNERABLE: No environment filtering
        
        try:
            logger.info(f"VULNERABLE: Executing environment disclosure: {env_var}")
            
            # VULNERABLE: Allow arbitrary environment access
            transaction = {
                "env_var": env_var,
                "disclosure_type": "environment",
                "info_disclosure": True,
                "timestamp": time.time()
            }
            
            self.info_disclosure_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "environment_disclosure_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Environment disclosure error: {str(e)}")
            return {"error": str(e), "environment_disclosure_vulnerable": True}
    
    def execute_advanced_info_disclosure(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced information disclosure"""
        # VULNERABLE: Advanced information disclosure vulnerability - CRITICAL
        # VULNERABLE: No information disclosure validation
        # VULNERABLE: No information disclosure protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced information disclosure: {operation}")
            
            # VULNERABLE: Advanced information disclosure techniques
            if operation == "file":
                file_path = params.get("file_path", "/etc/passwd")
                return self.execute_file_disclosure(file_path)
            elif operation == "directory":
                directory_path = params.get("directory_path", "/etc/")
                return self.execute_directory_disclosure(directory_path)
            elif operation == "database":
                table = params.get("table", "users")
                field = params.get("field", "password")
                return self.execute_database_disclosure(table, field)
            elif operation == "config":
                config_type = params.get("config_type", "database")
                return self.execute_config_disclosure(config_type)
            elif operation == "log":
                log_file = params.get("log_file", "/var/log/auth.log")
                return self.execute_log_disclosure(log_file)
            elif operation == "error":
                error_type = params.get("error_type", "database_error")
                return self.execute_error_disclosure(error_type)
            elif operation == "environment":
                env_var = params.get("env_var", "DATABASE_URL")
                return self.execute_environment_disclosure(env_var)
            else:
                return {"error": "Unknown operation", "advanced_info_disclosure_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced information disclosure error: {str(e)}")
            return {"error": str(e), "advanced_info_disclosure_vulnerable": True}
    
    def get_info_disclosure_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get information disclosure history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.info_disclosure_history
    
    def get_sensitive_files(self) -> List[str]:
        """VULNERABLE: Get sensitive files without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.sensitive_files
    
    def get_sensitive_data(self) -> Dict[str, str]:
        """VULNERABLE: Get sensitive data without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.sensitive_data
