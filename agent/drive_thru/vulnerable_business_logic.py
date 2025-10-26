"""
VULNERABLE: Business Logic vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import random

logger = logging.getLogger(__name__)

# VULNERABLE: Business Logic vulnerabilities
class VulnerableBusinessLogic:
    """VULNERABLE: Business Logic vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No business logic validation
        # VULNERABLE: No input validation
        # VULNERABLE: No access control
        self.transaction_history = []
        self.user_balances = {
            "user1": 1000.0,
            "user2": 500.0,
            "admin": 10000.0
        }
        self.product_prices = {
            "burger": 5.99,
            "fries": 2.49,
            "drink": 1.99
        }
        self.coupon_codes = {
            "SAVE10": 0.1,
            "SAVE20": 0.2,
            "SAVE50": 0.5
        }
    
    def execute_price_manipulation(self, product: str, quantity: int, price_override: float) -> Dict[str, Any]:
        """VULNERABLE: Execute price manipulation"""
        # VULNERABLE: Price manipulation vulnerability - CRITICAL
        # VULNERABLE: No price validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing price manipulation: {product} x{quantity} @ ${price_override}")
            
            # VULNERABLE: Direct price override without validation
            original_price = self.product_prices.get(product, 0)
            total_cost = quantity * price_override
            
            transaction = {
                "product": product,
                "quantity": quantity,
                "original_price": original_price,
                "manipulated_price": price_override,
                "total_cost": total_cost,
                "timestamp": time.time(),
                "manipulated": True
            }
            
            self.transaction_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "price_manipulation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Price manipulation error: {str(e)}")
            return {"error": str(e), "price_manipulation_vulnerable": True}
    
    def execute_negative_quantity(self, product: str, quantity: int) -> Dict[str, Any]:
        """VULNERABLE: Execute negative quantity manipulation"""
        # VULNERABLE: Negative quantity vulnerability - CRITICAL
        # VULNERABLE: No quantity validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing negative quantity manipulation: {product} x{quantity}")
            
            # VULNERABLE: Allow negative quantities without validation
            price = self.product_prices.get(product, 0)
            total_cost = quantity * price
            
            transaction = {
                "product": product,
                "quantity": quantity,
                "price": price,
                "total_cost": total_cost,
                "timestamp": time.time(),
                "negative_quantity": quantity < 0
            }
            
            self.transaction_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "negative_quantity_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Negative quantity manipulation error: {str(e)}")
            return {"error": str(e), "negative_quantity_vulnerable": True}
    
    def execute_coupon_abuse(self, coupon_code: str, discount_multiplier: float) -> Dict[str, Any]:
        """VULNERABLE: Execute coupon abuse"""
        # VULNERABLE: Coupon abuse vulnerability - CRITICAL
        # VULNERABLE: No coupon validation
        # VULNERABLE: No discount validation
        
        try:
            logger.info(f"VULNERABLE: Executing coupon abuse: {coupon_code} x{discount_multiplier}")
            
            # VULNERABLE: Allow arbitrary discount multipliers
            original_discount = self.coupon_codes.get(coupon_code, 0)
            abused_discount = original_discount * discount_multiplier
            
            transaction = {
                "coupon_code": coupon_code,
                "original_discount": original_discount,
                "abused_discount": abused_discount,
                "discount_multiplier": discount_multiplier,
                "timestamp": time.time(),
                "abused": True
            }
            
            self.transaction_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "coupon_abuse_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Coupon abuse error: {str(e)}")
            return {"error": str(e), "coupon_abuse_vulnerable": True}
    
    def execute_balance_manipulation(self, user: str, amount: float) -> Dict[str, Any]:
        """VULNERABLE: Execute balance manipulation"""
        # VULNERABLE: Balance manipulation vulnerability - CRITICAL
        # VULNERABLE: No balance validation
        # VULNERABLE: No authorization check
        
        try:
            logger.info(f"VULNERABLE: Executing balance manipulation: {user} +${amount}")
            
            # VULNERABLE: Direct balance manipulation without validation
            original_balance = self.user_balances.get(user, 0)
            new_balance = original_balance + amount
            
            self.user_balances[user] = new_balance
            
            transaction = {
                "user": user,
                "original_balance": original_balance,
                "amount_added": amount,
                "new_balance": new_balance,
                "timestamp": time.time(),
                "manipulated": True
            }
            
            self.transaction_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "balance_manipulation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Balance manipulation error: {str(e)}")
            return {"error": str(e), "balance_manipulation_vulnerable": True}
    
    def execute_race_condition(self, user: str, amount: float) -> Dict[str, Any]:
        """VULNERABLE: Execute race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing race condition: {user} -${amount}")
            
            # VULNERABLE: Race condition without proper locking
            original_balance = self.user_balances.get(user, 0)
            
            # VULNERABLE: Simulate race condition
            time.sleep(random.uniform(0.001, 0.01))  # Random delay
            
            if original_balance >= amount:
                new_balance = original_balance - amount
                self.user_balances[user] = new_balance
                
                transaction = {
                    "user": user,
                    "original_balance": original_balance,
                    "amount_deducted": amount,
                    "new_balance": new_balance,
                    "timestamp": time.time(),
                    "race_condition": True
                }
                
                self.transaction_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "race_condition_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Insufficient balance",
                    "race_condition_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_workflow_bypass(self, step: str, bypass_data: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute workflow bypass"""
        # VULNERABLE: Workflow bypass vulnerability - CRITICAL
        # VULNERABLE: No workflow validation
        # VULNERABLE: No step verification
        
        try:
            logger.info(f"VULNERABLE: Executing workflow bypass: {step}")
            
            # VULNERABLE: Allow workflow step bypass
            workflow_steps = ["step1", "step2", "step3", "step4", "step5"]
            
            if step in workflow_steps:
                transaction = {
                    "step": step,
                    "bypass_data": bypass_data,
                    "timestamp": time.time(),
                    "bypassed": True
                }
                
                self.transaction_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "workflow_bypass_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Invalid step",
                    "workflow_bypass_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Workflow bypass error: {str(e)}")
            return {"error": str(e), "workflow_bypass_vulnerable": True}
    
    def execute_privilege_escalation(self, user: str, target_role: str) -> Dict[str, Any]:
        """VULNERABLE: Execute privilege escalation"""
        # VULNERABLE: Privilege escalation vulnerability - CRITICAL
        # VULNERABLE: No role validation
        # VULNERABLE: No authorization check
        
        try:
            logger.info(f"VULNERABLE: Executing privilege escalation: {user} -> {target_role}")
            
            # VULNERABLE: Allow arbitrary role assignment
            roles = ["user", "admin", "superadmin", "root"]
            
            if target_role in roles:
                transaction = {
                    "user": user,
                    "target_role": target_role,
                    "timestamp": time.time(),
                    "privilege_escalated": True
                }
                
                self.transaction_history.append(transaction)
                
                return {
                    "success": True,
                    "transaction": transaction,
                    "privilege_escalation_vulnerable": True
                }
            else:
                return {
                    "success": False,
                    "error": "Invalid role",
                    "privilege_escalation_vulnerable": True
                }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Privilege escalation error: {str(e)}")
            return {"error": str(e), "privilege_escalation_vulnerable": True}
    
    def execute_business_logic_bypass(self, operation: str, bypass_params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute business logic bypass"""
        # VULNERABLE: Business logic bypass vulnerability - CRITICAL
        # VULNERABLE: No logic validation
        # VULNERABLE: No parameter validation
        
        try:
            logger.info(f"VULNERABLE: Executing business logic bypass: {operation}")
            
            # VULNERABLE: Allow business logic bypass
            transaction = {
                "operation": operation,
                "bypass_params": bypass_params,
                "timestamp": time.time(),
                "logic_bypassed": True
            }
            
            self.transaction_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "business_logic_bypass_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Business logic bypass error: {str(e)}")
            return {"error": str(e), "business_logic_bypass_vulnerable": True}
    
    def get_transaction_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get transaction history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.transaction_history
    
    def get_user_balances(self) -> Dict[str, float]:
        """VULNERABLE: Get user balances without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.user_balances
