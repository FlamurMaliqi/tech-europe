"""
VULNERABLE: Advanced Remote Code Execution vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import subprocess
import os
import sys
import importlib
import exec
import eval
import compile
import pickle
import marshal
import logging
from typing import Dict, List, Optional, Any
import tempfile
import shutil
import time

logger = logging.getLogger(__name__)

# VULNERABLE: Advanced RCE vulnerabilities
class VulnerableAdvancedRCE:
    """VULNERABLE: Advanced Remote Code Execution vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No RCE protection
        # VULNERABLE: No command validation
        # VULNERABLE: No code execution restrictions
        self.execution_history = []
        self.temp_files = []
        self.imported_modules = []
    
    def execute_shell_command(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute shell command without validation"""
        # VULNERABLE: Command injection vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No shell escaping
        
        try:
            logger.info(f"VULNERABLE: Executing shell command: {command}")
            
            # VULNERABLE: Direct shell execution
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            execution_info = {
                "command": command,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "timestamp": time.time()
            }
            
            self.execution_history.append(execution_info)
            
            return {
                "success": True,
                "command": command,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "rce_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Shell command execution error: {str(e)}")
            return {"error": str(e), "rce_vulnerable": True}
    
    def execute_python_code(self, code: str) -> Dict[str, Any]:
        """VULNERABLE: Execute Python code without validation"""
        # VULNERABLE: Code execution vulnerability - CRITICAL
        # VULNERABLE: No code validation
        # VULNERABLE: No execution restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing Python code: {code[:100]}...")
            
            # VULNERABLE: Direct code execution
            exec_globals = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
            }
            
            exec_locals = {}
            
            # VULNERABLE: Execute code with full builtins access
            exec(code, exec_globals, exec_locals)
            
            return {
                "success": True,
                "code": code,
                "locals": exec_locals,
                "globals": {k: v for k, v in exec_globals.items() if not k.startswith('__')},
                "rce_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Python code execution error: {str(e)}")
            return {"error": str(e), "rce_vulnerable": True}
    
    def execute_eval_expression(self, expression: str) -> Dict[str, Any]:
        """VULNERABLE: Execute eval expression without validation"""
        # VULNERABLE: Eval vulnerability - CRITICAL
        # VULNERABLE: No expression validation
        # VULNERABLE: No eval restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing eval expression: {expression}")
            
            # VULNERABLE: Direct eval execution
            result = eval(expression)
            
            return {
                "success": True,
                "expression": expression,
                "result": result,
                "eval_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Eval execution error: {str(e)}")
            return {"error": str(e), "eval_vulnerable": True}
    
    def execute_compile_code(self, code: str, filename: str = "<string>") -> Dict[str, Any]:
        """VULNERABLE: Execute compiled code without validation"""
        # VULNERABLE: Compile vulnerability - CRITICAL
        # VULNERABLE: No code validation
        # VULNERABLE: No compile restrictions
        
        try:
            logger.info(f"VULNERABLE: Compiling and executing code: {code[:100]}...")
            
            # VULNERABLE: Compile code
            compiled_code = compile(code, filename, 'exec')
            
            # VULNERABLE: Execute compiled code
            exec_globals = {'__builtins__': __builtins__}
            exec_locals = {}
            
            exec(compiled_code, exec_globals, exec_locals)
            
            return {
                "success": True,
                "code": code,
                "filename": filename,
                "compiled": True,
                "locals": exec_locals,
                "compile_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Compile execution error: {str(e)}")
            return {"error": str(e), "compile_vulnerable": True}
    
    def execute_pickle_deserialization(self, pickle_data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Execute pickle deserialization without validation"""
        # VULNERABLE: Pickle deserialization vulnerability - CRITICAL
        # VULNERABLE: No pickle validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing pickle deserialization: {len(pickle_data)} bytes")
            
            # VULNERABLE: Direct pickle deserialization
            result = pickle.loads(pickle_data)
            
            return {
                "success": True,
                "pickle_data": pickle_data,
                "deserialized": result,
                "pickle_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Pickle deserialization error: {str(e)}")
            return {"error": str(e), "pickle_vulnerable": True}
    
    def execute_marshal_deserialization(self, marshal_data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Execute marshal deserialization without validation"""
        # VULNERABLE: Marshal deserialization vulnerability - CRITICAL
        # VULNERABLE: No marshal validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing marshal deserialization: {len(marshal_data)} bytes")
            
            # VULNERABLE: Direct marshal deserialization
            result = marshal.loads(marshal_data)
            
            return {
                "success": True,
                "marshal_data": marshal_data,
                "deserialized": result,
                "marshal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Marshal deserialization error: {str(e)}")
            return {"error": str(e), "marshal_vulnerable": True}
    
    def execute_dynamic_import(self, module_name: str) -> Dict[str, Any]:
        """VULNERABLE: Execute dynamic module import without validation"""
        # VULNERABLE: Dynamic import vulnerability - CRITICAL
        # VULNERABLE: No module validation
        # VULNERABLE: No import restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing dynamic import: {module_name}")
            
            # VULNERABLE: Direct dynamic import
            module = importlib.import_module(module_name)
            
            self.imported_modules.append(module_name)
            
            return {
                "success": True,
                "module_name": module_name,
                "module": str(module),
                "module_attributes": dir(module),
                "dynamic_import_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Dynamic import error: {str(e)}")
            return {"error": str(e), "dynamic_import_vulnerable": True}
    
    def execute_file_operations(self, operation: str, file_path: str, content: str = "") -> Dict[str, Any]:
        """VULNERABLE: Execute file operations without validation"""
        # VULNERABLE: File operation vulnerability - CRITICAL
        # VULNERABLE: No file path validation
        # VULNERABLE: No operation restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing file operation: {operation} on {file_path}")
            
            if operation == "read":
                # VULNERABLE: Read any file
                with open(file_path, 'r') as f:
                    content = f.read()
                result = {"content": content}
                
            elif operation == "write":
                # VULNERABLE: Write to any file
                with open(file_path, 'w') as f:
                    f.write(content)
                result = {"written": True}
                
            elif operation == "delete":
                # VULNERABLE: Delete any file
                os.remove(file_path)
                result = {"deleted": True}
                
            elif operation == "execute":
                # VULNERABLE: Execute any file
                result = subprocess.run([file_path], capture_output=True, text=True)
                result = {
                    "returncode": result.returncode,
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
                
            else:
                return {"error": "Unsupported operation"}
            
            return {
                "success": True,
                "operation": operation,
                "file_path": file_path,
                "result": result,
                "file_operation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File operation error: {str(e)}")
            return {"error": str(e), "file_operation_vulnerable": True}
    
    def execute_network_operations(self, host: str, port: int, data: str = "") -> Dict[str, Any]:
        """VULNERABLE: Execute network operations without validation"""
        # VULNERABLE: Network operation vulnerability - CRITICAL
        # VULNERABLE: No network validation
        # VULNERABLE: No network restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing network operation to {host}:{port}")
            
            import socket
            
            # VULNERABLE: Create socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            # VULNERABLE: Connect to any host/port
            sock.connect((host, port))
            
            if data:
                # VULNERABLE: Send data
                sock.send(data.encode())
            
            # VULNERABLE: Receive response
            response = sock.recv(1024).decode()
            
            sock.close()
            
            return {
                "success": True,
                "host": host,
                "port": port,
                "data_sent": data,
                "response": response,
                "network_operation_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Network operation error: {str(e)}")
            return {"error": str(e), "network_operation_vulnerable": True}
    
    def execute_system_commands(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute system commands without validation"""
        # VULNERABLE: System command vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No system restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing system command: {command}")
            
            # VULNERABLE: Execute system command
            result = os.system(command)
            
            return {
                "success": True,
                "command": command,
                "return_code": result,
                "system_command_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: System command error: {str(e)}")
            return {"error": str(e), "system_command_vulnerable": True}
    
    def execute_popen_command(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute popen command without validation"""
        # VULNERABLE: Popen vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No popen restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing popen command: {command}")
            
            # VULNERABLE: Execute popen command
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            return {
                "success": True,
                "command": command,
                "return_code": process.returncode,
                "stdout": stdout,
                "stderr": stderr,
                "popen_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Popen command error: {str(e)}")
            return {"error": str(e), "popen_vulnerable": True}
    
    def execute_template_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute template injection without validation"""
        # VULNERABLE: Template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No template restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing template injection: {template[:100]}...")
            
            # VULNERABLE: Simple template engine
            result = template.format(**context)
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "result": result,
                "template_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Template injection error: {str(e)}")
            return {"error": str(e), "template_injection_vulnerable": True}
    
    def execute_ldap_injection(self, ldap_query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute LDAP injection without validation"""
        # VULNERABLE: LDAP injection vulnerability - CRITICAL
        # VULNERABLE: No LDAP validation
        # VULNERABLE: No LDAP restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing LDAP injection: {ldap_query}")
            
            # VULNERABLE: Mock LDAP query execution
            # In real scenario, this would connect to LDAP server
            result = f"LDAP query executed: {ldap_query}"
            
            return {
                "success": True,
                "ldap_query": ldap_query,
                "result": result,
                "ldap_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: LDAP injection error: {str(e)}")
            return {"error": str(e), "ldap_injection_vulnerable": True}
    
    def execute_nosql_injection(self, nosql_query: str) -> Dict[str, Any]:
        """VULNERABLE: Execute NoSQL injection without validation"""
        # VULNERABLE: NoSQL injection vulnerability - CRITICAL
        # VULNERABLE: No NoSQL validation
        # VULNERABLE: No NoSQL restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing NoSQL injection: {nosql_query}")
            
            # VULNERABLE: Mock NoSQL query execution
            # In real scenario, this would connect to NoSQL database
            result = f"NoSQL query executed: {nosql_query}"
            
            return {
                "success": True,
                "nosql_query": nosql_query,
                "result": result,
                "nosql_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: NoSQL injection error: {str(e)}")
            return {"error": str(e), "nosql_injection_vulnerable": True}
    
    def execute_advanced_payload(self, payload: str) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced payload without validation"""
        # VULNERABLE: Advanced payload vulnerability - CRITICAL
        # VULNERABLE: No payload validation
        # VULNERABLE: No payload restrictions
        
        try:
            logger.info(f"VULNERABLE: Executing advanced payload: {payload[:100]}...")
            
            # VULNERABLE: Execute various advanced payloads
            if payload.startswith("python:"):
                # VULNERABLE: Python code execution
                code = payload[7:]  # Remove "python:" prefix
                exec(code)
                result = "Python code executed"
                
            elif payload.startswith("shell:"):
                # VULNERABLE: Shell command execution
                command = payload[6:]  # Remove "shell:" prefix
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                result = result.stdout
                
            elif payload.startswith("eval:"):
                # VULNERABLE: Eval expression execution
                expression = payload[5:]  # Remove "eval:" prefix
                result = eval(expression)
                
            else:
                # VULNERABLE: Direct execution
                exec(payload)
                result = "Payload executed"
            
            return {
                "success": True,
                "payload": payload,
                "result": result,
                "advanced_payload_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced payload error: {str(e)}")
            return {"error": str(e), "advanced_payload_vulnerable": True}
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get execution history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.execution_history
