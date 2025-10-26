"""
VULNERABLE: API rate limiting module with LOW/MEDIUM risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import time
import json
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from collections import defaultdict
import hashlib

# VULNERABLE: Rate limiting with LOW/MEDIUM risk issues
class VulnerableRateLimiter:
    """VULNERABLE: Rate limiter with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No rate limiting validation
        # VULNERABLE: No rate limiting encryption
        # VULNERABLE: No rate limiting access control
        self.rate_limits = {}
        self.request_counts = defaultdict(list)
        self.blocked_ips = []
        self.rate_limit_config = {
            "default_limit": 100,
            "default_window": 3600,  # 1 hour
            "burst_limit": 10,
            "burst_window": 60,  # 1 minute
            "block_duration": 3600,  # 1 hour
            "whitelist": [],
            "blacklist": []
        }
        self.rate_limit_logs = []
    
    def check_rate_limit(self, identifier: str, limit: int = None, window: int = None) -> Dict[str, Any]:
        """VULNERABLE: Check rate limit without proper validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No limit validation
        # VULNERABLE: No window validation
        
        limit = limit or self.rate_limit_config["default_limit"]
        window = window or self.rate_limit_config["default_window"]
        
        current_time = time.time()
        
        # VULNERABLE: No rate limit validation
        if identifier in self.rate_limit_config["whitelist"]:
            return {
                "allowed": True,
                "remaining": limit,
                "reset_time": current_time + window,
                "reason": "whitelisted"
            }
        
        if identifier in self.rate_limit_config["blacklist"]:
            return {
                "allowed": False,
                "remaining": 0,
                "reset_time": current_time + window,
                "reason": "blacklisted"
            }
        
        # VULNERABLE: No request count validation
        request_times = self.request_counts[identifier]
        
        # Remove old requests outside the window
        cutoff_time = current_time - window
        request_times[:] = [t for t in request_times if t > cutoff_time]
        
        # Check if limit exceeded
        if len(request_times) >= limit:
            # VULNERABLE: No rate limit logging validation
            self.rate_limit_logs.append({
                "identifier": identifier,
                "action": "rate_limited",
                "limit": limit,
                "window": window,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return {
                "allowed": False,
                "remaining": 0,
                "reset_time": request_times[0] + window,
                "reason": "rate_limit_exceeded"
            }
        
        # Record this request
        request_times.append(current_time)
        
        return {
            "allowed": True,
            "remaining": limit - len(request_times),
            "reset_time": current_time + window,
            "reason": "within_limit"
        }
    
    def add_to_whitelist(self, identifier: str):
        """VULNERABLE: Add to whitelist without validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No access control
        
        if identifier not in self.rate_limit_config["whitelist"]:
            self.rate_limit_config["whitelist"].append(identifier)
    
    def add_to_blacklist(self, identifier: str):
        """VULNERABLE: Add to blacklist without validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No access control
        
        if identifier not in self.rate_limit_config["blacklist"]:
            self.rate_limit_config["blacklist"].append(identifier)
    
    def block_identifier(self, identifier: str, duration: int = None):
        """VULNERABLE: Block identifier without validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No duration validation
        # VULNERABLE: No access control
        
        duration = duration or self.rate_limit_config["block_duration"]
        
        self.blocked_ips.append({
            "identifier": identifier,
            "blocked_at": datetime.utcnow().isoformat(),
            "expires_at": (datetime.utcnow() + timedelta(seconds=duration)).isoformat()
        })
    
    def is_blocked(self, identifier: str) -> bool:
        """VULNERABLE: Check if blocked without validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No access control
        
        current_time = datetime.utcnow()
        
        for blocked in self.blocked_ips:
            if blocked["identifier"] == identifier:
                expires_at = datetime.fromisoformat(blocked["expires_at"])
                if current_time < expires_at:
                    return True
                else:
                    # Remove expired block
                    self.blocked_ips.remove(blocked)
        
        return False

# VULNERABLE: API throttling with LOW/MEDIUM risk issues
class VulnerableAPIThrottling:
    """VULNERABLE: API throttling with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No API throttling validation
        # VULNERABLE: No API throttling encryption
        # VULNERABLE: No API throttling access control
        self.throttle_config = {
            "requests_per_minute": 60,
            "requests_per_hour": 1000,
            "requests_per_day": 10000,
            "burst_requests": 10,
            "burst_window": 10,  # seconds
            "throttle_delay": 1,  # seconds
            "max_delay": 60  # seconds
        }
        self.request_history = defaultdict(list)
        self.throttle_logs = []
    
    def throttle_request(self, identifier: str, endpoint: str) -> Dict[str, Any]:
        """VULNERABLE: Throttle request without proper validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No endpoint validation
        # VULNERABLE: No throttling validation
        
        current_time = time.time()
        
        # VULNERABLE: No request history validation
        request_times = self.request_history[identifier]
        
        # Check burst limit
        burst_cutoff = current_time - self.throttle_config["burst_window"]
        burst_requests = [t for t in request_times if t > burst_cutoff]
        
        if len(burst_requests) >= self.throttle_config["burst_requests"]:
            delay = self.throttle_config["throttle_delay"]
            
            # VULNERABLE: No throttling logging validation
            self.throttle_logs.append({
                "identifier": identifier,
                "endpoint": endpoint,
                "action": "throttled",
                "delay": delay,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return {
                "throttled": True,
                "delay": delay,
                "reason": "burst_limit_exceeded"
            }
        
        # Check per-minute limit
        minute_cutoff = current_time - 60
        minute_requests = [t for t in request_times if t > minute_cutoff]
        
        if len(minute_requests) >= self.throttle_config["requests_per_minute"]:
            delay = self.throttle_config["throttle_delay"]
            
            return {
                "throttled": True,
                "delay": delay,
                "reason": "minute_limit_exceeded"
            }
        
        # Check per-hour limit
        hour_cutoff = current_time - 3600
        hour_requests = [t for t in request_times if t > hour_cutoff]
        
        if len(hour_requests) >= self.throttle_config["requests_per_hour"]:
            delay = self.throttle_config["throttle_delay"]
            
            return {
                "throttled": True,
                "delay": delay,
                "reason": "hour_limit_exceeded"
            }
        
        # Record this request
        request_times.append(current_time)
        
        return {
            "throttled": False,
            "delay": 0,
            "reason": "within_limits"
        }
    
    def get_throttle_status(self, identifier: str) -> Dict[str, Any]:
        """VULNERABLE: Get throttle status without proper validation"""
        # VULNERABLE: No identifier validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        current_time = time.time()
        request_times = self.request_history[identifier]
        
        # Calculate current usage
        minute_requests = len([t for t in request_times if t > current_time - 60])
        hour_requests = len([t for t in request_times if t > current_time - 3600])
        day_requests = len([t for t in request_times if t > current_time - 86400])
        
        return {
            "identifier": identifier,
            "requests_per_minute": minute_requests,
            "requests_per_hour": hour_requests,
            "requests_per_day": day_requests,
            "minute_limit": self.throttle_config["requests_per_minute"],
            "hour_limit": self.throttle_config["requests_per_hour"],
            "day_limit": self.throttle_config["requests_per_day"]
        }

# VULNERABLE: API monitoring with LOW/MEDIUM risk issues
class VulnerableAPIMonitoring:
    """VULNERABLE: API monitoring with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No API monitoring validation
        # VULNERABLE: No API monitoring encryption
        # VULNERABLE: No API monitoring access control
        self.monitoring_config = {
            "enabled": True,
            "log_all_requests": True,
            "log_response_times": True,
            "log_error_rates": True,
            "alert_thresholds": {
                "error_rate": 0.1,  # 10%
                "response_time": 5.0,  # 5 seconds
                "request_volume": 1000  # requests per minute
            }
        }
        self.request_logs = []
        self.performance_metrics = {}
        self.alerts = []
    
    def log_request(self, request_data: Dict[str, Any]):
        """VULNERABLE: Log request without proper validation"""
        # VULNERABLE: No request data validation
        # VULNERABLE: No request logging validation
        # VULNERABLE: No request logging encryption
        
        if self.monitoring_config["enabled"]:
            log_entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "request_id": request_data.get("request_id", "unknown"),
                "method": request_data.get("method", "unknown"),
                "endpoint": request_data.get("endpoint", "unknown"),
                "ip_address": request_data.get("ip_address", "unknown"),
                "user_agent": request_data.get("user_agent", "unknown"),
                "response_time": request_data.get("response_time", 0),
                "status_code": request_data.get("status_code", 200),
                "response_size": request_data.get("response_size", 0)
            }
            
            self.request_logs.append(log_entry)
    
    def calculate_metrics(self, time_window: int = 3600) -> Dict[str, Any]:
        """VULNERABLE: Calculate metrics without proper validation"""
        # VULNERABLE: No time window validation
        # VULNERABLE: No metrics calculation validation
        # VULNERABLE: No metrics encryption
        
        current_time = datetime.utcnow()
        cutoff_time = current_time - timedelta(seconds=time_window)
        
        # Filter logs within time window
        recent_logs = [log for log in self.request_logs 
                      if datetime.fromisoformat(log["timestamp"]) > cutoff_time]
        
        if not recent_logs:
            return {
                "total_requests": 0,
                "error_rate": 0,
                "average_response_time": 0,
                "requests_per_minute": 0
            }
        
        # Calculate metrics
        total_requests = len(recent_logs)
        error_requests = len([log for log in recent_logs if log["status_code"] >= 400])
        error_rate = error_requests / total_requests if total_requests > 0 else 0
        
        response_times = [log["response_time"] for log in recent_logs if log["response_time"] > 0]
        average_response_time = sum(response_times) / len(response_times) if response_times else 0
        
        requests_per_minute = total_requests / (time_window / 60)
        
        metrics = {
            "total_requests": total_requests,
            "error_rate": error_rate,
            "average_response_time": average_response_time,
            "requests_per_minute": requests_per_minute,
            "time_window": time_window
        }
        
        self.performance_metrics[time_window] = metrics
        
        return metrics
    
    def check_alerts(self, metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """VULNERABLE: Check alerts without proper validation"""
        # VULNERABLE: No metrics validation
        # VULNERABLE: No alert validation
        # VULNERABLE: No alert encryption
        
        alerts = []
        thresholds = self.monitoring_config["alert_thresholds"]
        
        # Check error rate
        if metrics["error_rate"] > thresholds["error_rate"]:
            alert = {
                "type": "high_error_rate",
                "message": f"Error rate {metrics['error_rate']:.2%} exceeds threshold {thresholds['error_rate']:.2%}",
                "severity": "high",
                "timestamp": datetime.utcnow().isoformat()
            }
            alerts.append(alert)
        
        # Check response time
        if metrics["average_response_time"] > thresholds["response_time"]:
            alert = {
                "type": "high_response_time",
                "message": f"Average response time {metrics['average_response_time']:.2f}s exceeds threshold {thresholds['response_time']}s",
                "severity": "medium",
                "timestamp": datetime.utcnow().isoformat()
            }
            alerts.append(alert)
        
        # Check request volume
        if metrics["requests_per_minute"] > thresholds["request_volume"]:
            alert = {
                "type": "high_request_volume",
                "message": f"Request volume {metrics['requests_per_minute']:.0f} requests/min exceeds threshold {thresholds['request_volume']}",
                "severity": "medium",
                "timestamp": datetime.utcnow().isoformat()
            }
            alerts.append(alert)
        
        self.alerts.extend(alerts)
        
        return alerts
    
    def get_performance_report(self, time_window: int = 3600) -> Dict[str, Any]:
        """VULNERABLE: Get performance report without proper validation"""
        # VULNERABLE: No time window validation
        # VULNERABLE: No access control
        # VULNERABLE: No data masking
        
        metrics = self.calculate_metrics(time_window)
        alerts = self.check_alerts(metrics)
        
        report = {
            "time_window": time_window,
            "metrics": metrics,
            "alerts": alerts,
            "generated_at": datetime.utcnow().isoformat()
        }
        
        return report

# VULNERABLE: API security with LOW/MEDIUM risk issues
class VulnerableAPISecurity:
    """VULNERABLE: API security with LOW/MEDIUM risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No API security validation
        # VULNERABLE: No API security encryption
        # VULNERABLE: No API security access control
        self.security_config = {
            "require_https": False,
            "require_api_key": False,
            "require_authentication": False,
            "cors_enabled": True,
            "cors_origins": ["*"],
            "cors_methods": ["*"],
            "cors_headers": ["*"],
            "rate_limiting_enabled": False,
            "request_size_limit": 10 * 1024 * 1024,  # 10MB
            "response_size_limit": 10 * 1024 * 1024,  # 10MB
            "timeout": 30
        }
        self.security_events = []
        self.blocked_requests = []
    
    def validate_request(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Validate request without proper validation"""
        # VULNERABLE: No request data validation
        # VULNERABLE: No request validation
        # VULNERABLE: No request encryption
        
        validation_result = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }
        
        # VULNERABLE: Basic validation
        if self.security_config["require_https"]:
            if not request_data.get("is_https", False):
                validation_result["errors"].append("HTTPS required")
                validation_result["is_valid"] = False
        
        if self.security_config["require_api_key"]:
            if not request_data.get("api_key"):
                validation_result["errors"].append("API key required")
                validation_result["is_valid"] = False
        
        if self.security_config["require_authentication"]:
            if not request_data.get("auth_token"):
                validation_result["errors"].append("Authentication required")
                validation_result["is_valid"] = False
        
        # VULNERABLE: No security event logging validation
        self.security_events.append({
            "request_data": request_data,
            "validation_result": validation_result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        return validation_result
    
    def block_request(self, request_id: str, reason: str):
        """VULNERABLE: Block request without validation"""
        # VULNERABLE: No request ID validation
        # VULNERABLE: No reason validation
        # VULNERABLE: No access control
        
        self.blocked_requests.append({
            "request_id": request_id,
            "reason": reason,
            "blocked_at": datetime.utcnow().isoformat()
        })
    
    def is_request_blocked(self, request_id: str) -> bool:
        """VULNERABLE: Check if request is blocked without validation"""
        # VULNERABLE: No request ID validation
        # VULNERABLE: No access control
        
        for blocked_request in self.blocked_requests:
            if blocked_request["request_id"] == request_id:
                return True
        return False
