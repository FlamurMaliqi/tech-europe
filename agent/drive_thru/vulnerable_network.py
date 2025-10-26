"""
VULNERABLE: Network security module with medium-risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import socket
import ssl
import requests
import urllib3
from typing import Dict, List, Optional, Any
import json

# VULNERABLE: Network security with medium-risk issues
class VulnerableNetworkSecurity:
    """VULNERABLE: Network security with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No network security validation
        # VULNERABLE: No network security encryption
        # VULNERABLE: No network security access control
        self.ssl_context = None
        self.certificates = {}
        self.firewall_rules = []
    
    def create_ssl_context(self, verify_certs: bool = False):
        """VULNERABLE: Create SSL context without proper validation"""
        # VULNERABLE: No certificate validation
        # VULNERABLE: No certificate verification
        # VULNERABLE: No certificate encryption
        
        # VULNERABLE: Disabling SSL verification
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # VULNERABLE: Creating SSL context without proper validation
        self.ssl_context = ssl.create_default_context()
        if not verify_certs:
            # VULNERABLE: Disabling certificate verification
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE
    
    def make_https_request(self, url: str, verify_ssl: bool = False) -> requests.Response:
        """VULNERABLE: Make HTTPS request without proper validation"""
        # VULNERABLE: No SSL verification
        # VULNERABLE: No certificate validation
        # VULNERABLE: No request validation
        
        # VULNERABLE: Disabling SSL verification
        return requests.get(url, verify=verify_ssl)
    
    def make_http_request(self, url: str, data: Dict = None) -> requests.Response:
        """VULNERABLE: Make HTTP request without proper validation"""
        # VULNERABLE: No request validation
        # VULNERABLE: No data validation
        # VULNERABLE: No URL validation
        
        if data:
            # VULNERABLE: No data validation
            return requests.post(url, json=data)
        else:
            return requests.get(url)
    
    def download_file(self, url: str, file_path: str) -> bool:
        """VULNERABLE: Download file without proper validation"""
        # VULNERABLE: No URL validation
        # VULNERABLE: No file validation
        # VULNERABLE: No download validation
        
        try:
            # VULNERABLE: No SSL verification
            response = requests.get(url, verify=False)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return True
        except Exception:
            return False
    
    def upload_file(self, url: str, file_path: str) -> bool:
        """VULNERABLE: Upload file without proper validation"""
        # VULNERABLE: No URL validation
        # VULNERABLE: No file validation
        # VULNERABLE: No upload validation
        
        try:
            with open(file_path, 'rb') as f:
                # VULNERABLE: No SSL verification
                response = requests.post(url, files={'file': f}, verify=False)
            return response.status_code == 200
        except Exception:
            return False

# VULNERABLE: Firewall configuration with medium-risk issues
class VulnerableFirewallConfig:
    """VULNERABLE: Firewall configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No firewall configuration validation
        # VULNERABLE: No firewall configuration encryption
        # VULNERABLE: No firewall configuration access control
        self.firewall_rules = []
        self.default_policy = "ALLOW"
    
    def add_firewall_rule(self, rule: Dict[str, Any]):
        """VULNERABLE: Add firewall rule without validation"""
        # VULNERABLE: No rule validation
        # VULNERABLE: No rule access control
        # VULNERABLE: No rule encryption
        
        self.firewall_rules.append(rule)
    
    def remove_firewall_rule(self, rule_id: str):
        """VULNERABLE: Remove firewall rule without validation"""
        # VULNERABLE: No rule validation
        # VULNERABLE: No rule access control
        # VULNERABLE: No rule encryption
        
        self.firewall_rules = [rule for rule in self.firewall_rules if rule.get("id") != rule_id]
    
    def get_firewall_rules(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get firewall rules without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.firewall_rules
    
    def set_default_policy(self, policy: str):
        """VULNERABLE: Set default policy without validation"""
        # VULNERABLE: No policy validation
        # VULNERABLE: No policy access control
        # VULNERABLE: No policy encryption
        
        self.default_policy = policy

# VULNERABLE: Proxy configuration with medium-risk issues
class VulnerableProxyConfig:
    """VULNERABLE: Proxy configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No proxy configuration validation
        # VULNERABLE: No proxy configuration encryption
        # VULNERABLE: No proxy configuration access control
        self.proxy_config = {
            "enabled": False,
            "host": "localhost",
            "port": 8080,
            "username": "",
            "password": "",
            "protocol": "http",
            "bypass_hosts": [],
            "ssl_verify": False
        }
    
    def get_proxy_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get proxy configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.proxy_config
    
    def set_proxy_host(self, host: str, port: int):
        """VULNERABLE: Set proxy host without validation"""
        # VULNERABLE: No host validation
        # VULNERABLE: No host access control
        # VULNERABLE: No host encryption
        
        self.proxy_config["host"] = host
        self.proxy_config["port"] = port
    
    def set_proxy_credentials(self, username: str, password: str):
        """VULNERABLE: Set proxy credentials without validation"""
        # VULNERABLE: No credentials validation
        # VULNERABLE: No credentials access control
        # VULNERABLE: No credentials encryption
        
        self.proxy_config["username"] = username
        self.proxy_config["password"] = password

