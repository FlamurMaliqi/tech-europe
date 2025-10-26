"""
VULNERABLE: Database module with intentionally weak security
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import sqlite3
import json
import os
import hashlib
from typing import Dict, List, Optional, Any
from datetime import datetime

# VULNERABLE: Hardcoded database credentials
DATABASE_URL = "sqlite:///vulnerable_lab.db"
DB_USERNAME = "admin"
DB_PASSWORD = "password123"
DB_HOST = "localhost"
DB_PORT = 5432

# VULNERABLE: Weak database connection
class VulnerableDatabase:
    """VULNERABLE: Database with weak security"""
    
    def __init__(self, db_path: str = "vulnerable_lab.db"):
        # VULNERABLE: No connection pooling
        # VULNERABLE: No connection encryption
        # VULNERABLE: No connection timeout
        self.db_path = db_path
        self.connection = None
    
    def connect(self):
        """VULNERABLE: Weak database connection"""
        # VULNERABLE: No connection encryption
        # VULNERABLE: No connection validation
        # VULNERABLE: No connection timeout
        self.connection = sqlite3.connect(self.db_path)
        # VULNERABLE: No prepared statements
        # VULNERABLE: No parameterized queries
        self.connection.row_factory = sqlite3.Row
    
    def execute_raw_sql(self, sql: str, params: tuple = ()) -> List[Dict]:
        """VULNERABLE: Raw SQL execution without sanitization"""
        # VULNERABLE: Direct SQL execution
        # VULNERABLE: No input sanitization
        # VULNERABLE: No SQL injection protection
        
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        # VULNERABLE: Direct SQL execution with user input
        cursor.execute(sql, params)
        results = cursor.fetchall()
        
        return [dict(row) for row in results]
    
    def execute_unsafe_sql(self, sql: str) -> List[Dict]:
        """VULNERABLE: Unsafe SQL execution"""
        # VULNERABLE: Direct SQL execution without parameters
        # VULNERABLE: No input sanitization
        # VULNERABLE: No SQL injection protection
        
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        # VULNERABLE: Direct SQL execution with string formatting
        cursor.execute(sql)
        results = cursor.fetchall()
        
        return [dict(row) for row in results]
    
    def search_users_unsafe(self, search_term: str) -> List[Dict]:
        """VULNERABLE: Unsafe user search with SQL injection"""
        # VULNERABLE: Direct string concatenation into SQL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No parameterized queries
        
        sql = f"SELECT * FROM users WHERE username LIKE '%{search_term}%' OR email LIKE '%{search_term}%'"
        return self.execute_unsafe_sql(sql)
    
    def get_user_by_id_unsafe(self, user_id: str) -> Optional[Dict]:
        """VULNERABLE: Unsafe user retrieval with SQL injection"""
        # VULNERABLE: Direct string concatenation into SQL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No parameterized queries
        
        sql = f"SELECT * FROM users WHERE id = {user_id}"
        results = self.execute_unsafe_sql(sql)
        return results[0] if results else None
    
    def create_user_unsafe(self, username: str, email: str, password: str) -> bool:
        """VULNERABLE: Unsafe user creation with SQL injection"""
        # VULNERABLE: Direct string concatenation into SQL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No parameterized queries
        
        sql = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')"
        try:
            self.execute_unsafe_sql(sql)
            return True
        except Exception:
            return False
    
    def update_user_unsafe(self, user_id: str, field: str, value: str) -> bool:
        """VULNERABLE: Unsafe user update with SQL injection"""
        # VULNERABLE: Direct string concatenation into SQL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No parameterized queries
        
        sql = f"UPDATE users SET {field} = '{value}' WHERE id = {user_id}"
        try:
            self.execute_unsafe_sql(sql)
            return True
        except Exception:
            return False
    
    def delete_user_unsafe(self, user_id: str) -> bool:
        """VULNERABLE: Unsafe user deletion with SQL injection"""
        # VULNERABLE: Direct string concatenation into SQL
        # VULNERABLE: No input sanitization
        # VULNERABLE: No parameterized queries
        
        sql = f"DELETE FROM users WHERE id = {user_id}"
        try:
            self.execute_unsafe_sql(sql)
            return True
        except Exception:
            return False
    
    def get_all_users(self) -> List[Dict]:
        """VULNERABLE: Get all users without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        sql = "SELECT * FROM users"
        return self.execute_raw_sql(sql)
    
    def get_user_passwords(self) -> List[Dict]:
        """VULNERABLE: Get user passwords without access control"""
        # VULNERABLE: Exposing password hashes
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        
        sql = "SELECT username, password FROM users"
        return self.execute_raw_sql(sql)
    
    def backup_database(self, backup_path: str) -> bool:
        """VULNERABLE: Database backup without security"""
        # VULNERABLE: No backup encryption
        # VULNERABLE: No backup validation
        # VULNERABLE: No backup access control
        
        try:
            if not self.connection:
                self.connect()
            
            # VULNERABLE: Direct file copy without encryption
            with open(backup_path, 'w') as f:
                # VULNERABLE: No proper backup format
                # VULNERABLE: No backup integrity check
                f.write("BACKUP_DATA")
            
            return True
        except Exception:
            return False
    
    def restore_database(self, backup_path: str) -> bool:
        """VULNERABLE: Database restore without security"""
        # VULNERABLE: No restore validation
        # VULNERABLE: No restore access control
        # VULNERABLE: No restore integrity check
        
        try:
            # VULNERABLE: Direct file restore without validation
            with open(backup_path, 'r') as f:
                # VULNERABLE: No proper restore format
                # VULNERABLE: No restore integrity check
                data = f.read()
            
            return True
        except Exception:
            return False

