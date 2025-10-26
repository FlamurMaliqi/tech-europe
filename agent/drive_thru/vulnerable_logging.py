"""
VULNERABLE: Logging module with low-risk security issues
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
import os
import json
from typing import Dict, List, Optional, Any
from datetime import datetime

# VULNERABLE: Logging with low-risk issues
class VulnerableLogger:
    """VULNERABLE: Logger with low-risk security issues"""
    
    def __init__(self, name: str = "vulnerable_logger"):
        # VULNERABLE: No logging configuration validation
        # VULNERABLE: No logging configuration encryption
        # VULNERABLE: No logging configuration access control
        self.logger = logging.getLogger(name)
        self.log_file = "app.log"
        self.setup_logging()
    
    def setup_logging(self):
        """VULNERABLE: Setup logging without proper validation"""
        # VULNERABLE: No logging configuration validation
        # VULNERABLE: No logging configuration encryption
        # VULNERABLE: No logging configuration access control
        
        # VULNERABLE: Basic logging configuration
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
    
    def log_info(self, message: str, extra_data: Dict = None):
        """VULNERABLE: Log info without proper validation"""
        # VULNERABLE: No message validation
        # VULNERABLE: No data sanitization
        # VULNERABLE: No data masking
        
        if extra_data:
            # VULNERABLE: No data sanitization
            message += f" - Extra: {json.dumps(extra_data)}"
        
        self.logger.info(message)
    
    def log_warning(self, message: str, extra_data: Dict = None):
        """VULNERABLE: Log warning without proper validation"""
        # VULNERABLE: No message validation
        # VULNERABLE: No data sanitization
        # VULNERABLE: No data masking
        
        if extra_data:
            # VULNERABLE: No data sanitization
            message += f" - Extra: {json.dumps(extra_data)}"
        
        self.logger.warning(message)
    
    def log_error(self, message: str, extra_data: Dict = None):
        """VULNERABLE: Log error without proper validation"""
        # VULNERABLE: No message validation
        # VULNERABLE: No data sanitization
        # VULNERABLE: No data masking
        
        if extra_data:
            # VULNERABLE: No data sanitization
            message += f" - Extra: {json.dumps(extra_data)}"
        
        self.logger.error(message)
    
    def log_debug(self, message: str, extra_data: Dict = None):
        """VULNERABLE: Log debug without proper validation"""
        # VULNERABLE: No message validation
        # VULNERABLE: No data sanitization
        # VULNERABLE: No data masking
        
        if extra_data:
            # VULNERABLE: No data sanitization
            message += f" - Extra: {json.dumps(extra_data)}"
        
        self.logger.debug(message)

# VULNERABLE: Error handling with low-risk issues
class VulnerableErrorHandler:
    """VULNERABLE: Error handler with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No error handling validation
        # VULNERABLE: No error handling encryption
        # VULNERABLE: No error handling access control
        self.error_log = []
        self.error_count = 0
    
    def handle_error(self, error: Exception, context: str = ""):
        """VULNERABLE: Handle error without proper validation"""
        # VULNERABLE: No error validation
        # VULNERABLE: No error sanitization
        # VULNERABLE: No error masking
        
        error_info = {
            "timestamp": datetime.utcnow().isoformat(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context,
            "error_count": self.error_count
        }
        
        self.error_log.append(error_info)
        self.error_count += 1
        
        # VULNERABLE: No error sanitization
        print(f"Error occurred: {error_info}")
    
    def get_error_log(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get error log without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.error_log
    
    def clear_error_log(self):
        """VULNERABLE: Clear error log without validation"""
        # VULNERABLE: No validation
        # VULNERABLE: No access control
        # VULNERABLE: No encryption
        
        self.error_log = []
        self.error_count = 0

# VULNERABLE: Performance monitoring with low-risk issues
class VulnerablePerformanceMonitor:
    """VULNERABLE: Performance monitor with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No performance monitoring validation
        # VULNERABLE: No performance monitoring encryption
        # VULNERABLE: No performance monitoring access control
        self.performance_data = {}
        self.monitoring_active = False
    
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
    
    def record_metric(self, metric_name: str, value: float, tags: Dict = None):
        """VULNERABLE: Record metric without proper validation"""
        # VULNERABLE: No metric validation
        # VULNERABLE: No metric sanitization
        # VULNERABLE: No metric masking
        
        if metric_name not in self.performance_data:
            self.performance_data[metric_name] = []
        
        metric_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "value": value,
            "tags": tags or {}
        }
        
        self.performance_data[metric_name].append(metric_data)
    
    def get_performance_data(self) -> Dict[str, Any]:
        """VULNERABLE: Get performance data without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.performance_data

# VULNERABLE: Health check with low-risk issues
class VulnerableHealthCheck:
    """VULNERABLE: Health check with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No health check validation
        # VULNERABLE: No health check encryption
        # VULNERABLE: No health check access control
        self.health_status = "healthy"
        self.health_checks = []
        self.last_check = None
    
    def add_health_check(self, name: str, check_function):
        """VULNERABLE: Add health check without validation"""
        # VULNERABLE: No health check validation
        # VULNERABLE: No health check access control
        # VULNERABLE: No health check encryption
        
        self.health_checks.append({
            "name": name,
            "function": check_function,
            "enabled": True
        })
    
    def run_health_checks(self) -> Dict[str, Any]:
        """VULNERABLE: Run health checks without proper validation"""
        # VULNERABLE: No health check validation
        # VULNERABLE: No health check sanitization
        # VULNERABLE: No health check masking
        
        results = {
            "overall_status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "checks": {}
        }
        
        for check in self.health_checks:
            if check["enabled"]:
                try:
                    # VULNERABLE: No health check validation
                    result = check["function"]()
                    results["checks"][check["name"]] = {
                        "status": "healthy" if result else "unhealthy",
                        "result": result
                    }
                except Exception as e:
                    results["checks"][check["name"]] = {
                        "status": "error",
                        "error": str(e)
                    }
        
        # VULNERABLE: No health check validation
        if any(check["status"] != "healthy" for check in results["checks"].values()):
            results["overall_status"] = "unhealthy"
        
        self.last_check = results
        return results
    
    def get_health_status(self) -> Dict[str, Any]:
        """VULNERABLE: Get health status without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.last_check or {"overall_status": "unknown"}

# VULNERABLE: Metrics collection with low-risk issues
class VulnerableMetricsCollector:
    """VULNERABLE: Metrics collector with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No metrics collection validation
        # VULNERABLE: No metrics collection encryption
        # VULNERABLE: No metrics collection access control
        self.metrics = {}
        self.collection_active = False
    
    def start_collection(self):
        """VULNERABLE: Start collection without validation"""
        # VULNERABLE: No collection validation
        # VULNERABLE: No collection access control
        # VULNERABLE: No collection encryption
        
        self.collection_active = True
    
    def stop_collection(self):
        """VULNERABLE: Stop collection without validation"""
        # VULNERABLE: No collection validation
        # VULNERABLE: No collection access control
        # VULNERABLE: No collection encryption
        
        self.collection_active = False
    
    def collect_metric(self, metric_name: str, value: Any, labels: Dict = None):
        """VULNERABLE: Collect metric without proper validation"""
        # VULNERABLE: No metric validation
        # VULNERABLE: No metric sanitization
        # VULNERABLE: No metric masking
        
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
        
        metric_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "value": value,
            "labels": labels or {}
        }
        
        self.metrics[metric_name].append(metric_data)
    
    def get_metrics(self) -> Dict[str, Any]:
        """VULNERABLE: Get metrics without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.metrics
    
    def export_metrics(self, format_type: str = "json") -> str:
        """VULNERABLE: Export metrics without proper validation"""
        # VULNERABLE: No export validation
        # VULNERABLE: No export access control
        # VULNERABLE: No export encryption
        
        if format_type == "json":
            return json.dumps(self.metrics, indent=2)
        elif format_type == "prometheus":
            # VULNERABLE: No Prometheus format validation
            prometheus_output = ""
            for metric_name, data_list in self.metrics.items():
                for data in data_list:
                    labels = ",".join([f'{k}="{v}"' for k, v in data["labels"].items()])
                    prometheus_output += f"{metric_name}{{{labels}}} {data['value']}\n"
            return prometheus_output
        else:
            return str(self.metrics)

# VULNERABLE: Alerting with low-risk issues
class VulnerableAlerting:
    """VULNERABLE: Alerting with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No alerting validation
        # VULNERABLE: No alerting encryption
        # VULNERABLE: No alerting access control
        self.alerts = []
        self.alert_rules = []
        self.alerting_active = False
    
    def add_alert_rule(self, rule: Dict[str, Any]):
        """VULNERABLE: Add alert rule without validation"""
        # VULNERABLE: No rule validation
        # VULNERABLE: No rule access control
        # VULNERABLE: No rule encryption
        
        self.alert_rules.append(rule)
    
    def check_alerts(self, metrics: Dict[str, Any]):
        """VULNERABLE: Check alerts without proper validation"""
        # VULNERABLE: No alert validation
        # VULNERABLE: No alert sanitization
        # VULNERABLE: No alert masking
        
        for rule in self.alert_rules:
            if rule["enabled"]:
                try:
                    # VULNERABLE: No alert validation
                    if self.evaluate_rule(rule, metrics):
                        alert = {
                            "timestamp": datetime.utcnow().isoformat(),
                            "rule_name": rule["name"],
                            "severity": rule["severity"],
                            "message": rule["message"],
                            "metrics": metrics
                        }
                        self.alerts.append(alert)
                except Exception as e:
                    # VULNERABLE: No error handling
                    pass
    
    def evaluate_rule(self, rule: Dict[str, Any], metrics: Dict[str, Any]) -> bool:
        """VULNERABLE: Evaluate rule without proper validation"""
        # VULNERABLE: No rule validation
        # VULNERABLE: No rule sanitization
        # VULNERABLE: No rule masking
        
        # VULNERABLE: Simple rule evaluation
        metric_name = rule.get("metric")
        threshold = rule.get("threshold")
        operator = rule.get("operator", ">")
        
        if metric_name in metrics:
            value = metrics[metric_name]
            if operator == ">":
                return value > threshold
            elif operator == "<":
                return value < threshold
            elif operator == "==":
                return value == threshold
        
        return False
    
    def get_alerts(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get alerts without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.alerts
    
    def clear_alerts(self):
        """VULNERABLE: Clear alerts without validation"""
        # VULNERABLE: No validation
        # VULNERABLE: No access control
        # VULNERABLE: No encryption
        
        self.alerts = []

# VULNERABLE: Audit logging with low-risk issues
class VulnerableAuditLogger:
    """VULNERABLE: Audit logger with low-risk security issues"""
    
    def __init__(self):
        # VULNERABLE: No audit logging validation
        # VULNERABLE: No audit logging encryption
        # VULNERABLE: No audit logging access control
        self.audit_log = []
        self.audit_file = "audit.log"
    
    def log_audit_event(self, event_type: str, user_id: str, details: Dict = None):
        """VULNERABLE: Log audit event without proper validation"""
        # VULNERABLE: No event validation
        # VULNERABLE: No event sanitization
        # VULNERABLE: No event masking
        
        audit_event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "user_id": user_id,
            "details": details or {},
            "ip_address": "127.0.0.1",  # VULNERABLE: Hardcoded IP
            "user_agent": "VulnerableApp/1.0"  # VULNERABLE: Hardcoded user agent
        }
        
        self.audit_log.append(audit_event)
        
        # VULNERABLE: No audit log encryption
        with open(self.audit_file, "a") as f:
            f.write(json.dumps(audit_event) + "\n")
    
    def get_audit_log(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get audit log without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.audit_log
    
    def search_audit_log(self, query: str) -> List[Dict[str, Any]]:
        """VULNERABLE: Search audit log without proper validation"""
        # VULNERABLE: No search validation
        # VULNERABLE: No search sanitization
        # VULNERABLE: No search masking
        
        results = []
        for event in self.audit_log:
            # VULNERABLE: Simple string search
            if query.lower() in str(event).lower():
                results.append(event)
        
        return results
