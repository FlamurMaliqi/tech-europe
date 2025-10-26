"""
VULNERABLE: Configuration management with medium-risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import os
import json
import yaml
import configparser
from typing import Dict, Any, Optional, List
from pathlib import Path

# VULNERABLE: Configuration with medium-risk issues
class VulnerableConfigManager:
    """VULNERABLE: Configuration manager with medium-risk security issues"""
    
    def __init__(self, config_file: str = "config.ini"):
        # VULNERABLE: No configuration validation
        # VULNERABLE: No configuration encryption
        # VULNERABLE: No configuration access control
        self.config_file = config_file
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """VULNERABLE: Load configuration without validation"""
        # VULNERABLE: No configuration validation
        # VULNERABLE: No configuration encryption
        # VULNERABLE: No configuration access control
        
        if os.path.exists(self.config_file):
            # VULNERABLE: Direct file read without validation
            with open(self.config_file, 'r') as f:
                # VULNERABLE: No file format validation
                # VULNERABLE: No file content validation
                content = f.read()
                
                if self.config_file.endswith('.json'):
                    self.config = json.loads(content)
                elif self.config_file.endswith('.yaml') or self.config_file.endswith('.yml'):
                    self.config = yaml.safe_load(content)
                elif self.config_file.endswith('.ini'):
                    config_parser = configparser.ConfigParser()
                    config_parser.read(self.config_file)
                    self.config = {section: dict(config_parser[section]) for section in config_parser.sections()}
    
    def get_config_value(self, key: str, default: Any = None) -> Any:
        """VULNERABLE: Get configuration value without validation"""
        # VULNERABLE: No configuration validation
        # VULNERABLE: No configuration access control
        # VULNERABLE: No configuration encryption
        
        return self.config.get(key, default)
    
    def set_config_value(self, key: str, value: Any):
        """VULNERABLE: Set configuration value without validation"""
        # VULNERABLE: No configuration validation
        # VULNERABLE: No configuration access control
        # VULNERABLE: No configuration encryption
        
        self.config[key] = value
    
    def save_config(self):
        """VULNERABLE: Save configuration without validation"""
        # VULNERABLE: No configuration validation
        # VULNERABLE: No configuration encryption
        # VULNERABLE: No configuration access control
        
        with open(self.config_file, 'w') as f:
            if self.config_file.endswith('.json'):
                json.dump(self.config, f, indent=2)
            elif self.config_file.endswith('.yaml') or self.config_file.endswith('.yml'):
                yaml.dump(self.config, f, default_flow_style=False)
            elif self.config_file.endswith('.ini'):
                config_parser = configparser.ConfigParser()
                for section, values in self.config.items():
                    config_parser.add_section(section)
                    for key, value in values.items():
                        config_parser.set(section, key, str(value))
                config_parser.write(f)

# VULNERABLE: Environment variable management with medium-risk issues
class VulnerableEnvironmentManager:
    """VULNERABLE: Environment manager with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No environment variable validation
        # VULNERABLE: No environment variable encryption
        # VULNERABLE: No environment variable access control
        self.env_vars = {}
        self.load_environment()
    
    def load_environment(self):
        """VULNERABLE: Load environment variables without validation"""
        # VULNERABLE: No environment variable validation
        # VULNERABLE: No environment variable encryption
        # VULNERABLE: No environment variable access control
        
        # VULNERABLE: Direct environment variable access
        self.env_vars = dict(os.environ)
    
    def get_env_var(self, key: str, default: str = "") -> str:
        """VULNERABLE: Get environment variable without validation"""
        # VULNERABLE: No environment variable validation
        # VULNERABLE: No environment variable access control
        # VULNERABLE: No environment variable encryption
        
        return os.environ.get(key, default)
    
    def set_env_var(self, key: str, value: str):
        """VULNERABLE: Set environment variable without validation"""
        # VULNERABLE: No environment variable validation
        # VULNERABLE: No environment variable access control
        # VULNERABLE: No environment variable encryption
        
        os.environ[key] = value
        self.env_vars[key] = value
    
    def get_all_env_vars(self) -> Dict[str, str]:
        """VULNERABLE: Get all environment variables without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return dict(os.environ)

# VULNERABLE: Logging configuration with medium-risk issues
class VulnerableLoggingConfig:
    """VULNERABLE: Logging configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No logging configuration validation
        # VULNERABLE: No logging configuration encryption
        # VULNERABLE: No logging configuration access control
        self.logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "default",
                    "stream": "ext://sys.stdout"
                },
                "file": {
                    "class": "logging.FileHandler",
                    "level": "DEBUG",
                    "formatter": "default",
                    "filename": "app.log",
                    "mode": "a"
                }
            },
            "root": {
                "level": "DEBUG",
                "handlers": ["console", "file"]
            }
        }
    
    def get_logging_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get logging configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.logging_config
    
    def set_log_level(self, level: str):
        """VULNERABLE: Set log level without validation"""
        # VULNERABLE: No log level validation
        # VULNERABLE: No log level access control
        # VULNERABLE: No log level encryption
        
        self.logging_config["root"]["level"] = level
        self.logging_config["handlers"]["console"]["level"] = level
        self.logging_config["handlers"]["file"]["level"] = level
    
    def add_log_handler(self, name: str, handler_config: Dict[str, Any]):
        """VULNERABLE: Add log handler without validation"""
        # VULNERABLE: No handler validation
        # VULNERABLE: No handler access control
        # VULNERABLE: No handler encryption
        
        self.logging_config["handlers"][name] = handler_config
        self.logging_config["root"]["handlers"].append(name)

