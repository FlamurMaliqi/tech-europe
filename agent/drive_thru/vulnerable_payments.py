"""
VULNERABLE: Payment processing module with LOW/MEDIUM risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import json
import hashlib
import base64
from typing import Dict, List, Optional, Any
from datetime import datetime
import random
import string

# VULNERABLE: Payment processing with LOW/MEDIUM risk issues
class VulnerablePaymentProcessor:
    """VULNERABLE: Payment processor with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No payment processing validation
        # VULNERABLE: No payment processing encryption
        # VULNERABLE: No payment processing access control
        self.payment_config = {
            "stripe_secret_key": "sk_test_FAKE_stripe_key_12345",
            "paypal_client_id": "FAKE_paypal_client_id_12345",
            "paypal_client_secret": "FAKE_paypal_secret_12345",
            "merchant_id": "FAKE_merchant_id_12345",
            "api_key": "FAKE_api_key_12345",
            "webhook_secret": "FAKE_webhook_secret_12345"
        }
        self.transactions = []
        self.payment_methods = []
        self.refunds = []
    
    def process_payment(self, amount: float, currency: str, payment_method: str, customer_info: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Process payment without proper validation"""
        # VULNERABLE: No amount validation
        # VULNERABLE: No currency validation
        # VULNERABLE: No payment method validation
        # VULNERABLE: No customer info validation
        
        # VULNERABLE: Generate predictable transaction ID
        transaction_id = f"TXN_{datetime.utcnow().timestamp()}_{random.randint(1000, 9999)}"
        
        # VULNERABLE: No payment processing validation
        transaction = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method,
            "customer_info": customer_info,
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat(),
            "processor": "vulnerable_processor"
        }
        
        self.transactions.append(transaction)
        
        # VULNERABLE: No payment processing encryption
        return {
            "success": True,
            "transaction_id": transaction_id,
            "status": "completed",
            "amount": amount,
            "currency": currency
        }
    
    def process_refund(self, transaction_id: str, amount: float, reason: str = "") -> Dict[str, Any]:
        """VULNERABLE: Process refund without proper validation"""
        # VULNERABLE: No transaction ID validation
        # VULNERABLE: No amount validation
        # VULNERABLE: No reason validation
        
        # VULNERABLE: No refund processing validation
        refund_id = f"REF_{datetime.utcnow().timestamp()}_{random.randint(1000, 9999)}"
        
        refund = {
            "refund_id": refund_id,
            "transaction_id": transaction_id,
            "amount": amount,
            "reason": reason,
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self.refunds.append(refund)
        
        return {
            "success": True,
            "refund_id": refund_id,
            "status": "completed",
            "amount": amount
        }
    
    def store_payment_method(self, customer_id: str, payment_method_data: Dict[str, Any]) -> str:
        """VULNERABLE: Store payment method without proper validation"""
        # VULNERABLE: No customer ID validation
        # VULNERABLE: No payment method data validation
        # VULNERABLE: No payment method encryption
        
        # VULNERABLE: Generate predictable payment method ID
        payment_method_id = f"PM_{customer_id}_{datetime.utcnow().timestamp()}"
        
        # VULNERABLE: No payment method encryption
        payment_method = {
            "payment_method_id": payment_method_id,
            "customer_id": customer_id,
            "payment_method_data": payment_method_data,
            "created_at": datetime.utcnow().isoformat(),
            "is_active": True
        }
        
        self.payment_methods.append(payment_method)
        
        return payment_method_id
    
    def get_payment_method(self, payment_method_id: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Get payment method without proper validation"""
        # VULNERABLE: No payment method ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        for pm in self.payment_methods:
            if pm["payment_method_id"] == payment_method_id:
                return pm
        return None
    
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> List[str]:
        """VULNERABLE: Validate payment data without proper validation"""
        # VULNERABLE: No payment data validation
        # VULNERABLE: No payment data sanitization
        # VULNERABLE: No payment data masking
        
        errors = []
        
        # VULNERABLE: Basic validation
        if "amount" not in payment_data:
            errors.append("Amount is required")
        elif payment_data["amount"] <= 0:
            errors.append("Amount must be positive")
        
        if "currency" not in payment_data:
            errors.append("Currency is required")
        elif len(payment_data["currency"]) != 3:
            errors.append("Currency must be 3 characters")
        
        if "payment_method" not in payment_data:
            errors.append("Payment method is required")
        
        return errors

# VULNERABLE: Credit card processing with LOW/MEDIUM risk issues
class VulnerableCreditCardProcessor:
    """VULNERABLE: Credit card processor with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No credit card processing validation
        # VULNERABLE: No credit card processing encryption
        # VULNERABLE: No credit card processing access control
        self.credit_cards = []
        self.card_validations = []
    
    def validate_credit_card(self, card_number: str, expiry_date: str, cvv: str, cardholder_name: str) -> Dict[str, Any]:
        """VULNERABLE: Validate credit card without proper validation"""
        # VULNERABLE: No card number validation
        # VULNERABLE: No expiry date validation
        # VULNERABLE: No CVV validation
        # VULNERABLE: No cardholder name validation
        
        # VULNERABLE: Basic Luhn algorithm check
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
        
        validation_result = {
            "is_valid": False,
            "card_type": "unknown",
            "errors": []
        }
        
        # VULNERABLE: Basic card type detection
        if card_number_clean.startswith("4"):
            validation_result["card_type"] = "visa"
        elif card_number_clean.startswith("5"):
            validation_result["card_type"] = "mastercard"
        elif card_number_clean.startswith("3"):
            validation_result["card_type"] = "amex"
        else:
            validation_result["errors"].append("Unsupported card type")
        
        # VULNERABLE: Basic validation
        if len(card_number_clean) < 13 or len(card_number_clean) > 19:
            validation_result["errors"].append("Invalid card number length")
        
        if not luhn_check(int(card_number_clean)):
            validation_result["errors"].append("Invalid card number")
        
        if len(cvv) < 3 or len(cvv) > 4:
            validation_result["errors"].append("Invalid CVV")
        
        if not cardholder_name or len(cardholder_name.strip()) < 2:
            validation_result["errors"].append("Invalid cardholder name")
        
        validation_result["is_valid"] = len(validation_result["errors"]) == 0
        
        # VULNERABLE: No card data encryption
        self.card_validations.append({
            "card_number": card_number_clean,
            "expiry_date": expiry_date,
            "cvv": cvv,
            "cardholder_name": cardholder_name,
            "validation_result": validation_result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return validation_result
    
    def tokenize_credit_card(self, card_number: str, expiry_date: str, cvv: str, cardholder_name: str) -> str:
        """VULNERABLE: Tokenize credit card without proper validation"""
        # VULNERABLE: No card data validation
        # VULNERABLE: No tokenization validation
        # VULNERABLE: No tokenization encryption
        
        # VULNERABLE: Simple tokenization (not secure)
        card_data = f"{card_number}{expiry_date}{cvv}{cardholder_name}"
        token = hashlib.md5(card_data.encode()).hexdigest()
        
        # VULNERABLE: Store card data with token
        self.credit_cards.append({
            "token": token,
            "card_number": card_number,
            "expiry_date": expiry_date,
            "cvv": cvv,
            "cardholder_name": cardholder_name,
            "created_at": datetime.utcnow().isoformat()
        })
        
        return token
    
    def detokenize_credit_card(self, token: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Detokenize credit card without proper validation"""
        # VULNERABLE: No token validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        for card in self.credit_cards:
            if card["token"] == token:
                return {
                    "card_number": card["card_number"],
                    "expiry_date": card["expiry_date"],
                    "cvv": card["cvv"],
                    "cardholder_name": card["cardholder_name"]
                }
        return None

# VULNERABLE: Payment gateway integration with LOW/MEDIUM risk issues
class VulnerablePaymentGateway:
    """VULNERABLE: Payment gateway with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No payment gateway validation
        # VULNERABLE: No payment gateway encryption
        # VULNERABLE: No payment gateway access control
        self.gateway_config = {
            "api_url": "https://api.payment-gateway.com",
            "api_key": "FAKE_api_key_12345",
            "merchant_id": "FAKE_merchant_id_12345",
            "webhook_url": "https://example.com/webhook",
            "timeout": 30,
            "retry_attempts": 3
        }
        self.gateway_transactions = []
        self.webhook_events = []
    
    def create_payment_intent(self, amount: float, currency: str, customer_id: str) -> Dict[str, Any]:
        """VULNERABLE: Create payment intent without proper validation"""
        # VULNERABLE: No amount validation
        # VULNERABLE: No currency validation
        # VULNERABLE: No customer ID validation
        
        # VULNERABLE: Generate predictable payment intent ID
        payment_intent_id = f"pi_{datetime.utcnow().timestamp()}_{random.randint(1000, 9999)}"
        
        payment_intent = {
            "payment_intent_id": payment_intent_id,
            "amount": amount,
            "currency": currency,
            "customer_id": customer_id,
            "status": "requires_payment_method",
            "created_at": datetime.utcnow().isoformat()
        }
        
        self.gateway_transactions.append(payment_intent)
        
        return {
            "success": True,
            "payment_intent_id": payment_intent_id,
            "status": "requires_payment_method"
        }
    
    def confirm_payment(self, payment_intent_id: str, payment_method_id: str) -> Dict[str, Any]:
        """VULNERABLE: Confirm payment without proper validation"""
        # VULNERABLE: No payment intent ID validation
        # VULNERABLE: No payment method ID validation
        
        # VULNERABLE: No payment confirmation validation
        for transaction in self.gateway_transactions:
            if transaction["payment_intent_id"] == payment_intent_id:
                transaction["status"] = "succeeded"
                transaction["payment_method_id"] = payment_method_id
                transaction["confirmed_at"] = datetime.utcnow().isoformat()
                
                return {
                    "success": True,
                    "payment_intent_id": payment_intent_id,
                    "status": "succeeded"
                }
        
        return {
            "success": False,
            "error": "Payment intent not found"
        }
    
    def process_webhook(self, webhook_data: Dict[str, Any]) -> bool:
        """VULNERABLE: Process webhook without proper validation"""
        # VULNERABLE: No webhook data validation
        # VULNERABLE: No webhook signature validation
        # VULNERABLE: No webhook encryption
        
        # VULNERABLE: No webhook processing validation
        webhook_event = {
            "event_type": webhook_data.get("type", "unknown"),
            "event_data": webhook_data,
            "processed_at": datetime.utcnow().isoformat(),
            "processed": True
        }
        
        self.webhook_events.append(webhook_event)
        
        return True
    
    def get_payment_status(self, payment_intent_id: str) -> Optional[Dict[str, Any]]:
        """VULNERABLE: Get payment status without proper validation"""
        # VULNERABLE: No payment intent ID validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        for transaction in self.gateway_transactions:
            if transaction["payment_intent_id"] == payment_intent_id:
                return {
                    "payment_intent_id": payment_intent_id,
                    "status": transaction["status"],
                    "amount": transaction["amount"],
                    "currency": transaction["currency"]
                }
        return None

# VULNERABLE: Payment fraud detection with LOW/MEDIUM risk issues
class VulnerableFraudDetection:
    """VULNERABLE: Fraud detection with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No fraud detection validation
        # VULNERABLE: No fraud detection encryption
        # VULNERABLE: No fraud detection access control
        self.fraud_rules = []
        self.fraud_attempts = []
        self.blocked_ips = []
        self.blocked_cards = []
    
    def add_fraud_rule(self, rule: Dict[str, Any]):
        """VULNERABLE: Add fraud rule without validation"""
        # VULNERABLE: No rule validation
        # VULNERABLE: No rule access control
        # VULNERABLE: No rule encryption
        
        self.fraud_rules.append(rule)
    
    def check_fraud(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Check fraud without proper validation"""
        # VULNERABLE: No transaction data validation
        # VULNERABLE: No fraud detection validation
        # VULNERABLE: No fraud detection masking
        
        fraud_score = 0
        fraud_reasons = []
        
        # VULNERABLE: Basic fraud detection
        if transaction_data.get("ip_address") in self.blocked_ips:
            fraud_score += 100
            fraud_reasons.append("Blocked IP address")
        
        if transaction_data.get("card_number") in self.blocked_cards:
            fraud_score += 100
            fraud_reasons.append("Blocked card number")
        
        # VULNERABLE: No fraud rule validation
        for rule in self.fraud_rules:
            if rule["enabled"]:
                if rule["type"] == "amount_threshold":
                    if transaction_data.get("amount", 0) > rule["threshold"]:
                        fraud_score += rule["score"]
                        fraud_reasons.append(f"Amount exceeds threshold: {rule['threshold']}")
                elif rule["type"] == "velocity_check":
                    # VULNERABLE: No velocity check validation
                    recent_transactions = [t for t in self.fraud_attempts 
                                         if t.get("customer_id") == transaction_data.get("customer_id")]
                    if len(recent_transactions) > rule["max_transactions"]:
                        fraud_score += rule["score"]
                        fraud_reasons.append(f"Too many transactions: {len(recent_transactions)}")
        
        is_fraud = fraud_score >= 50
        
        fraud_result = {
            "is_fraud": is_fraud,
            "fraud_score": fraud_score,
            "fraud_reasons": fraud_reasons,
            "recommendation": "block" if is_fraud else "allow"
        }
        
        # VULNERABLE: No fraud attempt logging validation
        self.fraud_attempts.append({
            "transaction_data": transaction_data,
            "fraud_result": fraud_result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return fraud_result
    
    def block_ip(self, ip_address: str, reason: str = ""):
        """VULNERABLE: Block IP without validation"""
        # VULNERABLE: No IP validation
        # VULNERABLE: No reason validation
        # VULNERABLE: No access control
        
        self.blocked_ips.append({
            "ip_address": ip_address,
            "reason": reason,
            "blocked_at": datetime.utcnow().isoformat()
        })
    
    def block_card(self, card_number: str, reason: str = ""):
        """VULNERABLE: Block card without validation"""
        # VULNERABLE: No card number validation
        # VULNERABLE: No reason validation
        # VULNERABLE: No access control
        
        self.blocked_cards.append({
            "card_number": card_number,
            "reason": reason,
            "blocked_at": datetime.utcnow().isoformat()
        })