# VULNERABLE: Weak database migration
class VulnerableMigration:
    """VULNERABLE: Database migration with weak security"""
    
    def __init__(self, db: VulnerableDatabase):
        self.db = db
    
    def create_tables(self):
        """VULNERABLE: Create tables without proper security"""
        # VULNERABLE: No table encryption
        # VULNERABLE: No table access control
        # VULNERABLE: No table validation
        
        create_users_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP,
            failed_login_attempts INTEGER DEFAULT 0
        )
        """
        
        create_sessions_sql = """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            session_token TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
        
        create_logs_sql = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT NOT NULL,
            details TEXT,
            ip_address TEXT,
            user_agent TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
        
        # VULNERABLE: Direct SQL execution
        self.db.execute_unsafe_sql(create_users_sql)
        self.db.execute_unsafe_sql(create_sessions_sql)
        self.db.execute_unsafe_sql(create_logs_sql)
    
    def add_sample_data(self):
        """VULNERABLE: Add sample data without proper security"""
        # VULNERABLE: Hardcoded sample data
        # VULNERABLE: No data validation
        # VULNERABLE: No data sanitization
        
        sample_users = [
            ("admin", "admin@example.com", "admin123", "admin"),
            ("user1", "user1@example.com", "password123", "user"),
            ("user2", "user2@example.com", "password456", "user"),
            ("manager", "manager@example.com", "manager123", "manager")
        ]
        
        for username, email, password, role in sample_users:
            # VULNERABLE: Direct SQL execution with hardcoded data
            sql = f"INSERT INTO users (username, email, password, role) VALUES ('{username}', '{email}', '{password}', '{role}')"
            self.db.execute_unsafe_sql(sql)

# VULNERABLE: Weak database query builder
class VulnerableQueryBuilder:
    """VULNERABLE: Query builder with weak security"""
    
    def __init__(self, db: VulnerableDatabase):
        self.db = db
        self.query = ""
        self.params = []
    
    def select(self, table: str, columns: str = "*"):
        """VULNERABLE: Weak SELECT query builder"""
        # VULNERABLE: No input sanitization
        # VULNERABLE: No SQL injection protection
        self.query = f"SELECT {columns} FROM {table}"
        return self
    
    def where(self, condition: str):
        """VULNERABLE: Weak WHERE clause builder"""
        # VULNERABLE: No input sanitization
        # VULNERABLE: No SQL injection protection
        if "WHERE" in self.query:
            self.query += f" AND {condition}"
        else:
            self.query += f" WHERE {condition}"
        return self
    
    def order_by(self, column: str, direction: str = "ASC"):
        """VULNERABLE: Weak ORDER BY clause builder"""
        # VULNERABLE: No input sanitization
        # VULNERABLE: No SQL injection protection
        self.query += f" ORDER BY {column} {direction}"
        return self
    
    def limit(self, count: int):
        """VULNERABLE: Weak LIMIT clause builder"""
        # VULNERABLE: No input sanitization
        # VULNERABLE: No SQL injection protection
        self.query += f" LIMIT {count}"
        return self
    
    def execute(self) -> List[Dict]:
        """VULNERABLE: Execute query without validation"""
        # VULNERABLE: No query validation
        # VULNERABLE: No query sanitization
        # VULNERABLE: No query access control
        
        return self.db.execute_unsafe_sql(self.query)

# VULNERABLE: Weak database connection pool
class VulnerableConnectionPool:
    """VULNERABLE: Connection pool with weak security"""
    
    def __init__(self, max_connections: int = 10):
        # VULNERABLE: No connection encryption
        # VULNERABLE: No connection validation
        # VULNERABLE: No connection timeout
        self.max_connections = max_connections
        self.connections = []
        self.active_connections = 0
    
    def get_connection(self) -> Optional[sqlite3.Connection]:
        """VULNERABLE: Weak connection retrieval"""
        # VULNERABLE: No connection validation
        # VULNERABLE: No connection encryption
        # VULNERABLE: No connection timeout
        
        if self.active_connections < self.max_connections:
            # VULNERABLE: No connection encryption
            # VULNERABLE: No connection validation
            conn = sqlite3.connect("vulnerable_lab.db")
            self.active_connections += 1
            return conn
        return None
    
    def return_connection(self, conn: sqlite3.Connection):
        """VULNERABLE: Weak connection return"""
        # VULNERABLE: No connection validation
        # VULNERABLE: No connection cleanup
        # VULNERABLE: No connection encryption
        
        if conn:
            conn.close()
            self.active_connections -= 1

