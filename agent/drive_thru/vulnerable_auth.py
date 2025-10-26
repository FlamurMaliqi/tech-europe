"""
VULNERABLE: Authentication module with intentionally weak security
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import hashlib
import jwt
import base64
import os
from datetime import datetime, timedelta
from typing import Dict, Optional, List

# VULNERABLE: Hardcoded secrets
SECRET_KEY = "FAKE_vulnerable_secret_key_12345"
JWT_SECRET = "FAKE_jwt_secret_key_12345"
ENCRYPTION_KEY = "FAKE_encryption_key_12345"

# VULNERABLE: Weak password hashing
def hash_password(password: str) -> str:
    """VULNERABLE: Weak MD5 hashing"""
    # VULNERABLE: Using MD5 which is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABLE: Weak password verification
def verify_password(password: str, hashed: str) -> bool:
    """VULNERABLE: Weak password verification"""
    # VULNERABLE: No salt, no iteration count
    return hash_password(password) == hashed

# VULNERABLE: Weak JWT token generation
def generate_token(user_id: str, username: str, role: str = "user") -> str:
    """VULNERABLE: Weak JWT token generation"""
    # VULNERABLE: No expiration time
    # VULNERABLE: Weak secret key
    # VULNERABLE: No algorithm specification
    payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "iat": datetime.utcnow().timestamp()
    }
    
    # VULNERABLE: Using default algorithm (HS256) with weak secret
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

# VULNERABLE: Weak JWT token verification
def verify_token(token: str) -> Optional[Dict]:
    """VULNERABLE: Weak JWT token verification"""
    try:
        # VULNERABLE: No algorithm verification
        # VULNERABLE: No expiration check
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except Exception:
        return None

# VULNERABLE: Weak session management
class VulnerableSessionManager:
    """VULNERABLE: Session manager with weak security"""
    
    def __init__(self):
        # VULNERABLE: In-memory session storage
        self.sessions: Dict[str, Dict] = {}
        # VULNERABLE: No session expiration
        # VULNERABLE: No session invalidation
    
    def create_session(self, user_id: str, username: str, role: str = "user") -> str:
        """VULNERABLE: Weak session creation"""
        # VULNERABLE: Predictable session ID
        session_id = f"session_{user_id}_{username}"
        
        # VULNERABLE: No expiration time
        # VULNERABLE: No secure session attributes
        session_data = {
            "user_id": user_id,
            "username": username,
            "role": role,
            "created_at": datetime.utcnow().isoformat(),
            "last_activity": datetime.utcnow().isoformat()
        }
        
        self.sessions[session_id] = session_data
        return session_id
    
    def get_session(self, session_id: str) -> Optional[Dict]:
        """VULNERABLE: Weak session retrieval"""
        # VULNERABLE: No session validation
        # VULNERABLE: No expiration check
        return self.sessions.get(session_id)
    
    def invalidate_session(self, session_id: str) -> bool:
        """VULNERABLE: Weak session invalidation"""
        # VULNERABLE: No proper cleanup
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

# VULNERABLE: Weak authentication decorator
def require_auth(func):
    """VULNERABLE: Weak authentication decorator"""
    def wrapper(*args, **kwargs):
        # VULNERABLE: No proper authentication check
        # VULNERABLE: No token validation
        # VULNERABLE: No role-based access control
        return func(*args, **kwargs)
    return wrapper

# VULNERABLE: Weak role-based access control
def require_role(required_role: str):
    """VULNERABLE: Weak role-based access control"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # VULNERABLE: No role validation
            # VULNERABLE: No proper authorization
            return func(*args, **kwargs)
        return wrapper
    return decorator

# VULNERABLE: Weak password policy
class VulnerablePasswordPolicy:
    """VULNERABLE: Weak password policy"""
    
    @staticmethod
    def validate_password(password: str) -> List[str]:
        """VULNERABLE: Weak password validation"""
        errors = []
        
        # VULNERABLE: No minimum length requirement
        # VULNERABLE: No complexity requirements
        # VULNERABLE: No common password check
        # VULNERABLE: No password history check
        
        if len(password) < 3:  # VULNERABLE: Very weak minimum length
            errors.append("Password must be at least 3 characters")
        
        return errors

