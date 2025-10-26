"""
VULNERABLE: NoSQL Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import json
import logging
from typing import Dict, List, Optional, Any
import re
import time

logger = logging.getLogger(__name__)

# VULNERABLE: NoSQL Injection vulnerabilities
class VulnerableNoSQLInjection:
    """VULNERABLE: NoSQL Injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No NoSQL injection protection
        # VULNERABLE: No query validation
        # VULNERABLE: No input sanitization
        self.query_history = []
        self.injection_patterns = [
            r'\$where',
            r'\$regex',
            r'\$ne',
            r'\$gt',
            r'\$lt',
            r'\$gte',
            r'\$lte',
            r'\$in',
            r'\$nin',
            r'\$exists',
            r'\$or',
            r'\$and',
            r'\$not',
            r'\$nor',
            r'\$all',
            r'\$elemMatch',
            r'\$size',
            r'\$type',
            r'\$mod',
            r'\$text',
            r'\$geoWithin',
            r'\$geoIntersects',
            r'\$near',
            r'\$nearSphere'
        ]
    
    def execute_mongodb_injection(self, collection: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute MongoDB NoSQL injection"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No query validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing MongoDB injection on {collection}: {query}")
            
            # VULNERABLE: Direct query execution without validation
            parsed_query = json.loads(query) if query.startswith('{') else {"$where": query}
            
            # VULNERABLE: Execute query without sanitization
            result = self._execute_mongodb_query(collection, parsed_query)
            
            self.query_history.append({
                "collection": collection,
                "query": query,
                "parsed_query": parsed_query,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "collection": collection,
                "query": query,
                "parsed_query": parsed_query,
                "result": result,
                "nosql_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: MongoDB injection error: {str(e)}")
            return {"error": str(e), "nosql_injection_vulnerable": True}
    
    def execute_couchdb_injection(self, database: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute CouchDB NoSQL injection"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No query validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing CouchDB injection on {database}: {query}")
            
            # VULNERABLE: Direct query execution without validation
            parsed_query = json.loads(query) if query.startswith('{') else {"selector": query}
            
            # VULNERABLE: Execute query without sanitization
            result = self._execute_couchdb_query(database, parsed_query)
            
            return {
                "success": True,
                "database": database,
                "query": query,
                "parsed_query": parsed_query,
                "result": result,
                "couchdb_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: CouchDB injection error: {str(e)}")
            return {"error": str(e), "couchdb_injection_vulnerable": True}
    
    def execute_cassandra_injection(self, keyspace: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Cassandra NoSQL injection"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No query validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Cassandra injection on {keyspace}: {query}")
            
            # VULNERABLE: Direct query execution without validation
            result = self._execute_cassandra_query(keyspace, query)
            
            return {
                "success": True,
                "keyspace": keyspace,
                "query": query,
                "result": result,
                "cassandra_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Cassandra injection error: {str(e)}")
            return {"error": str(e), "cassandra_injection_vulnerable": True}
    
    def execute_redis_injection(self, key: str, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Redis NoSQL injection"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Redis injection on {key}: {command}")
            
            # VULNERABLE: Direct command execution without validation
            result = self._execute_redis_command(key, command)
            
            return {
                "success": True,
                "key": key,
                "command": command,
                "result": result,
                "redis_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Redis injection error: {str(e)}")
            return {"error": str(e), "redis_injection_vulnerable": True}
    
    def execute_elasticsearch_injection(self, index: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Elasticsearch NoSQL injection"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No query validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Elasticsearch injection on {index}: {query}")
            
            # VULNERABLE: Direct query execution without validation
            parsed_query = json.loads(query) if query.startswith('{') else {"query": {"match": {"_all": query}}}
            
            # VULNERABLE: Execute query without sanitization
            result = self._execute_elasticsearch_query(index, parsed_query)
            
            return {
                "success": True,
                "index": index,
                "query": query,
                "parsed_query": parsed_query,
                "result": result,
                "elasticsearch_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Elasticsearch injection error: {str(e)}")
            return {"error": str(e), "elasticsearch_injection_vulnerable": True}
    
    def execute_neo4j_injection(self, database: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Neo4j NoSQL injection"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No query validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Neo4j injection on {database}: {query}")
            
            # VULNERABLE: Direct query execution without validation
            result = self._execute_neo4j_query(database, query)
            
            return {
                "success": True,
                "database": database,
                "query": query,
                "result": result,
                "neo4j_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Neo4j injection error: {str(e)}")
            return {"error": str(e), "neo4j_injection_vulnerable": True}
    
    def execute_advanced_nosql_injection(self, db_type: str, payload: str) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced NoSQL injection techniques"""
        # VULNERABLE: Advanced NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No payload validation
        # VULNERABLE: No injection protection
        
        try:
            logger.info(f"VULNERABLE: Executing advanced NoSQL injection on {db_type}: {payload}")
            
            # VULNERABLE: Advanced injection techniques
            if db_type.lower() == "mongodb":
                # VULNERABLE: MongoDB advanced injection
                advanced_payloads = [
                    f"this.password.match(/{payload}/)",
                    f"this.username == '{payload}'",
                    f"this.role == '{payload}'",
                    f"this.email.indexOf('{payload}') > -1",
                    f"this.created > new Date('{payload}')",
                    f"this.status == '{payload}'"
                ]
                
                results = []
                for advanced_payload in advanced_payloads:
                    result = self._execute_mongodb_query("users", {"$where": advanced_payload})
                    results.append({
                        "payload": advanced_payload,
                        "result": result,
                        "injection_successful": True
                    })
                
                return {
                    "success": True,
                    "db_type": db_type,
                    "payload": payload,
                    "advanced_results": results,
                    "advanced_nosql_injection_vulnerable": True
                }
                
            elif db_type.lower() == "couchdb":
                # VULNERABLE: CouchDB advanced injection
                advanced_payloads = [
                    f"doc.password.match(/{payload}/)",
                    f"doc.username == '{payload}'",
                    f"doc.role == '{payload}'",
                    f"doc.email.indexOf('{payload}') > -1",
                    f"doc.created > '{payload}'",
                    f"doc.status == '{payload}'"
                ]
                
                results = []
                for advanced_payload in advanced_payloads:
                    result = self._execute_couchdb_query("users", {"selector": advanced_payload})
                    results.append({
                        "payload": advanced_payload,
                        "result": result,
                        "injection_successful": True
                    })
                
                return {
                    "success": True,
                    "db_type": db_type,
                    "payload": payload,
                    "advanced_results": results,
                    "advanced_nosql_injection_vulnerable": True
                }
                
            else:
                return {"error": "Unsupported database type"}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced NoSQL injection error: {str(e)}")
            return {"error": str(e), "advanced_nosql_injection_vulnerable": True}
    
    def execute_blind_nosql_injection(self, db_type: str, payload: str) -> Dict[str, Any]:
        """VULNERABLE: Execute blind NoSQL injection"""
        # VULNERABLE: Blind NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No blind injection protection
        # VULNERABLE: No timing analysis protection
        
        try:
            logger.info(f"VULNERABLE: Executing blind NoSQL injection on {db_type}: {payload}")
            
            start_time = time.time()
            
            # VULNERABLE: Blind injection techniques
            if db_type.lower() == "mongodb":
                # VULNERABLE: MongoDB blind injection
                blind_query = f"this.password.match(/{payload}/) && sleep(5000)"
                result = self._execute_mongodb_query("users", {"$where": blind_query})
                
            elif db_type.lower() == "couchdb":
                # VULNERABLE: CouchDB blind injection
                blind_query = f"doc.password.match(/{payload}/) && sleep(5000)"
                result = self._execute_couchdb_query("users", {"selector": blind_query})
                
            else:
                return {"error": "Unsupported database type"}
            
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            return {
                "success": True,
                "db_type": db_type,
                "payload": payload,
                "execution_time": execution_time,
                "blind_injection_successful": execution_time > 4000,
                "blind_nosql_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Blind NoSQL injection error: {str(e)}")
            return {"error": str(e), "blind_nosql_injection_vulnerable": True}
    
    def execute_error_based_nosql_injection(self, db_type: str, payload: str) -> Dict[str, Any]:
        """VULNERABLE: Execute error-based NoSQL injection"""
        # VULNERABLE: Error-based NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No error handling protection
        # VULNERABLE: No error message sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing error-based NoSQL injection on {db_type}: {payload}")
            
            # VULNERABLE: Error-based injection techniques
            if db_type.lower() == "mongodb":
                # VULNERABLE: MongoDB error-based injection
                error_query = f"this.password.match(/{payload}/) && this.password.toArray()[0]"
                try:
                    result = self._execute_mongodb_query("users", {"$where": error_query})
                    return {
                        "success": True,
                        "db_type": db_type,
                        "payload": payload,
                        "result": result,
                        "error_based_injection_successful": True,
                        "error_based_nosql_injection_vulnerable": True
                    }
                except Exception as error:
                    # VULNERABLE: Return error information that might leak data
                    return {
                        "success": False,
                        "db_type": db_type,
                        "payload": payload,
                        "error": str(error),
                        "error_message": str(error),
                        "error_based_injection_successful": True,
                        "leaked_data": str(error),
                        "error_based_nosql_injection_vulnerable": True
                    }
                    
            elif db_type.lower() == "couchdb":
                # VULNERABLE: CouchDB error-based injection
                error_query = f"doc.password.match(/{payload}/) && doc.password.toArray()[0]"
                try:
                    result = self._execute_couchdb_query("users", {"selector": error_query})
                    return {
                        "success": True,
                        "db_type": db_type,
                        "payload": payload,
                        "result": result,
                        "error_based_injection_successful": True,
                        "error_based_nosql_injection_vulnerable": True
                    }
                except Exception as error:
                    # VULNERABLE: Return error information that might leak data
                    return {
                        "success": False,
                        "db_type": db_type,
                        "payload": payload,
                        "error": str(error),
                        "error_message": str(error),
                        "error_based_injection_successful": True,
                        "leaked_data": str(error),
                        "error_based_nosql_injection_vulnerable": True
                    }
                    
            else:
                return {"error": "Unsupported database type"}
            
        except Exception as e:
            logger.error(f"VULNERABLE: Error-based NoSQL injection error: {str(e)}")
            return {"error": str(e), "error_based_nosql_injection_vulnerable": True}
    
    def _execute_mongodb_query(self, collection: str, query: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute MongoDB query without validation"""
        # VULNERABLE: No query validation
        # VULNERABLE: No result sanitization
        
        # Mock MongoDB query execution
        mock_data = [
            {"_id": "1", "username": "admin", "password": "admin123", "role": "admin"},
            {"_id": "2", "username": "user1", "password": "password123", "role": "user"},
            {"_id": "3", "username": "user2", "password": "secret456", "role": "user"}
        ]
        
        # VULNERABLE: Simple mock filtering
        if "$where" in query:
            # VULNERABLE: Execute JavaScript in $where clause
            return {"results": mock_data, "count": len(mock_data), "query_executed": True}
        else:
            return {"results": mock_data, "count": len(mock_data), "query_executed": True}
    
    def _execute_couchdb_query(self, database: str, query: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute CouchDB query without validation"""
        # VULNERABLE: No query validation
        # VULNERABLE: No result sanitization
        
        # Mock CouchDB query execution
        mock_data = [
            {"_id": "1", "username": "admin", "password": "admin123", "role": "admin"},
            {"_id": "2", "username": "user1", "password": "password123", "role": "user"},
            {"_id": "3", "username": "user2", "password": "secret456", "role": "user"}
        ]
        
        return {"docs": mock_data, "total_rows": len(mock_data), "query_executed": True}
    
    def _execute_cassandra_query(self, keyspace: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Cassandra query without validation"""
        # VULNERABLE: No query validation
        # VULNERABLE: No result sanitization
        
        # Mock Cassandra query execution
        mock_data = [
            {"id": "1", "username": "admin", "password": "admin123", "role": "admin"},
            {"id": "2", "username": "user1", "password": "password123", "role": "user"},
            {"id": "3", "username": "user2", "password": "secret456", "role": "user"}
        ]
        
        return {"rows": mock_data, "count": len(mock_data), "query_executed": True}
    
    def _execute_redis_command(self, key: str, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Redis command without validation"""
        # VULNERABLE: No command validation
        # VULNERABLE: No result sanitization
        
        # Mock Redis command execution
        mock_data = {
            "user:1": {"username": "admin", "password": "admin123", "role": "admin"},
            "user:2": {"username": "user1", "password": "password123", "role": "user"},
            "user:3": {"username": "user2", "password": "secret456", "role": "user"}
        }
        
        return {"result": mock_data.get(key, "Key not found"), "command_executed": True}
    
    def _execute_elasticsearch_query(self, index: str, query: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute Elasticsearch query without validation"""
        # VULNERABLE: No query validation
        # VULNERABLE: No result sanitization
        
        # Mock Elasticsearch query execution
        mock_data = {
            "hits": {
                "total": {"value": 3},
                "hits": [
                    {"_id": "1", "_source": {"username": "admin", "password": "admin123", "role": "admin"}},
                    {"_id": "2", "_source": {"username": "user1", "password": "password123", "role": "user"}},
                    {"_id": "3", "_source": {"username": "user2", "password": "secret456", "role": "user"}}
                ]
            }
        }
        
        return {"results": mock_data, "query_executed": True}
    
    def _execute_neo4j_query(self, database: str, query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Neo4j query without validation"""
        # VULNERABLE: No query validation
        # VULNERABLE: No result sanitization
        
        # Mock Neo4j query execution
        mock_data = {
            "results": [
                {"data": [{"row": ["admin", "admin123", "admin"]}]},
                {"data": [{"row": ["user1", "password123", "user"]}]},
                {"data": [{"row": ["user2", "secret456", "user"]}]}
            ]
        }
        
        return {"results": mock_data, "query_executed": True}
    
    def get_query_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get query history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.query_history
