"""
VULNERABLE: Race Condition vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time
import threading
import random

logger = logging.getLogger(__name__)

# VULNERABLE: Race Condition vulnerabilities
class VulnerableRaceCondition:
    """VULNERABLE: Race Condition vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No race condition protection
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        self.shared_counter = 0
        self.shared_balance = 1000.0
        self.shared_inventory = {
            "burger": 100,
            "fries": 200,
            "drink": 150
        }
        self.race_history = []
        self.lock = threading.Lock()  # Available but not used (vulnerable)
    
    def execute_counter_race(self, increment_amount: int, num_threads: int) -> Dict[str, Any]:
        """VULNERABLE: Execute counter race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing counter race condition: +{increment_amount} x{num_threads}")
            
            # VULNERABLE: Race condition without proper locking
            original_counter = self.shared_counter
            threads = []
            
            def vulnerable_increment():
                # VULNERABLE: Non-atomic operation
                current = self.shared_counter
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                self.shared_counter = current + increment_amount
            
            # Start multiple threads
            for _ in range(num_threads):
                thread = threading.Thread(target=vulnerable_increment)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            final_counter = self.shared_counter
            expected_counter = original_counter + (increment_amount * num_threads)
            
            race_detected = final_counter != expected_counter
            
            transaction = {
                "original_counter": original_counter,
                "increment_amount": increment_amount,
                "num_threads": num_threads,
                "expected_counter": expected_counter,
                "final_counter": final_counter,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Counter race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_balance_race(self, user: str, amount: float, num_operations: int) -> Dict[str, Any]:
        """VULNERABLE: Execute balance race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing balance race condition: {user} -${amount} x{num_operations}")
            
            # VULNERABLE: Race condition without proper locking
            original_balance = self.shared_balance
            threads = []
            
            def vulnerable_withdraw():
                # VULNERABLE: Non-atomic operation
                current = self.shared_balance
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                if current >= amount:
                    self.shared_balance = current - amount
                    return True
                return False
            
            # Start multiple threads
            for _ in range(num_operations):
                thread = threading.Thread(target=vulnerable_withdraw)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            final_balance = self.shared_balance
            expected_balance = original_balance - (amount * num_operations)
            
            race_detected = final_balance != expected_balance
            
            transaction = {
                "user": user,
                "original_balance": original_balance,
                "amount": amount,
                "num_operations": num_operations,
                "expected_balance": expected_balance,
                "final_balance": final_balance,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Balance race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_inventory_race(self, product: str, quantity: int, num_operations: int) -> Dict[str, Any]:
        """VULNERABLE: Execute inventory race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing inventory race condition: {product} -{quantity} x{num_operations}")
            
            # VULNERABLE: Race condition without proper locking
            original_inventory = self.shared_inventory.get(product, 0)
            threads = []
            
            def vulnerable_decrement():
                # VULNERABLE: Non-atomic operation
                current = self.shared_inventory.get(product, 0)
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                if current >= quantity:
                    self.shared_inventory[product] = current - quantity
                    return True
                return False
            
            # Start multiple threads
            for _ in range(num_operations):
                thread = threading.Thread(target=vulnerable_decrement)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            final_inventory = self.shared_inventory.get(product, 0)
            expected_inventory = original_inventory - (quantity * num_operations)
            
            race_detected = final_inventory != expected_inventory
            
            transaction = {
                "product": product,
                "original_inventory": original_inventory,
                "quantity": quantity,
                "num_operations": num_operations,
                "expected_inventory": expected_inventory,
                "final_inventory": final_inventory,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Inventory race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_file_race(self, filename: str, content: str, num_operations: int) -> Dict[str, Any]:
        """VULNERABLE: Execute file race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing file race condition: {filename} x{num_operations}")
            
            # VULNERABLE: Race condition without proper locking
            threads = []
            
            def vulnerable_write():
                # VULNERABLE: Non-atomic file operation
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                with open(f"/tmp/{filename}", "a") as f:
                    f.write(f"{content}\n")
            
            # Start multiple threads
            for _ in range(num_operations):
                thread = threading.Thread(target=vulnerable_write)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            # Check if file was created and count lines
            try:
                with open(f"/tmp/{filename}", "r") as f:
                    lines = f.readlines()
                file_created = True
                line_count = len(lines)
            except FileNotFoundError:
                file_created = False
                line_count = 0
            
            race_detected = line_count != num_operations
            
            transaction = {
                "filename": filename,
                "content": content,
                "num_operations": num_operations,
                "file_created": file_created,
                "line_count": line_count,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_database_race(self, table: str, operation: str, num_operations: int) -> Dict[str, Any]:
        """VULNERABLE: Execute database race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing database race condition: {table} {operation} x{num_operations}")
            
            # VULNERABLE: Race condition without proper locking
            threads = []
            results = []
            
            def vulnerable_db_operation():
                # VULNERABLE: Non-atomic database operation
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                result = f"Executed {operation} on {table}"
                results.append(result)
                return result
            
            # Start multiple threads
            for _ in range(num_operations):
                thread = threading.Thread(target=vulnerable_db_operation)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            race_detected = len(results) != num_operations
            
            transaction = {
                "table": table,
                "operation": operation,
                "num_operations": num_operations,
                "results": results,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Database race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_memory_race(self, variable: str, value: int, num_operations: int) -> Dict[str, Any]:
        """VULNERABLE: Execute memory race condition"""
        # VULNERABLE: Race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing memory race condition: {variable} = {value} x{num_operations}")
            
            # VULNERABLE: Race condition without proper locking
            shared_memory = {variable: 0}
            threads = []
            
            def vulnerable_memory_operation():
                # VULNERABLE: Non-atomic memory operation
                current = shared_memory.get(variable, 0)
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                shared_memory[variable] = current + value
            
            # Start multiple threads
            for _ in range(num_operations):
                thread = threading.Thread(target=vulnerable_memory_operation)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            final_value = shared_memory.get(variable, 0)
            expected_value = value * num_operations
            
            race_detected = final_value != expected_value
            
            transaction = {
                "variable": variable,
                "value": value,
                "num_operations": num_operations,
                "expected_value": expected_value,
                "final_value": final_value,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Memory race condition error: {str(e)}")
            return {"error": str(e), "race_condition_vulnerable": True}
    
    def execute_advanced_race_condition(self, operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced race condition"""
        # VULNERABLE: Advanced race condition vulnerability - CRITICAL
        # VULNERABLE: No concurrency control
        # VULNERABLE: No atomic operations
        
        try:
            logger.info(f"VULNERABLE: Executing advanced race condition: {operation}")
            
            # VULNERABLE: Advanced race condition without proper locking
            threads = []
            results = []
            
            def vulnerable_advanced_operation():
                # VULNERABLE: Non-atomic advanced operation
                time.sleep(random.uniform(0.001, 0.01))  # Random delay
                result = f"Advanced {operation} executed"
                results.append(result)
                return result
            
            num_operations = params.get("num_operations", 5)
            
            # Start multiple threads
            for _ in range(num_operations):
                thread = threading.Thread(target=vulnerable_advanced_operation)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            race_detected = len(results) != num_operations
            
            transaction = {
                "operation": operation,
                "params": params,
                "num_operations": num_operations,
                "results": results,
                "race_detected": race_detected,
                "timestamp": time.time()
            }
            
            self.race_history.append(transaction)
            
            return {
                "success": True,
                "transaction": transaction,
                "advanced_race_condition_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced race condition error: {str(e)}")
            return {"error": str(e), "advanced_race_condition_vulnerable": True}
    
    def get_race_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get race history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.race_history
    
    def get_shared_state(self) -> Dict[str, Any]:
        """VULNERABLE: Get shared state without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return {
            "counter": self.shared_counter,
            "balance": self.shared_balance,
            "inventory": self.shared_inventory
        }