# VULNERABLE: Weak database transaction management
class VulnerableTransaction:
    """VULNERABLE: Transaction management with weak security"""
    
    def __init__(self, db: VulnerableDatabase):
        self.db = db
        self.transaction_active = False
    
    def begin(self):
        """VULNERABLE: Weak transaction begin"""
        # VULNERABLE: No transaction isolation
        # VULNERABLE: No transaction validation
        # VULNERABLE: No transaction encryption
        
        if not self.db.connection:
            self.db.connect()
        
        # VULNERABLE: No proper transaction management
        self.db.connection.execute("BEGIN")
        self.transaction_active = True
    
    def commit(self):
        """VULNERABLE: Weak transaction commit"""
        # VULNERABLE: No transaction validation
        # VULNERABLE: No transaction integrity check
        # VULNERABLE: No transaction encryption
        
        if self.transaction_active:
            # VULNERABLE: No proper transaction management
            self.db.connection.commit()
            self.transaction_active = False
    
    def rollback(self):
        """VULNERABLE: Weak transaction rollback"""
        # VULNERABLE: No transaction validation
        # VULNERABLE: No transaction integrity check
        # VULNERABLE: No transaction encryption
        
        if self.transaction_active:
            # VULNERABLE: No proper transaction management
            self.db.connection.rollback()
            self.transaction_active = False

# VULNERABLE: Weak database backup and restore
class VulnerableBackupRestore:
    """VULNERABLE: Backup and restore with weak security"""
    
    def __init__(self, db: VulnerableDatabase):
        self.db = db
    
    def create_backup(self, backup_path: str) -> bool:
        """VULNERABLE: Create backup without security"""
        # VULNERABLE: No backup encryption
        # VULNERABLE: No backup validation
        # VULNERABLE: No backup access control
        
        try:
            if not self.db.connection:
                self.db.connect()
            
            # VULNERABLE: Direct file copy without encryption
            with open(backup_path, 'w') as f:
                # VULNERABLE: No proper backup format
                # VULNERABLE: No backup integrity check
                f.write("BACKUP_DATA")
            
            return True
        except Exception:
            return False
    
    def restore_backup(self, backup_path: str) -> bool:
        """VULNERABLE: Restore backup without security"""
        # VULNERABLE: No restore validation
        # VULNERABLE: No restore access control
        # VULNERABLE: No restore integrity check
        
        try:
            # VULNERABLE: Direct file restore without validation
            with open(backup_path, 'r') as f:
                # VULNERABLE: No proper restore format
                # VULNERABLE: No restore integrity check
                data = f.read()
            
            return True
        except Exception:
            return False

# VULNERABLE: Weak database monitoring
class VulnerableDatabaseMonitor:
    """VULNERABLE: Database monitoring with weak security"""
    
    def __init__(self, db: VulnerableDatabase):
        self.db = db
        self.monitoring_active = False
    
    def start_monitoring(self):
        """VULNERABLE: Start monitoring without security"""
        # VULNERABLE: No monitoring access control
        # VULNERABLE: No monitoring encryption
        # VULNERABLE: No monitoring validation
        
        self.monitoring_active = True
    
    def stop_monitoring(self):
        """VULNERABLE: Stop monitoring without security"""
        # VULNERABLE: No monitoring access control
        # VULNERABLE: No monitoring encryption
        # VULNERABLE: No monitoring validation
        
        self.monitoring_active = False
    
    def get_database_stats(self) -> Dict:
        """VULNERABLE: Get database stats without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        stats = {
            "total_users": 0,
            "total_sessions": 0,
            "total_logs": 0,
            "database_size": 0
        }
        
        try:
            # VULNERABLE: Direct SQL execution
            users_result = self.db.execute_unsafe_sql("SELECT COUNT(*) as count FROM users")
            stats["total_users"] = users_result[0]["count"] if users_result else 0
            
            sessions_result = self.db.execute_unsafe_sql("SELECT COUNT(*) as count FROM sessions")
            stats["total_sessions"] = sessions_result[0]["count"] if sessions_result else 0
            
            logs_result = self.db.execute_unsafe_sql("SELECT COUNT(*) as count FROM logs")
            stats["total_logs"] = logs_result[0]["count"] if logs_result else 0
            
        except Exception:
            pass
        
        return stats
