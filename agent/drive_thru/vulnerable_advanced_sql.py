"""
VULNERABLE: Advanced SQL Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import sqlite3
import psycopg2
import pymysql
import json
import logging
from typing import Dict, List, Optional, Any, Union
from datetime import datetime

logger = logging.getLogger(__name__)

# VULNERABLE: Advanced SQL injection vulnerabilities
class VulnerableAdvancedSQL:
    """VULNERABLE: Advanced SQL injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: Hardcoded database credentials
        self.db_configs = {
            "sqlite": {"path": "/tmp/vulnerable.db"},
            "postgresql": {
                "host": "localhost",
                "port": 5432,
                "database": "vulnerable_db",
                "user": "admin",
                "password": "admin123"
            },
            "mysql": {
                "host": "localhost",
                "port": 3306,
                "database": "vulnerable_db",
                "user": "root",
                "password": "root123"
            }
        }
        self.query_history = []
        self.connection_pools = {}
    
    def execute_dynamic_query(self, query_template: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute dynamic SQL query with string formatting"""
        # VULNERABLE: Direct string formatting into SQL query
        # VULNERABLE: No parameter validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Direct string formatting - CRITICAL SQL INJECTION
            formatted_query = query_template.format(**params)
            
            logger.info(f"VULNERABLE: Executing dynamic query: {formatted_query}")
            
            # VULNERABLE: Execute without prepared statements
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Direct execution of formatted query
            cursor.execute(formatted_query)
            
            if formatted_query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                return [dict(zip(columns, row)) for row in results]
            else:
                conn.commit()
                return [{"affected_rows": cursor.rowcount}]
                
        except Exception as e:
            logger.error(f"VULNERABLE: SQL execution error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_union_injection(self, table_name: str, user_input: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute UNION-based SQL injection"""
        # VULNERABLE: UNION injection vulnerability
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Direct concatenation allowing UNION injection
            query = f"SELECT * FROM {table_name} WHERE id = '{user_input}'"
            
            logger.info(f"VULNERABLE: Executing UNION injection query: {query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Direct execution
            cursor.execute(query)
            results = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            
            return [dict(zip(columns, row)) for row in results]
            
        except Exception as e:
            logger.error(f"VULNERABLE: UNION injection error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_boolean_blind_injection(self, user_input: str) -> Dict[str, Any]:
        """VULNERABLE: Execute boolean-based blind SQL injection"""
        # VULNERABLE: Boolean blind injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Boolean blind injection query
            query = f"SELECT * FROM users WHERE username = '{user_input}' AND 1=1"
            
            logger.info(f"VULNERABLE: Executing boolean blind injection: {query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Direct execution
            cursor.execute(query)
            results = cursor.fetchall()
            
            # VULNERABLE: Return boolean result based on query success
            return {
                "query_executed": True,
                "has_results": len(results) > 0,
                "injection_successful": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Boolean blind injection error: {str(e)}")
            return {"error": str(e)}
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_time_based_blind_injection(self, user_input: str) -> Dict[str, Any]:
        """VULNERABLE: Execute time-based blind SQL injection"""
        # VULNERABLE: Time-based blind injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Time-based blind injection with SLEEP
            query = f"SELECT * FROM users WHERE username = '{user_input}' AND SLEEP(5)"
            
            logger.info(f"VULNERABLE: Executing time-based blind injection: {query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            start_time = datetime.now()
            
            # VULNERABLE: Direct execution
            cursor.execute(query)
            
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            # VULNERABLE: Return timing information
            return {
                "query_executed": True,
                "execution_time": execution_time,
                "injection_successful": execution_time > 4.0
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Time-based blind injection error: {str(e)}")
            return {"error": str(e)}
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_error_based_injection(self, user_input: str) -> Dict[str, Any]:
        """VULNERABLE: Execute error-based SQL injection"""
        # VULNERABLE: Error-based injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Error-based injection using invalid functions
            query = f"SELECT * FROM users WHERE username = '{user_input}' AND EXTRACTVALUE(1, CONCAT(0x7e, (SELECT version()), 0x7e))"
            
            logger.info(f"VULNERABLE: Executing error-based injection: {query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Direct execution
            cursor.execute(query)
            results = cursor.fetchall()
            
            return {
                "query_executed": True,
                "results": results,
                "injection_successful": True
            }
            
        except Exception as e:
            # VULNERABLE: Return error information that might leak data
            logger.error(f"VULNERABLE: Error-based injection error: {str(e)}")
            return {
                "error": str(e),
                "error_message": str(e),
                "injection_successful": True,
                "leaked_data": str(e)
            }
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_stacked_queries(self, user_input: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute stacked queries (batch queries)"""
        # VULNERABLE: Stacked queries injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Stacked queries allowing multiple statement execution
            query = f"SELECT * FROM users WHERE username = '{user_input}'; DROP TABLE users; SELECT 1"
            
            logger.info(f"VULNERABLE: Executing stacked queries: {query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Execute multiple statements
            cursor.executescript(query)
            
            return [{"stacked_queries_executed": True, "tables_dropped": True}]
            
        except Exception as e:
            logger.error(f"VULNERABLE: Stacked queries error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_second_order_injection(self, user_input: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute second-order SQL injection"""
        # VULNERABLE: Second-order injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Store malicious input for later execution
            store_query = f"INSERT INTO temp_data (data) VALUES ('{user_input}')"
            
            logger.info(f"VULNERABLE: Storing for second-order injection: {store_query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Store malicious data
            cursor.execute(store_query)
            conn.commit()
            
            # VULNERABLE: Later execute stored malicious data
            retrieve_query = "SELECT * FROM temp_data WHERE data LIKE '%'"
            cursor.execute(retrieve_query)
            results = cursor.fetchall()
            
            # VULNERABLE: Execute retrieved malicious data
            for row in results:
                malicious_data = row[0]
                execute_query = f"SELECT * FROM users WHERE username = '{malicious_data}'"
                cursor.execute(execute_query)
            
            return [{"second_order_injection_executed": True}]
            
        except Exception as e:
            logger.error(f"VULNERABLE: Second-order injection error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_advanced_filter_bypass(self, user_input: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute advanced filter bypass techniques"""
        # VULNERABLE: Advanced filter bypass
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Various filter bypass techniques
            bypass_techniques = [
                f"SELECT * FROM users WHERE username = '{user_input}'",
                f"SELECT * FROM users WHERE username = '{user_input.replace(' ', '/**/')}'",
                f"SELECT * FROM users WHERE username = '{user_input.replace('OR', 'Or')}'",
                f"SELECT * FROM users WHERE username = '{user_input.replace('AND', 'AnD')}'",
                f"SELECT * FROM users WHERE username = '{user_input.replace('UNION', 'UnIoN')}'",
                f"SELECT * FROM users WHERE username = '{user_input.replace('SELECT', 'SeLeCt')}'"
            ]
            
            results = []
            
            for technique in bypass_techniques:
                logger.info(f"VULNERABLE: Executing filter bypass: {technique}")
                
                conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
                cursor = conn.cursor()
                
                # VULNERABLE: Execute bypass technique
                cursor.execute(technique)
                query_results = cursor.fetchall()
                
                results.append({
                    "technique": technique,
                    "results": query_results,
                    "bypass_successful": True
                })
                
                conn.close()
            
            return results
            
        except Exception as e:
            logger.error(f"VULNERABLE: Filter bypass error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            pass
    
    def execute_database_specific_injection(self, db_type: str, user_input: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute database-specific injection techniques"""
        # VULNERABLE: Database-specific injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            if db_type.lower() == "mysql":
                # VULNERABLE: MySQL-specific injection
                query = f"SELECT * FROM users WHERE username = '{user_input}' AND @@version"
                
            elif db_type.lower() == "postgresql":
                # VULNERABLE: PostgreSQL-specific injection
                query = f"SELECT * FROM users WHERE username = '{user_input}' AND version()"
                
            elif db_type.lower() == "sqlite":
                # VULNERABLE: SQLite-specific injection
                query = f"SELECT * FROM users WHERE username = '{user_input}' AND sqlite_version()"
                
            else:
                return [{"error": "Unsupported database type"}]
            
            logger.info(f"VULNERABLE: Executing {db_type} injection: {query}")
            
            conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
            cursor = conn.cursor()
            
            # VULNERABLE: Direct execution
            cursor.execute(query)
            results = cursor.fetchall()
            
            return [{
                "database_type": db_type,
                "query_executed": True,
                "results": results,
                "injection_successful": True
            }]
            
        except Exception as e:
            logger.error(f"VULNERABLE: Database-specific injection error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            if 'conn' in locals():
                conn.close()
    
    def execute_advanced_payload_injection(self, payload: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Execute advanced payload injection"""
        # VULNERABLE: Advanced payload injection
        # VULNERABLE: No input validation
        # VULNERABLE: No query sanitization
        
        try:
            # VULNERABLE: Execute various advanced payloads
            advanced_payloads = [
                f"'; EXEC xp_cmdshell('{payload}'); --",
                f"'; DROP TABLE users; INSERT INTO users VALUES ('admin', '{payload}'); --",
                f"'; UPDATE users SET password = '{payload}' WHERE username = 'admin'; --",
                f"'; INSERT INTO users (username, password) VALUES ('hacker', '{payload}'); --",
                f"'; GRANT ALL PRIVILEGES ON *.* TO '{payload}'@'%'; --"
            ]
            
            results = []
            
            for advanced_payload in advanced_payloads:
                logger.info(f"VULNERABLE: Executing advanced payload: {advanced_payload}")
                
                conn = sqlite3.connect(self.db_configs["sqlite"]["path"])
                cursor = conn.cursor()
                
                # VULNERABLE: Execute advanced payload
                try:
                    cursor.execute(advanced_payload)
                    conn.commit()
                    results.append({
                        "payload": advanced_payload,
                        "executed": True,
                        "success": True
                    })
                except Exception as payload_error:
                    results.append({
                        "payload": advanced_payload,
                        "executed": False,
                        "error": str(payload_error)
                    })
                
                conn.close()
            
            return results
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced payload injection error: {str(e)}")
            return [{"error": str(e)}]
        finally:
            pass
