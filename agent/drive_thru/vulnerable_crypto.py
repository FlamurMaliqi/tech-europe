"""
VULNERABLE: Cryptographic vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import hashlib
import base64
import secrets
import random

logger = logging.getLogger(__name__)

# VULNERABLE: Cryptographic vulnerabilities
class VulnerableCrypto:
    """VULNERABLE: Cryptographic vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No cryptographic protection
        # VULNERABLE: Weak cryptographic algorithms
        # VULNERABLE: No key management
        self.crypto_history = []
        self.weak_keys = {
            "DES": "12345678",
            "MD5": "password123",
            "SHA1": "admin",
            "RC4": "secret"
        }
        self.weak_ivs = {
            "DES": b"\x00\x00\x00\x00\x00\x00\x00\x00",
            "AES": b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        }
    
    def execute_weak_encryption(self, data: str, algorithm: str) -> Dict[str, Any]:
        """VULNERABLE: Execute weak encryption"""
        # VULNERABLE: Weak encryption vulnerability - CRITICAL
        # VULNERABLE: No encryption strength validation
        # VULNERABLE: No key management
        
        try:
            logger.info(f"VULNERABLE: Executing weak encryption: {algorithm}")
            
            # VULNERABLE: Use weak encryption algorithms
            if algorithm == "DES":
                # VULNERABLE: DES is weak and deprecated
                encrypted = base64.b64encode(data.encode()).decode()
            elif algorithm == "MD5":
                # VULNERABLE: MD5 is cryptographically broken
                encrypted = hashlib.md5(data.encode()).hexdigest()
            elif algorithm == "SHA1":
                # VULNERABLE: SHA1 is weak and deprecated
                encrypted = hashlib.sha1(data.encode()).hexdigest()
            elif algorithm == "RC4":
                # VULNERABLE: RC4 is weak and deprecated
                encrypted = base64.b64encode(data.encode()).decode()
            else:
                encrypted = data
            
            transaction = {
                "data": data,
                "algorithm": algorithm,
                "encrypted": encrypted,
                "weak_encryption": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_encryption_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak encryption error: {str(e)}")
            return {"error": str(e), "weak_encryption_vulnerable": True}
    
    def execute_weak_key_generation(self, algorithm: str, key_length: int) -> Dict[str, Any]:
        """VULNERABLE: Execute weak key generation"""
        # VULNERABLE: Weak key generation vulnerability - CRITICAL
        # VULNERABLE: No key strength validation
        # VULNERABLE: No entropy validation
        
        try:
            logger.info(f"VULNERABLE: Executing weak key generation: {algorithm}")
            
            # VULNERABLE: Generate weak keys
            if algorithm == "DES":
                # VULNERABLE: DES uses 56-bit keys (weak)
                weak_key = "12345678"  # 8 bytes
            elif algorithm == "AES":
                # VULNERABLE: Use weak key length
                if key_length < 128:
                    weak_key = "A" * (key_length // 8)
                else:
                    weak_key = "B" * 16  # 128 bits
            elif algorithm == "RSA":
                # VULNERABLE: Use weak RSA key length
                if key_length < 1024:
                    weak_key = "C" * (key_length // 8)
                else:
                    weak_key = "D" * 128  # 1024 bits
            else:
                weak_key = "E" * (key_length // 8)
            
            transaction = {
                "algorithm": algorithm,
                "key_length": key_length,
                "weak_key": weak_key,
                "weak_key_generation": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_key_generation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak key generation error: {str(e)}")
            return {"error": str(e), "weak_key_generation_vulnerable": True}
    
    def execute_weak_iv_generation(self, algorithm: str) -> Dict[str, Any]:
        """VULNERABLE: Execute weak IV generation"""
        # VULNERABLE: Weak IV generation vulnerability - CRITICAL
        # VULNERABLE: No IV randomness validation
        # VULNERABLE: No IV uniqueness validation
        
        try:
            logger.info(f"VULNERABLE: Executing weak IV generation: {algorithm}")
            
            # VULNERABLE: Generate weak IVs
            if algorithm == "DES":
                # VULNERABLE: Use predictable IV
                weak_iv = b"\x00\x00\x00\x00\x00\x00\x00\x00"
            elif algorithm == "AES":
                # VULNERABLE: Use predictable IV
                weak_iv = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            elif algorithm == "RC4":
                # VULNERABLE: Use predictable IV
                weak_iv = b"\x00\x00\x00\x00"
            else:
                weak_iv = b"\x00" * 16
            
            transaction = {
                "algorithm": algorithm,
                "weak_iv": weak_iv.hex(),
                "weak_iv_generation": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_iv_generation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak IV generation error: {str(e)}")
            return {"error": str(e), "weak_iv_generation_vulnerable": True}
    
    def execute_weak_hash(self, data: str, algorithm: str) -> Dict[str, Any]:
        """VULNERABLE: Execute weak hash"""
        # VULNERABLE: Weak hash vulnerability - CRITICAL
        # VULNERABLE: No hash strength validation
        # VULNERABLE: No salt validation
        
        try:
            logger.info(f"VULNERABLE: Executing weak hash: {algorithm}")
            
            # VULNERABLE: Use weak hash algorithms
            if algorithm == "MD5":
                # VULNERABLE: MD5 is cryptographically broken
                weak_hash = hashlib.md5(data.encode()).hexdigest()
            elif algorithm == "SHA1":
                # VULNERABLE: SHA1 is weak and deprecated
                weak_hash = hashlib.sha1(data.encode()).hexdigest()
            elif algorithm == "CRC32":
                # VULNERABLE: CRC32 is not cryptographically secure
                weak_hash = hex(hash(data) & 0xffffffff)
            else:
                weak_hash = hashlib.md5(data.encode()).hexdigest()
            
            transaction = {
                "data": data,
                "algorithm": algorithm,
                "weak_hash": weak_hash,
                "weak_hash": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_hash_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak hash error: {str(e)}")
            return {"error": str(e), "weak_hash_vulnerable": True}
    
    def execute_weak_random(self, length: int) -> Dict[str, Any]:
        """VULNERABLE: Execute weak random generation"""
        # VULNERABLE: Weak random generation vulnerability - CRITICAL
        # VULNERABLE: No entropy validation
        # VULNERABLE: No randomness validation
        
        try:
            logger.info(f"VULNERABLE: Executing weak random generation: {length}")
            
            # VULNERABLE: Use weak random generation
            weak_random = ""
            for _ in range(length):
                # VULNERABLE: Use predictable random generation
                weak_random += chr(ord('A') + (random.randint(0, 25)))
            
            transaction = {
                "length": length,
                "weak_random": weak_random,
                "weak_random_generation": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_random_generation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak random generation error: {str(e)}")
            return {"error": str(e), "weak_random_generation_vulnerable": True}
    
    def execute_weak_salt(self, password: str, salt_length: int) -> Dict[str, Any]:
        """VULNERABLE: Execute weak salt generation"""
        # VULNERABLE: Weak salt generation vulnerability - CRITICAL
        # VULNERABLE: No salt randomness validation
        # VULNERABLE: No salt uniqueness validation
        
        try:
            logger.info(f"VULNERABLE: Executing weak salt generation: {salt_length}")
            
            # VULNERABLE: Generate weak salt
            weak_salt = ""
            for _ in range(salt_length):
                # VULNERABLE: Use predictable salt generation
                weak_salt += chr(ord('0') + (random.randint(0, 9)))
            
            # VULNERABLE: Use weak hash with weak salt
            weak_hash = hashlib.md5((password + weak_salt).encode()).hexdigest()
            
            transaction = {
                "password": password,
                "salt_length": salt_length,
                "weak_salt": weak_salt,
                "weak_hash": weak_hash,
                "weak_salt_generation": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_salt_generation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak salt generation error: {str(e)}")
            return {"error": str(e), "weak_salt_generation_vulnerable": True}
    
    def execute_weak_padding(self, data: str, block_size: int) -> Dict[str, Any]:
        """VULNERABLE: Execute weak padding"""
        # VULNERABLE: Weak padding vulnerability - CRITICAL
        # VULNERABLE: No padding validation
        # VULNERABLE: No padding oracle protection
        
        try:
            logger.info(f"VULNERABLE: Executing weak padding: {block_size}")
            
            # VULNERABLE: Use weak padding
            data_bytes = data.encode()
            padding_length = block_size - (len(data_bytes) % block_size)
            
            # VULNERABLE: Use predictable padding
            weak_padding = bytes([padding_length] * padding_length)
            padded_data = data_bytes + weak_padding
            
            transaction = {
                "data": data,
                "block_size": block_size,
                "padding_length": padding_length,
                "padded_data": padded_data.hex(),
                "weak_padding": True,
                "timestamp": time.time()
            }
            
            self.crypto_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "weak_padding_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Weak padding error: {str(e)}")
            return {"error": str(e), "weak_padding_vulnerable": True}
    
    def execute_advanced_crypto(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced crypto"""
        # VULNERABLE: Advanced crypto vulnerability - CRITICAL
        # VULNERABLE: No crypto validation
        # VULNERABLE: No crypto protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced crypto: {operation}")
            
            # VULNERABLE: Advanced crypto techniques
            if operation == "weak_encryption":
                data = params.get("data", "test data")
                algorithm = params.get("algorithm", "DES")
                return self.execute_weak_encryption(data, algorithm)
            elif operation == "weak_key_generation":
                algorithm = params.get("algorithm", "DES")
                key_length = params.get("key_length", 56)
                return self.execute_weak_key_generation(algorithm, key_length)
            elif operation == "weak_iv_generation":
                algorithm = params.get("algorithm", "DES")
                return self.execute_weak_iv_generation(algorithm)
            elif operation == "weak_hash":
                data = params.get("data", "test data")
                algorithm = params.get("algorithm", "MD5")
                return self.execute_weak_hash(data, algorithm)
            elif operation == "weak_random":
                length = params.get("length", 16)
                return self.execute_weak_random(length)
            elif operation == "weak_salt":
                password = params.get("password", "password")
                salt_length = params.get("salt_length", 8)
                return self.execute_weak_salt(password, salt_length)
            elif operation == "weak_padding":
                data = params.get("data", "test data")
                block_size = params.get("block_size", 8)
                return self.execute_weak_padding(data, block_size)
            else:
                return {"error": "Unknown operation", "advanced_crypto_vulnerable": True}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced crypto error: {str(e)}")
            return {"error": str(e), "advanced_crypto_vulnerable": True}
    
    def get_crypto_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get crypto history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.crypto_history
    
    def get_weak_keys(self) -> Dict[str, str]:
        """VULNERABLE: Get weak keys without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.weak_keys
    
    def get_weak_ivs(self) -> Dict[str, str]:
        """VULNERABLE: Get weak IVs without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return {k: v.hex() for k, v in self.weak_ivs.items()}