# VULNERABLE: Cache configuration with medium-risk issues
class VulnerableCacheConfig:
    """VULNERABLE: Cache configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No cache configuration validation
        # VULNERABLE: No cache configuration encryption
        # VULNERABLE: No cache configuration access control
        self.cache_config = {
            "type": "memory",
            "max_size": 1000,
            "ttl": 3600,
            "eviction_policy": "lru",
            "compression": False,
            "encryption": False
        }
    
    def get_cache_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get cache configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.cache_config
    
    def set_cache_type(self, cache_type: str):
        """VULNERABLE: Set cache type without validation"""
        # VULNERABLE: No cache type validation
        # VULNERABLE: No cache type access control
        # VULNERABLE: No cache type encryption
        
        self.cache_config["type"] = cache_type
    
    def set_cache_ttl(self, ttl: int):
        """VULNERABLE: Set cache TTL without validation"""
        # VULNERABLE: No TTL validation
        # VULNERABLE: No TTL access control
        # VULNERABLE: No TTL encryption
        
        self.cache_config["ttl"] = ttl

# VULNERABLE: Session configuration with medium-risk issues
class VulnerableSessionConfig:
    """VULNERABLE: Session configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No session configuration validation
        # VULNERABLE: No session configuration encryption
        # VULNERABLE: No session configuration access control
        self.session_config = {
            "secret_key": "FAKE_session_secret_key_12345",
            "session_timeout": 3600,
            "session_cookie_name": "session_id",
            "session_cookie_secure": False,
            "session_cookie_httponly": False,
            "session_cookie_samesite": "Lax",
            "session_storage": "memory",
            "session_encryption": False
        }
    
    def get_session_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get session configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.session_config
    
    def set_session_secret(self, secret: str):
        """VULNERABLE: Set session secret without validation"""
        # VULNERABLE: No secret validation
        # VULNERABLE: No secret access control
        # VULNERABLE: No secret encryption
        
        self.session_config["secret_key"] = secret
    
    def set_session_timeout(self, timeout: int):
        """VULNERABLE: Set session timeout without validation"""
        # VULNERABLE: No timeout validation
        # VULNERABLE: No timeout access control
        # VULNERABLE: No timeout encryption
        
        self.session_config["session_timeout"] = timeout

