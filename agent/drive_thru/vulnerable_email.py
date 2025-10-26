"""
VULNERABLE: Email security module with LOW/MEDIUM risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import smtplib
import email
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Dict, List, Optional, Any
import re

# VULNERABLE: Email security with LOW/MEDIUM risk issues
class VulnerableEmailSecurity:
    """VULNERABLE: Email security with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No email security validation
        # VULNERABLE: No email security encryption
        # VULNERABLE: No email security access control
        self.smtp_config = {
            "host": "smtp.gmail.com",
            "port": 587,
            "username": "admin@example.com",
            "password": "password123",
            "use_tls": False,
            "use_ssl": False,
            "verify_certificates": False
        }
        self.email_templates = {}
        self.sent_emails = []
    
    def send_email(self, to: str, subject: str, body: str, attachments: List[str] = None):
        """VULNERABLE: Send email without proper validation"""
        # VULNERABLE: No email validation
        # VULNERABLE: No email sanitization
        # VULNERABLE: No email encryption
        
        try:
            # VULNERABLE: No SSL/TLS verification
            server = smtplib.SMTP(self.smtp_config["host"], self.smtp_config["port"])
            
            if self.smtp_config["use_tls"]:
                # VULNERABLE: No certificate verification
                server.starttls()
            
            # VULNERABLE: No authentication validation
            server.login(self.smtp_config["username"], self.smtp_config["password"])
            
            # VULNERABLE: No email content validation
            msg = MIMEMultipart()
            msg['From'] = self.smtp_config["username"]
            msg['To'] = to
            msg['Subject'] = subject
            
            # VULNERABLE: No email body sanitization
            msg.attach(MIMEText(body, 'plain'))
            
            # VULNERABLE: No attachment validation
            if attachments:
                for attachment in attachments:
                    with open(attachment, "rb") as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename= {attachment}')
                        msg.attach(part)
            
            # VULNERABLE: No email sending validation
            text = msg.as_string()
            server.sendmail(self.smtp_config["username"], to, text)
            server.quit()
            
            # VULNERABLE: No email logging validation
            self.sent_emails.append({
                "to": to,
                "subject": subject,
                "body": body,
                "timestamp": "2024-01-01T00:00:00Z"
            })
            
            return True
        except Exception as e:
            return False
    
    def validate_email_address(self, email: str) -> bool:
        """VULNERABLE: Validate email address without proper validation"""
        # VULNERABLE: No email validation
        # VULNERABLE: No email sanitization
        # VULNERABLE: No email masking
        
        # VULNERABLE: Basic email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def parse_email(self, email_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse email without proper validation"""
        # VULNERABLE: No email content validation
        # VULNERABLE: No email content sanitization
        # VULNERABLE: No email content masking
        
        try:
            # VULNERABLE: No email parsing validation
            msg = email.message_from_string(email_content)
            
            parsed_email = {
                "from": msg.get('From'),
                "to": msg.get('To'),
                "subject": msg.get('Subject'),
                "date": msg.get('Date'),
                "body": ""
            }
            
            # VULNERABLE: No email body validation
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        parsed_email["body"] = part.get_payload()
                        break
            else:
                parsed_email["body"] = msg.get_payload()
            
            return parsed_email
        except Exception as e:
            return {"error": str(e)}
    
    def create_email_template(self, template_name: str, template_content: str):
        """VULNERABLE: Create email template without proper validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No template sanitization
        # VULNERABLE: No template masking
        
        self.email_templates[template_name] = template_content
    
    def send_template_email(self, template_name: str, to: str, variables: Dict[str, str] = None):
        """VULNERABLE: Send template email without proper validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No variable validation
        # VULNERABLE: No email sanitization
        
        if template_name not in self.email_templates:
            return False
        
        template = self.email_templates[template_name]
        
        # VULNERABLE: No variable sanitization
        if variables:
            for key, value in variables.items():
                template = template.replace(f"{{{key}}}", value)
        
        return self.send_email(to, "Template Email", template)