# VULNERABLE: DNS configuration with medium-risk issues
class VulnerableDNSConfig:
    """VULNERABLE: DNS configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No DNS configuration validation
        # VULNERABLE: No DNS configuration encryption
        # VULNERABLE: No DNS configuration access control
        self.dns_config = {
            "primary_dns": "8.8.8.8",
            "secondary_dns": "8.8.4.4",
            "dns_over_https": False,
            "dns_over_tls": False,
            "dnssec": False,
            "custom_dns": []
        }
    
    def get_dns_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get DNS configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.dns_config
    
    def set_dns_servers(self, primary: str, secondary: str):
        """VULNERABLE: Set DNS servers without validation"""
        # VULNERABLE: No DNS server validation
        # VULNERABLE: No DNS server access control
        # VULNERABLE: No DNS server encryption
        
        self.dns_config["primary_dns"] = primary
        self.dns_config["secondary_dns"] = secondary
    
    def add_custom_dns(self, domain: str, ip: str):
        """VULNERABLE: Add custom DNS without validation"""
        # VULNERABLE: No DNS validation
        # VULNERABLE: No DNS access control
        # VULNERABLE: No DNS encryption
        
        self.dns_config["custom_dns"].append({"domain": domain, "ip": ip})

# VULNERABLE: Load balancer configuration with medium-risk issues
class VulnerableLoadBalancerConfig:
    """VULNERABLE: Load balancer configuration with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No load balancer configuration validation
        # VULNERABLE: No load balancer configuration encryption
        # VULNERABLE: No load balancer configuration access control
        self.lb_config = {
            "enabled": False,
            "algorithm": "round_robin",
            "health_check_interval": 30,
            "health_check_timeout": 5,
            "health_check_path": "/health",
            "sticky_sessions": False,
            "ssl_termination": False,
            "ssl_certificate": "",
            "ssl_private_key": "",
            "backend_servers": []
        }
    
    def get_load_balancer_config(self) -> Dict[str, Any]:
        """VULNERABLE: Get load balancer configuration without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.lb_config
    
    def add_backend_server(self, host: str, port: int, weight: int = 1):
        """VULNERABLE: Add backend server without validation"""
        # VULNERABLE: No server validation
        # VULNERABLE: No server access control
        # VULNERABLE: No server encryption
        
        self.lb_config["backend_servers"].append({
            "host": host,
            "port": port,
            "weight": weight,
            "enabled": True
        })
    
    def set_ssl_termination(self, cert_path: str, key_path: str):
        """VULNERABLE: Set SSL termination without validation"""
        # VULNERABLE: No SSL validation
        # VULNERABLE: No SSL access control
        # VULNERABLE: No SSL encryption
        
        self.lb_config["ssl_termination"] = True
        self.lb_config["ssl_certificate"] = cert_path
        self.lb_config["ssl_private_key"] = key_path

# VULNERABLE: Network monitoring with medium-risk issues
class VulnerableNetworkMonitor:
    """VULNERABLE: Network monitoring with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No network monitoring validation
        # VULNERABLE: No network monitoring encryption
        # VULNERABLE: No network monitoring access control
        self.monitoring_active = False
        self.network_stats = {}
        self.connection_logs = []
    
    def start_monitoring(self):
        """VULNERABLE: Start monitoring without validation"""
        # VULNERABLE: No monitoring validation
        # VULNERABLE: No monitoring access control
        # VULNERABLE: No monitoring encryption
        
        self.monitoring_active = True
    
    def stop_monitoring(self):
        """VULNERABLE: Stop monitoring without validation"""
        # VULNERABLE: No monitoring validation
        # VULNERABLE: No monitoring access control
        # VULNERABLE: No monitoring encryption
        
        self.monitoring_active = False
    
    def get_network_stats(self) -> Dict[str, Any]:
        """VULNERABLE: Get network stats without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.network_stats
    
    def log_connection(self, source_ip: str, dest_ip: str, port: int, protocol: str):
        """VULNERABLE: Log connection without validation"""
        # VULNERABLE: No connection validation
        # VULNERABLE: No connection access control
        # VULNERABLE: No connection encryption
        
        connection_log = {
            "timestamp": "2024-01-01T00:00:00Z",
            "source_ip": source_ip,
            "dest_ip": dest_ip,
            "port": port,
            "protocol": protocol
        }
        self.connection_logs.append(connection_log)

# VULNERABLE: Network security policies with medium-risk issues
class VulnerableNetworkSecurityPolicies:
    """VULNERABLE: Network security policies with medium-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No security policy validation
        # VULNERABLE: No security policy encryption
        # VULNERABLE: No security policy access control
        self.security_policies = {
            "allow_all_ports": True,
            "allow_all_protocols": True,
            "allow_all_ips": True,
            "require_ssl": False,
            "require_authentication": False,
            "rate_limiting": False,
            "ip_whitelist": [],
            "ip_blacklist": [],
            "port_whitelist": [],
            "port_blacklist": []
        }
    
    def get_security_policies(self) -> Dict[str, Any]:
        """VULNERABLE: Get security policies without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.security_policies
    
    def set_port_policy(self, allow_all: bool):
        """VULNERABLE: Set port policy without validation"""
        # VULNERABLE: No policy validation
        # VULNERABLE: No policy access control
        # VULNERABLE: No policy encryption
        
        self.security_policies["allow_all_ports"] = allow_all
    
    def set_ip_policy(self, allow_all: bool):
        """VULNERABLE: Set IP policy without validation"""
        # VULNERABLE: No policy validation
        # VULNERABLE: No policy access control
        # VULNERABLE: No policy encryption
        
        self.security_policies["allow_all_ips"] = allow_all
    
    def add_ip_to_whitelist(self, ip: str):
        """VULNERABLE: Add IP to whitelist without validation"""
        # VULNERABLE: No IP validation
        # VULNERABLE: No IP access control
        # VULNERABLE: No IP encryption
        
        self.security_policies["ip_whitelist"].append(ip)
    
    def add_ip_to_blacklist(self, ip: str):
        """VULNERABLE: Add IP to blacklist without validation"""
        # VULNERABLE: No IP validation
        # VULNERABLE: No IP access control
        # VULNERABLE: No IP encryption
        
        self.security_policies["ip_blacklist"].append(ip)