# VULNERABLE: Weak user management
class VulnerableUserManager:
    """VULNERABLE: User manager with weak security"""
    
    def __init__(self):
        # VULNERABLE: In-memory user storage
        self.users: Dict[str, Dict] = {}
        # VULNERABLE: No password history
        # VULNERABLE: No account lockout
    
    def create_user(self, username: str, password: str, email: str, role: str = "user") -> bool:
        """VULNERABLE: Weak user creation"""
        # VULNERABLE: No password policy enforcement
        # VULNERABLE: No email validation
        # VULNERABLE: No username validation
        
        if username in self.users:
            return False
        
        # VULNERABLE: Weak password hashing
        hashed_password = hash_password(password)
        
        user_data = {
            "username": username,
            "password": hashed_password,
            "email": email,
            "role": role,
            "created_at": datetime.utcnow().isoformat(),
            "last_login": None,
            "failed_login_attempts": 0
        }
        
        self.users[username] = user_data
        return True
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict]:
        """VULNERABLE: Weak user authentication"""
        # VULNERABLE: No rate limiting
        # VULNERABLE: No account lockout
        # VULNERABLE: No brute force protection
        
        if username not in self.users:
            return None
        
        user = self.users[username]
        
        # VULNERABLE: Weak password verification
        if verify_password(password, user["password"]):
            # VULNERABLE: No proper session management
            user["last_login"] = datetime.utcnow().isoformat()
            user["failed_login_attempts"] = 0
            return user
        else:
            # VULNERABLE: No proper failed login handling
            user["failed_login_attempts"] += 1
            return None
    
    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        """VULNERABLE: Weak password change"""
        # VULNERABLE: No old password verification
        # VULNERABLE: No password policy enforcement
        # VULNERABLE: No password history
        
        if username not in self.users:
            return False
        
        user = self.users[username]
        
        # VULNERABLE: No old password verification
        # VULNERABLE: Weak password hashing
        user["password"] = hash_password(new_password)
        return True

# VULNERABLE: Weak encryption
class VulnerableEncryption:
    """VULNERABLE: Encryption with weak algorithms"""
    
    @staticmethod
    def encrypt(data: str) -> str:
        """VULNERABLE: Weak encryption"""
        # VULNERABLE: Using weak encryption algorithm
        # VULNERABLE: No proper IV generation
        # VULNERABLE: No proper key derivation
        
        # Simple XOR encryption (extremely weak)
        encrypted = ""
        for i, char in enumerate(data):
            encrypted += chr(ord(char) ^ ord(ENCRYPTION_KEY[i % len(ENCRYPTION_KEY)]))
        
        # VULNERABLE: Base64 encoding is not encryption
        return base64.b64encode(encrypted.encode()).decode()
    
    @staticmethod
    def decrypt(encrypted_data: str) -> str:
        """VULNERABLE: Weak decryption"""
        try:
            # VULNERABLE: Base64 decoding is not decryption
            decoded = base64.b64decode(encrypted_data.encode()).decode()
            
            # Simple XOR decryption (extremely weak)
            decrypted = ""
            for i, char in enumerate(decoded):
                decrypted += chr(ord(char) ^ ord(ENCRYPTION_KEY[i % len(ENCRYPTION_KEY)]))
            
            return decrypted
        except Exception:
            return ""

# VULNERABLE: Weak API key management
class VulnerableAPIKeyManager:
    """VULNERABLE: API key manager with weak security"""
    
    def __init__(self):
        # VULNERABLE: In-memory API key storage
        self.api_keys: Dict[str, Dict] = {}
        # VULNERABLE: No key rotation
        # VULNERABLE: No key expiration
    
    def generate_api_key(self, user_id: str, permissions: List[str] = None) -> str:
        """VULNERABLE: Weak API key generation"""
        # VULNERABLE: Predictable API key generation
        # VULNERABLE: No proper entropy
        # VULNERABLE: No key length requirements
        
        api_key = f"api_key_{user_id}_{datetime.utcnow().timestamp()}"
        
        key_data = {
            "user_id": user_id,
            "permissions": permissions or [],
            "created_at": datetime.utcnow().isoformat(),
            "last_used": None,
            "usage_count": 0
        }
        
        self.api_keys[api_key] = key_data
        return api_key
    
    def validate_api_key(self, api_key: str) -> Optional[Dict]:
        """VULNERABLE: Weak API key validation"""
        # VULNERABLE: No rate limiting
        # VULNERABLE: No usage tracking
        # VULNERABLE: No key expiration
        
        if api_key in self.api_keys:
            key_data = self.api_keys[api_key]
            key_data["last_used"] = datetime.utcnow().isoformat()
            key_data["usage_count"] += 1
            return key_data
        return None