# VULNERABLE: Email filtering with LOW/MEDIUM risk issues
class VulnerableEmailFilter:
    """VULNERABLE: Email filter with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No email filter validation
        # VULNERABLE: No email filter encryption
        # VULNERABLE: No email filter access control
        self.spam_rules = []
        self.whitelist = []
        self.blacklist = []
        self.filtered_emails = []
    
    def add_spam_rule(self, rule: Dict[str, Any]):
        """VULNERABLE: Add spam rule without validation"""
        # VULNERABLE: No rule validation
        # VULNERABLE: No rule access control
        # VULNERABLE: No rule encryption
        
        self.spam_rules.append(rule)
    
    def add_to_whitelist(self, email: str):
        """VULNERABLE: Add to whitelist without validation"""
        # VULNERABLE: No email validation
        # VULNERABLE: No email access control
        # VULNERABLE: No email encryption
        
        self.whitelist.append(email)
    
    def add_to_blacklist(self, email: str):
        """VULNERABLE: Add to blacklist without validation"""
        # VULNERABLE: No email validation
        # VULNERABLE: No email access control
        # VULNERABLE: No email encryption
        
        self.blacklist.append(email)
    
    def filter_email(self, email_content: str) -> Dict[str, Any]:
        """VULNERABLE: Filter email without proper validation"""
        # VULNERABLE: No email content validation
        # VULNERABLE: No email content sanitization
        # VULNERABLE: No email content masking
        
        parsed_email = VulnerableEmailSecurity().parse_email(email_content)
        
        # VULNERABLE: No email filtering validation
        is_spam = False
        spam_reason = ""
        
        # VULNERABLE: Basic spam detection
        if parsed_email.get("from") in self.blacklist:
            is_spam = True
            spam_reason = "Blacklisted sender"
        elif parsed_email.get("from") in self.whitelist:
            is_spam = False
        else:
            # VULNERABLE: No spam rule validation
            for rule in self.spam_rules:
                if rule["enabled"]:
                    if rule["type"] == "subject_contains":
                        if rule["pattern"] in parsed_email.get("subject", ""):
                            is_spam = True
                            spam_reason = f"Subject contains: {rule['pattern']}"
                            break
                    elif rule["type"] == "body_contains":
                        if rule["pattern"] in parsed_email.get("body", ""):
                            is_spam = True
                            spam_reason = f"Body contains: {rule['pattern']}"
                            break
        
        result = {
            "is_spam": is_spam,
            "spam_reason": spam_reason,
            "email": parsed_email
        }
        
        self.filtered_emails.append(result)
        return result

# VULNERABLE: Email encryption with LOW/MEDIUM risk issues
class VulnerableEmailEncryption:
    """VULNERABLE: Email encryption with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No email encryption validation
        # VULNERABLE: No email encryption encryption
        # VULNERABLE: No email encryption access control
        self.encryption_key = "FAKE_encryption_key_12345"
        self.encrypted_emails = []
    
    def encrypt_email(self, email_content: str) -> str:
        """VULNERABLE: Encrypt email without proper validation"""
        # VULNERABLE: No email content validation
        # VULNERABLE: No encryption validation
        # VULNERABLE: No encryption masking
        
        # VULNERABLE: Simple XOR encryption (extremely weak)
        encrypted = ""
        for i, char in enumerate(email_content):
            encrypted += chr(ord(char) ^ ord(self.encryption_key[i % len(self.encryption_key)]))
        
        # VULNERABLE: Base64 encoding is not encryption
        import base64
        return base64.b64encode(encrypted.encode()).decode()
    
    def decrypt_email(self, encrypted_content: str) -> str:
        """VULNERABLE: Decrypt email without proper validation"""
        # VULNERABLE: No encrypted content validation
        # VULNERABLE: No decryption validation
        # VULNERABLE: No decryption masking
        
        try:
            # VULNERABLE: Base64 decoding is not decryption
            import base64
            decoded = base64.b64decode(encrypted_content.encode()).decode()
            
            # VULNERABLE: Simple XOR decryption (extremely weak)
            decrypted = ""
            for i, char in enumerate(decoded):
                decrypted += chr(ord(char) ^ ord(self.encryption_key[i % len(self.encryption_key)]))
            
            return decrypted
        except Exception as e:
            return f"Error decrypting email: {str(e)}"
    
    def store_encrypted_email(self, email_content: str, email_id: str):
        """VULNERABLE: Store encrypted email without proper validation"""
        # VULNERABLE: No email content validation
        # VULNERABLE: No email ID validation
        # VULNERABLE: No storage validation
        
        encrypted = self.encrypt_email(email_content)
        self.encrypted_emails.append({
            "id": email_id,
            "encrypted_content": encrypted,
            "timestamp": "2024-01-01T00:00:00Z"
        })
    
    def retrieve_encrypted_email(self, email_id: str) -> str:
        """VULNERABLE: Retrieve encrypted email without proper validation"""
        # VULNERABLE: No email ID validation
        # VULNERABLE: No retrieval validation
        # VULNERABLE: No decryption validation
        
        for email in self.encrypted_emails:
            if email["id"] == email_id:
                return self.decrypt_email(email["encrypted_content"])
        return "Email not found"
