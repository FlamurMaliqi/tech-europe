"""
VULNERABLE: SSRF (Server-Side Request Forgery) vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import requests
import urllib.request
import urllib.parse
import socket
import subprocess
import logging
from typing import Dict, List, Optional, Any
import json
import time

logger = logging.getLogger(__name__)

# VULNERABLE: SSRF vulnerabilities
class VulnerableSSRF:
    """VULNERABLE: Server-Side Request Forgery vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No SSRF protection
        # VULNERABLE: No URL validation
        # VULNERABLE: No network restrictions
        self.request_history = []
        self.internal_services = [
            "127.0.0.1",
            "localhost",
            "0.0.0.0",
            "10.0.0.0/8",
            "172.16.0.0/12",
            "192.168.0.0/16"
        ]
        self.protected_endpoints = [
            "/admin",
            "/internal",
            "/api/internal"
        ]
    
    def make_unrestricted_request(self, url: str) -> Dict[str, Any]:
        """VULNERABLE: Make unrestricted HTTP request"""
        # VULNERABLE: SSRF vulnerability - CRITICAL
        # VULNERABLE: No URL validation
        # VULNERABLE: No network restrictions
        
        try:
            logger.info(f"VULNERABLE: Making unrestricted request to: {url}")
            
            # VULNERABLE: Direct request without validation
            response = requests.get(url, timeout=10)
            
            # VULNERABLE: Log request details
            request_info = {
                "url": url,
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content": response.text[:1000],  # VULNERABLE: Log response content
                "timestamp": time.time()
            }
            
            self.request_history.append(request_info)
            
            return {
                "success": True,
                "url": url,
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content": response.text,
                "ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: SSRF request error: {str(e)}")
            return {"error": str(e), "ssrf_vulnerable": True}
    
    def make_internal_request(self, endpoint: str) -> Dict[str, Any]:
        """VULNERABLE: Make request to internal services"""
        # VULNERABLE: Internal SSRF vulnerability - CRITICAL
        # VULNERABLE: No internal service protection
        # VULNERABLE: No endpoint validation
        
        try:
            # VULNERABLE: Construct internal URL
            internal_url = f"http://127.0.0.1:8080{endpoint}"
            
            logger.info(f"VULNERABLE: Making internal request to: {internal_url}")
            
            # VULNERABLE: Direct internal request
            response = requests.get(internal_url, timeout=5)
            
            return {
                "success": True,
                "internal_url": internal_url,
                "status_code": response.status_code,
                "content": response.text,
                "internal_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Internal SSRF error: {str(e)}")
            return {"error": str(e), "internal_ssrf_vulnerable": True}
    
    def make_cloud_metadata_request(self, cloud_provider: str, metadata_path: str) -> Dict[str, Any]:
        """VULNERABLE: Make request to cloud metadata services"""
        # VULNERABLE: Cloud metadata SSRF vulnerability - CRITICAL
        # VULNERABLE: No cloud metadata protection
        # VULNERABLE: No metadata path validation
        
        try:
            # VULNERABLE: Cloud metadata URLs
            metadata_urls = {
                "aws": f"http://169.254.169.254/latest/{metadata_path}",
                "gcp": f"http://metadata.google.internal/computeMetadata/v1/{metadata_path}",
                "azure": f"http://169.254.169.254/metadata/{metadata_path}",
                "digitalocean": f"http://169.254.169.254/metadata/v1/{metadata_path}"
            }
            
            if cloud_provider not in metadata_urls:
                return {"error": "Unsupported cloud provider"}
            
            metadata_url = metadata_urls[cloud_provider]
            
            logger.info(f"VULNERABLE: Making cloud metadata request to: {metadata_url}")
            
            # VULNERABLE: Direct cloud metadata request
            response = requests.get(metadata_url, timeout=5)
            
            return {
                "success": True,
                "cloud_provider": cloud_provider,
                "metadata_url": metadata_url,
                "status_code": response.status_code,
                "metadata": response.text,
                "cloud_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Cloud metadata SSRF error: {str(e)}")
            return {"error": str(e), "cloud_ssrf_vulnerable": True}
    
    def make_file_protocol_request(self, file_path: str) -> Dict[str, Any]:
        """VULNERABLE: Make request using file:// protocol"""
        # VULNERABLE: File protocol SSRF vulnerability - CRITICAL
        # VULNERABLE: No file protocol protection
        # VULNERABLE: No file path validation
        
        try:
            # VULNERABLE: Construct file URL
            file_url = f"file://{file_path}"
            
            logger.info(f"VULNERABLE: Making file protocol request to: {file_url}")
            
            # VULNERABLE: Direct file protocol request
            response = urllib.request.urlopen(file_url)
            content = response.read().decode('utf-8')
            
            return {
                "success": True,
                "file_url": file_url,
                "content": content,
                "file_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File protocol SSRF error: {str(e)}")
            return {"error": str(e), "file_ssrf_vulnerable": True}
    
    def make_gopher_protocol_request(self, gopher_url: str) -> Dict[str, Any]:
        """VULNERABLE: Make request using gopher:// protocol"""
        # VULNERABLE: Gopher protocol SSRF vulnerability - CRITICAL
        # VULNERABLE: No gopher protocol protection
        # VULNERABLE: No gopher URL validation
        
        try:
            logger.info(f"VULNERABLE: Making gopher protocol request to: {gopher_url}")
            
            # VULNERABLE: Direct gopher protocol request
            response = urllib.request.urlopen(gopher_url)
            content = response.read().decode('utf-8')
            
            return {
                "success": True,
                "gopher_url": gopher_url,
                "content": content,
                "gopher_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Gopher protocol SSRF error: {str(e)}")
            return {"error": str(e), "gopher_ssrf_vulnerable": True}
    
    def make_ftp_protocol_request(self, ftp_url: str) -> Dict[str, Any]:
        """VULNERABLE: Make request using ftp:// protocol"""
        # VULNERABLE: FTP protocol SSRF vulnerability - CRITICAL
        # VULNERABLE: No FTP protocol protection
        # VULNERABLE: No FTP URL validation
        
        try:
            logger.info(f"VULNERABLE: Making FTP protocol request to: {ftp_url}")
            
            # VULNERABLE: Direct FTP protocol request
            response = urllib.request.urlopen(ftp_url)
            content = response.read().decode('utf-8')
            
            return {
                "success": True,
                "ftp_url": ftp_url,
                "content": content,
                "ftp_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: FTP protocol SSRF error: {str(e)}")
            return {"error": str(e), "ftp_ssrf_vulnerable": True}
    
    def make_socket_connection(self, host: str, port: int) -> Dict[str, Any]:
        """VULNERABLE: Make direct socket connection"""
        # VULNERABLE: Socket SSRF vulnerability - CRITICAL
        # VULNERABLE: No socket connection protection
        # VULNERABLE: No host/port validation
        
        try:
            logger.info(f"VULNERABLE: Making socket connection to: {host}:{port}")
            
            # VULNERABLE: Direct socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            # VULNERABLE: Connect to any host/port
            result = sock.connect_ex((host, port))
            
            sock.close()
            
            return {
                "success": True,
                "host": host,
                "port": port,
                "connection_result": result,
                "socket_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Socket SSRF error: {str(e)}")
            return {"error": str(e), "socket_ssrf_vulnerable": True}
    
    def make_redis_request(self, redis_command: str) -> Dict[str, Any]:
        """VULNERABLE: Make request to Redis service"""
        # VULNERABLE: Redis SSRF vulnerability - CRITICAL
        # VULNERABLE: No Redis protection
        # VULNERABLE: No Redis command validation
        
        try:
            # VULNERABLE: Construct Redis URL
            redis_url = f"http://127.0.0.1:6379/{redis_command}"
            
            logger.info(f"VULNERABLE: Making Redis request to: {redis_url}")
            
            # VULNERABLE: Direct Redis request
            response = requests.get(redis_url, timeout=5)
            
            return {
                "success": True,
                "redis_url": redis_url,
                "redis_command": redis_command,
                "status_code": response.status_code,
                "content": response.text,
                "redis_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Redis SSRF error: {str(e)}")
            return {"error": str(e), "redis_ssrf_vulnerable": True}
    
    def make_elasticsearch_request(self, es_query: str) -> Dict[str, Any]:
        """VULNERABLE: Make request to Elasticsearch service"""
        # VULNERABLE: Elasticsearch SSRF vulnerability - CRITICAL
        # VULNERABLE: No Elasticsearch protection
        # VULNERABLE: No Elasticsearch query validation
        
        try:
            # VULNERABLE: Construct Elasticsearch URL
            es_url = f"http://127.0.0.1:9200/_search?q={es_query}"
            
            logger.info(f"VULNERABLE: Making Elasticsearch request to: {es_url}")
            
            # VULNERABLE: Direct Elasticsearch request
            response = requests.get(es_url, timeout=5)
            
            return {
                "success": True,
                "elasticsearch_url": es_url,
                "elasticsearch_query": es_query,
                "status_code": response.status_code,
                "content": response.text,
                "elasticsearch_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Elasticsearch SSRF error: {str(e)}")
            return {"error": str(e), "elasticsearch_ssrf_vulnerable": True}
    
    def make_mongodb_request(self, mongo_query: str) -> Dict[str, Any]:
        """VULNERABLE: Make request to MongoDB service"""
        # VULNERABLE: MongoDB SSRF vulnerability - CRITICAL
        # VULNERABLE: No MongoDB protection
        # VULNERABLE: No MongoDB query validation
        
        try:
            # VULNERABLE: Construct MongoDB URL
            mongo_url = f"http://127.0.0.1:27017/admin?query={mongo_query}"
            
            logger.info(f"VULNERABLE: Making MongoDB request to: {mongo_url}")
            
            # VULNERABLE: Direct MongoDB request
            response = requests.get(mongo_url, timeout=5)
            
            return {
                "success": True,
                "mongodb_url": mongo_url,
                "mongodb_query": mongo_query,
                "status_code": response.status_code,
                "content": response.text,
                "mongodb_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: MongoDB SSRF error: {str(e)}")
            return {"error": str(e), "mongodb_ssrf_vulnerable": True}
    
    def make_blind_ssrf_request(self, url: str) -> Dict[str, Any]:
        """VULNERABLE: Make blind SSRF request"""
        # VULNERABLE: Blind SSRF vulnerability - CRITICAL
        # VULNERABLE: No blind SSRF protection
        # VULNERABLE: No response validation
        
        try:
            logger.info(f"VULNERABLE: Making blind SSRF request to: {url}")
            
            # VULNERABLE: Make request without processing response
            response = requests.get(url, timeout=5)
            
            # VULNERABLE: Don't return response content (blind)
            return {
                "success": True,
                "url": url,
                "status_code": response.status_code,
                "blind_ssrf_vulnerable": True,
                "note": "Response content not returned (blind SSRF)"
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Blind SSRF error: {str(e)}")
            return {"error": str(e), "blind_ssrf_vulnerable": True}
    
    def make_ssrf_with_redirect(self, url: str) -> Dict[str, Any]:
        """VULNERABLE: Make SSRF request with redirect following"""
        # VULNERABLE: SSRF with redirect vulnerability - CRITICAL
        # VULNERABLE: No redirect protection
        # VULNERABLE: No redirect validation
        
        try:
            logger.info(f"VULNERABLE: Making SSRF request with redirects to: {url}")
            
            # VULNERABLE: Allow redirects
            response = requests.get(url, allow_redirects=True, timeout=10)
            
            return {
                "success": True,
                "url": url,
                "final_url": response.url,
                "status_code": response.status_code,
                "redirect_count": len(response.history),
                "content": response.text,
                "redirect_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Redirect SSRF error: {str(e)}")
            return {"error": str(e), "redirect_ssrf_vulnerable": True}
    
    def make_ssrf_with_custom_headers(self, url: str, headers: Dict[str, str]) -> Dict[str, Any]:
        """VULNERABLE: Make SSRF request with custom headers"""
        # VULNERABLE: SSRF with custom headers vulnerability - CRITICAL
        # VULNERABLE: No header validation
        # VULNERABLE: No header restrictions
        
        try:
            logger.info(f"VULNERABLE: Making SSRF request with custom headers to: {url}")
            
            # VULNERABLE: Use custom headers without validation
            response = requests.get(url, headers=headers, timeout=10)
            
            return {
                "success": True,
                "url": url,
                "custom_headers": headers,
                "status_code": response.status_code,
                "response_headers": dict(response.headers),
                "content": response.text,
                "custom_headers_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Custom headers SSRF error: {str(e)}")
            return {"error": str(e), "custom_headers_ssrf_vulnerable": True}
    
    def make_ssrf_with_post_data(self, url: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Make SSRF request with POST data"""
        # VULNERABLE: SSRF with POST data vulnerability - CRITICAL
        # VULNERABLE: No POST data validation
        # VULNERABLE: No data restrictions
        
        try:
            logger.info(f"VULNERABLE: Making SSRF POST request to: {url}")
            
            # VULNERABLE: Send POST data without validation
            response = requests.post(url, json=data, timeout=10)
            
            return {
                "success": True,
                "url": url,
                "post_data": data,
                "status_code": response.status_code,
                "content": response.text,
                "post_ssrf_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: POST SSRF error: {str(e)}")
            return {"error": str(e), "post_ssrf_vulnerable": True}
    
    def get_request_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get request history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.request_history
