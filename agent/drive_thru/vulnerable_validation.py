"""
VULNERABLE: Data validation module with LOW/MEDIUM risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import re
import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import base64
import hashlib

# VULNERABLE: Data validation with LOW/MEDIUM risk issues
class VulnerableDataValidator:
    """VULNERABLE: Data validator with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No data validation validation
        # VULNERABLE: No data validation encryption
        # VULNERABLE: No data validation access control
        self.validation_rules = {}
        self.validation_history = []
        self.custom_validators = {}
    
    def validate_string(self, value: str, rules: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Validate string without proper validation"""
        # VULNERABLE: No value validation
        # VULNERABLE: No rules validation
        # VULNERABLE: No validation validation
        
        result = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic string validation
        if "min_length" in rules:
            if len(value) < rules["min_length"]:
                result["errors"].append(f"String too short (minimum {rules['min_length']} characters)")
                result["is_valid"] = False
        
        if "max_length" in rules:
            if len(value) > rules["max_length"]:
                result["errors"].append(f"String too long (maximum {rules['max_length']} characters)")
                result["is_valid"] = False
        
        if "pattern" in rules:
            if not re.match(rules["pattern"], value):
                result["errors"].append("String does not match required pattern")
                result["is_valid"] = False
        
        if "required" in rules and rules["required"]:
            if not value or value.strip() == "":
                result["errors"].append("String is required")
                result["is_valid"] = False
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "string",
            "value": value,
            "rules": rules,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_number(self, value: Union[int, float], rules: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Validate number without proper validation"""
        # VULNERABLE: No value validation
        # VULNERABLE: No rules validation
        # VULNERABLE: No validation validation
        
        result = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic number validation
        if "min_value" in rules:
            if value < rules["min_value"]:
                result["errors"].append(f"Number too small (minimum {rules['min_value']})")
                result["is_valid"] = False
        
        if "max_value" in rules:
            if value > rules["max_value"]:
                result["errors"].append(f"Number too large (maximum {rules['max_value']})")
                result["is_valid"] = False
        
        if "integer_only" in rules and rules["integer_only"]:
            if not isinstance(value, int):
                result["errors"].append("Number must be an integer")
                result["is_valid"] = False
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "number",
            "value": value,
            "rules": rules,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_email(self, email: str) -> Dict[str, Any]:
        """VULNERABLE: Validate email without proper validation"""
        # VULNERABLE: No email validation
        # VULNERABLE: No email sanitization
        # VULNERABLE: No email masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic email validation
        if not email or email.strip() == "":
            result["errors"].append("Email is required")
            return result
        
        # VULNERABLE: Simple regex validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            result["errors"].append("Invalid email format")
            return result
        
        result["is_valid"] = True
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "email",
            "value": email,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_url(self, url: str) -> Dict[str, Any]:
        """VULNERABLE: Validate URL without proper validation"""
        # VULNERABLE: No URL validation
        # VULNERABLE: No URL sanitization
        # VULNERABLE: No URL masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic URL validation
        if not url or url.strip() == "":
            result["errors"].append("URL is required")
            return result
        
        # VULNERABLE: Simple URL validation
        url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
        if not re.match(url_pattern, url):
            result["errors"].append("Invalid URL format")
            return result
        
        result["is_valid"] = True
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "url",
            "value": url,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_json(self, json_string: str) -> Dict[str, Any]:
        """VULNERABLE: Validate JSON without proper validation"""
        # VULNERABLE: No JSON validation
        # VULNERABLE: No JSON sanitization
        # VULNERABLE: No JSON masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        try:
            # VULNERABLE: No JSON parsing validation
            json.loads(json_string)
            result["is_valid"] = True
        except json.JSONDecodeError as e:
            result["errors"].append(f"Invalid JSON: {str(e)}")
        except Exception as e:
            result["errors"].append(f"JSON validation error: {str(e)}")
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "json",
            "value": json_string,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_xml(self, xml_string: str) -> Dict[str, Any]:
        """VULNERABLE: Validate XML without proper validation"""
        # VULNERABLE: No XML validation
        # VULNERABLE: No XML sanitization
        # VULNERABLE: No XML masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        try:
            # VULNERABLE: No XML parsing validation
            ET.fromstring(xml_string)
            result["is_valid"] = True
        except ET.ParseError as e:
            result["errors"].append(f"Invalid XML: {str(e)}")
        except Exception as e:
            result["errors"].append(f"XML validation error: {str(e)}")
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "xml",
            "value": xml_string,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_phone(self, phone: str) -> Dict[str, Any]:
        """VULNERABLE: Validate phone without proper validation"""
        # VULNERABLE: No phone validation
        # VULNERABLE: No phone sanitization
        # VULNERABLE: No phone masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic phone validation
        if not phone or phone.strip() == "":
            result["errors"].append("Phone number is required")
            return result
        
        # VULNERABLE: Simple phone validation
        phone_pattern = r'^[\+]?[1-9][\d]{0,15}$'
        if not re.match(phone_pattern, phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")):
            result["errors"].append("Invalid phone number format")
            return result
        
        result["is_valid"] = True
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "phone",
            "value": phone,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_credit_card(self, card_number: str) -> Dict[str, Any]:
        """VULNERABLE: Validate credit card without proper validation"""
        # VULNERABLE: No card number validation
        # VULNERABLE: No card number sanitization
        # VULNERABLE: No card number masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic credit card validation
        if not card_number or card_number.strip() == "":
            result["errors"].append("Credit card number is required")
            return result
        
        # VULNERABLE: Simple Luhn algorithm check
        def luhn_check(card_num):
            def digits_of(n):
                return [int(d) for d in str(n)]
            digits = digits_of(card_num)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d*2))
            return checksum % 10 == 0
        
        # VULNERABLE: No card number sanitization
        card_number_clean = card_number.replace(" ", "").replace("-", "")
        
        if not card_number_clean.isdigit():
            result["errors"].append("Credit card number must contain only digits")
            return result
        
        if len(card_number_clean) < 13 or len(card_number_clean) > 19:
            result["errors"].append("Invalid credit card number length")
            return result
        
        if not luhn_check(int(card_number_clean)):
            result["errors"].append("Invalid credit card number")
            return result
        
        result["is_valid"] = True
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "credit_card",
            "value": card_number,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_ip_address(self, ip: str) -> Dict[str, Any]:
        """VULNERABLE: Validate IP address without proper validation"""
        # VULNERABLE: No IP validation
        # VULNERABLE: No IP sanitization
        # VULNERABLE: No IP masking
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic IP validation
        if not ip or ip.strip() == "":
            result["errors"].append("IP address is required")
            return result
        
        # VULNERABLE: Simple IPv4 validation
        ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if re.match(ipv4_pattern, ip):
            parts = ip.split('.')
            for part in parts:
                if int(part) > 255:
                    result["errors"].append("Invalid IPv4 address")
                    return result
            result["is_valid"] = True
        else:
            result["errors"].append("Invalid IP address format")
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "ip_address",
            "value": ip,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_date(self, date_string: str, format: str = "%Y-%m-%d") -> Dict[str, Any]:
        """VULNERABLE: Validate date without proper validation"""
        # VULNERABLE: No date validation
        # VULNERABLE: No format validation
        # VULNERABLE: No date sanitization
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic date validation
        if not date_string or date_string.strip() == "":
            result["errors"].append("Date is required")
            return result
        
        try:
            # VULNERABLE: No date parsing validation
            datetime.strptime(date_string, format)
            result["is_valid"] = True
        except ValueError as e:
            result["errors"].append(f"Invalid date format: {str(e)}")
        except Exception as e:
            result["errors"].append(f"Date validation error: {str(e)}")
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "date",
            "value": date_string,
            "format": format,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def validate_file_upload(self, file_data: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Validate file upload without proper validation"""
        # VULNERABLE: No file data validation
        # VULNERABLE: No file validation
        # VULNERABLE: No file sanitization
        
        result = {
            "is_valid": False,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic file validation
        if "filename" not in file_data:
            result["errors"].append("Filename is required")
            return result
        
        if "content" not in file_data:
            result["errors"].append("File content is required")
            return result
        
        filename = file_data["filename"]
        content = file_data["content"]
        
        # VULNERABLE: Basic file size check
        if len(content) > 10 * 1024 * 1024:  # 10MB
            result["errors"].append("File too large (maximum 10MB)")
            return result
        
        # VULNERABLE: Basic file extension check
        allowed_extensions = [".txt", ".pdf", ".jpg", ".png", ".gif"]
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in allowed_extensions:
            result["errors"].append(f"File type not allowed. Allowed: {allowed_extensions}")
            return result
        
        result["is_valid"] = True
        
        # VULNERABLE: No validation logging validation
        self.validation_history.append({
            "type": "file_upload",
            "value": filename,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return result
    
    def add_custom_validator(self, name: str, validator_func):
        """VULNERABLE: Add custom validator without validation"""
        # VULNERABLE: No name validation
        # VULNERABLE: No validator function validation
        # VULNERABLE: No access control
        
        self.custom_validators[name] = validator_func
    
    def validate_with_custom(self, value: Any, validator_name: str) -> Dict[str, Any]:
        """VULNERABLE: Validate with custom validator without validation"""
        # VULNERABLE: No value validation
        # VULNERABLE: No validator name validation
        # VULNERABLE: No custom validation validation
        
        if validator_name not in self.custom_validators:
            return {
                "is_valid": False,
                "errors": [f"Custom validator '{validator_name}' not found"],
                "warnings": []
            }
        
        try:
            # VULNERABLE: No custom validator validation
            result = self.custom_validators[validator_name](value)
            return result
        except Exception as e:
            return {
                "is_valid": False,
                "errors": [f"Custom validation error: {str(e)}"],
                "warnings": []
            }
    
    def get_validation_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get validation history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.validation_history
    
    def clear_validation_history(self):
        """VULNERABLE: Clear validation history without validation"""
        # VULNERABLE: No validation
        # VULNERABLE: No access control
        
        self.validation_history = []