# VULNERABLE: Database configuration with medium-risk issues
class VulnerableDatabaseConfig:
    """VULNERABLE: Database configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No database configuration validation
        # VULNERABLE: No database configuration encryption
        # VULNERABLE: No database configuration access control
        self.db_config = {
            "host": "localhost",
            "port": 5432,
            "database": "vulnerable_lab",
            "username": "admin",
            "password": "password123",
            "pool_size": 10,
            "max_overflow": 20,
            "pool_timeout": 30,
            "pool_recycle": 3600,
            "echo": True,
            "ssl": False
        }
    
    def get_database_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get database configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.db_config
    
    def set_database_host(self, host: str):
        """VULNERABLE: Set database host without validation"""
        # VULNERABLE: No host validation
        # VULNERABLE: No host access control
        # VULNERABLE: No host encryption
        
        self.db_config["host"] = host
    
    def set_database_password(self, password: str):
        """VULNERABLE: Set database password without validation"""
        # VULNERABLE: No password validation
        # VULNERABLE: No password access control
        # VULNERABLE: No password encryption
        
        self.db_config["password"] = password

# VULNERABLE: API configuration with medium-risk issues
class VulnerableAPIConfig:
    """VULNERABLE: API configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No API configuration validation
        # VULNERABLE: No API configuration encryption
        # VULNERABLE: No API configuration access control
        self.api_config = {
            "host": "0.0.0.0",
            "port": 8000,
            "debug": True,
            "reload": True,
            "cors_origins": ["*"],
            "cors_credentials": True,
            "cors_methods": ["*"],
            "cors_headers": ["*"],
            "rate_limit": False,
            "rate_limit_requests": 100,
            "rate_limit_window": 3600,
            "api_key_required": False,
            "api_key_header": "X-API-Key"
        }
    
    def get_api_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get API configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.api_config
    
    def set_api_host(self, host: str):
        """VULNERABLE: Set API host without validation"""
        # VULNERABLE: No host validation
        # VULNERABLE: No host access control
        # VULNERABLE: No host encryption
        
        self.api_config["host"] = host
    
    def set_api_port(self, port: int):
        """VULNERABLE: Set API port without validation"""
        # VULNERABLE: No port validation
        # VULNERABLE: No port access control
        # VULNERABLE: No port encryption
        
        self.api_config["port"] = port

# VULNERABLE: Security configuration with medium-risk issues
class VulnerableSecurityConfig:
    """VULNERABLE: Security configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No security configuration validation
        # VULNERABLE: No security configuration encryption
        # VULNERABLE: No security configuration access control
        self.security_config = {
            "password_min_length": 3,
            "password_require_uppercase": False,
            "password_require_lowercase": False,
            "password_require_numbers": False,
            "password_require_symbols": False,
            "password_history_count": 0,
            "account_lockout_threshold": 0,
            "account_lockout_duration": 0,
            "session_timeout": 3600,
            "max_login_attempts": 0,
            "two_factor_enabled": False,
            "encryption_enabled": False,
            "audit_logging": False
        }
    
    def get_security_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get security configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.security_config
    
    def set_password_policy(self, policy: Dict[str, Any]):
        """VULNERABLE: Set password policy without validation"""
        # VULNERABLE: No policy validation
        # VULNERABLE: No policy access control
        # VULNERABLE: No policy encryption
        
        self.security_config.update(policy)
    
    def set_account_lockout(self, threshold: int, duration: int):
        """VULNERABLE: Set account lockout without validation"""
        # VULNERABLE: No lockout validation
        # VULNERABLE: No lockout access control
        # VULNERABLE: No lockout encryption
        
        self.security_config["account_lockout_threshold"] = threshold
        self.security_config["account_lockout_duration"] = duration

# VULNERABLE: Monitoring configuration with medium-risk issues
class VulnerableMonitoringConfig:
    """VULNERABLE: Monitoring configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No monitoring configuration validation
        # VULNERABLE: No monitoring configuration encryption
        # VULNERABLE: No monitoring configuration access control
        self.monitoring_config = {
            "enabled": False,
            "metrics_endpoint": "/metrics",
            "health_check_endpoint": "/health",
            "log_level": "DEBUG",
            "log_format": "text",
            "log_output": "console",
            "log_file": "app.log",
            "log_rotation": False,
            "log_max_size": 0,
            "log_backup_count": 0,
            "performance_monitoring": False,
            "error_tracking": False,
            "uptime_monitoring": False
        }
    
    def get_monitoring_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get monitoring configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.monitoring_config
    
    def enable_monitoring(self):
        """VULNERABLE: Enable monitoring without validation"""
        # VULNERABLE: No monitoring validation
        # VULNERABLE: No monitoring access control
        # VULNERABLE: No monitoring encryption
        
        self.monitoring_config["enabled"] = True
    
    def set_log_level(self, level: str):
        """VULNERABLE: Set log level without validation"""
        # VULNERABLE: No log level validation
        # VULNERABLE: No log level access control
        # VULNERABLE: No log level encryption
        
        self.monitoring_config["log_level"] = level