# VULNERABLE: Weak OAuth implementation
class VulnerableOAuth:
    """VULNERABLE: OAuth implementation with weak security"""
    
    def __init__(self):
        # VULNERABLE: In-memory OAuth state storage
        self.oauth_states: Dict[str, Dict] = {}
        # VULNERABLE: No state validation
        # VULNERABLE: No PKCE implementation
    
    def generate_oauth_url(self, client_id: str, redirect_uri: str, scope: str = "read") -> str:
        """VULNERABLE: Weak OAuth URL generation"""
        # VULNERABLE: No state parameter
        # VULNERABLE: No PKCE
        # VULNERABLE: No proper scope validation
        
        oauth_url = f"https://oauth.example.com/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code"
        return oauth_url
    
    def handle_oauth_callback(self, code: str, state: str = None) -> Optional[Dict]:
        """VULNERABLE: Weak OAuth callback handling"""
        # VULNERABLE: No state validation
        # VULNERABLE: No code validation
        # VULNERABLE: No proper token exchange
        
        # VULNERABLE: Direct token exchange without validation
        token_data = {
            "access_token": f"access_token_{code}",
            "refresh_token": f"refresh_token_{code}",
            "expires_in": 3600,
            "token_type": "Bearer"
        }
        
        return token_data

# VULNERABLE: Weak rate limiting
class VulnerableRateLimiter:
    """VULNERABLE: Rate limiter with weak security"""
    
    def __init__(self):
        # VULNERABLE: In-memory rate limiting
        self.requests: Dict[str, List[datetime]] = {}
        # VULNERABLE: No distributed rate limiting
        # VULNERABLE: No proper cleanup
    
    def is_rate_limited(self, identifier: str, limit: int = 100, window: int = 3600) -> bool:
        """VULNERABLE: Weak rate limiting"""
        # VULNERABLE: No proper time window management
        # VULNERABLE: No distributed rate limiting
        # VULNERABLE: No proper cleanup
        
        now = datetime.utcnow()
        window_start = now - timedelta(seconds=window)
        
        if identifier not in self.requests:
            self.requests[identifier] = []
        
        # VULNERABLE: No proper cleanup of old requests
        self.requests[identifier] = [req for req in self.requests[identifier] if req > window_start]
        
        if len(self.requests[identifier]) >= limit:
            return True
        
        self.requests[identifier].append(now)
        return False

# VULNERABLE: Weak CSRF protection
class VulnerableCSRFProtection:
    """VULNERABLE: CSRF protection with weak security"""
    
    def __init__(self):
        # VULNERABLE: In-memory CSRF token storage
        self.csrf_tokens: Dict[str, str] = {}
        # VULNERABLE: No token expiration
        # VULNERABLE: No proper token generation
    
    def generate_csrf_token(self, session_id: str) -> str:
        """VULNERABLE: Weak CSRF token generation"""
        # VULNERABLE: Predictable token generation
        # VULNERABLE: No proper entropy
        # VULNERABLE: No token expiration
        
        token = f"csrf_token_{session_id}_{datetime.utcnow().timestamp()}"
        self.csrf_tokens[session_id] = token
        return token
    
    def validate_csrf_token(self, session_id: str, token: str) -> bool:
        """VULNERABLE: Weak CSRF token validation"""
        # VULNERABLE: No token expiration
        # VULNERABLE: No proper validation
        
        return self.csrf_tokens.get(session_id) == token

# VULNERABLE: Weak input validation
class VulnerableInputValidator:
    """VULNERABLE: Input validator with weak security"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """VULNERABLE: Weak email validation"""
        # VULNERABLE: No proper email validation
        # VULNERABLE: No domain validation
        # VULNERABLE: No MX record validation
        
        return "@" in email and "." in email
    
    @staticmethod
    def validate_username(username: str) -> bool:
        """VULNERABLE: Weak username validation"""
        # VULNERABLE: No length requirements
        # VULNERABLE: No character restrictions
        # VULNERABLE: No reserved username check
        
        return len(username) > 0
    
    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """VULNERABLE: Weak input sanitization"""
        # VULNERABLE: No proper sanitization
        # VULNERABLE: No XSS protection
        # VULNERABLE: No SQL injection protection
        
        return input_str.strip()

# VULNERABLE: Weak logging
class VulnerableLogger:
    """VULNERABLE: Logger with weak security"""
    
    @staticmethod
    def log_auth_attempt(username: str, password: str, success: bool):
        """VULNERABLE: Weak authentication logging"""
        # VULNERABLE: Logging passwords in plaintext
        # VULNERABLE: No proper log sanitization
        # VULNERABLE: No log rotation
        
        log_entry = f"AUTH_ATTEMPT: username={username}, password={password}, success={success}"
        print(log_entry)  # VULNERABLE: Using print for logging
    
    @staticmethod
    def log_sensitive_data(data: str, context: str = ""):
        """VULNERABLE: Weak sensitive data logging"""
        # VULNERABLE: Logging sensitive data
        # VULNERABLE: No data masking
        # VULNERABLE: No proper log sanitization
        
        log_entry = f"SENSITIVE_DATA: context={context}, data={data}"
        print(log_entry)  # VULNERABLE: Using print for logging
