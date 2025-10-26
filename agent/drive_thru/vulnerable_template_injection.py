"""
VULNERABLE: Template Injection vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import logging
from typing import Dict, List, Optional, Any
import time

logger = logging.getLogger(__name__)

# VULNERABLE: Template Injection vulnerabilities
class VulnerableTemplateInjection:
    """VULNERABLE: Template Injection vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No template injection protection
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        self.template_history = []
        self.injection_patterns = [
            r'\{\{.*\}\}',
            r'\{%.*%\}',
            r'\{#.*#\}',
            r'<%.*%>',
            r'<%=.*%>',
            r'<%.*%>',
            r'\$\{.*\}',
            r'#\{.*\}',
            r'@\{.*\}',
            r'\{.*\}',
            r'\[.*\]',
            r'\(.*\)'
        ]
    
    def execute_jinja2_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute Jinja2 template injection"""
        # VULNERABLE: Template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Jinja2 template injection: {template[:100]}...")
            
            # VULNERABLE: Direct template rendering without validation
            result = self._render_jinja2_template(template, context)
            
            self.template_history.append({
                "template": template,
                "context": context,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "result": result,
                "jinja2_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Jinja2 template injection error: {str(e)}")
            return {"error": str(e), "jinja2_injection_vulnerable": True}
    
    def execute_django_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute Django template injection"""
        # VULNERABLE: Template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Django template injection: {template[:100]}...")
            
            # VULNERABLE: Direct template rendering without validation
            result = self._render_django_template(template, context)
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "result": result,
                "django_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Django template injection error: {str(e)}")
            return {"error": str(e), "django_injection_vulnerable": True}
    
    def execute_erb_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute ERB template injection"""
        # VULNERABLE: Template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing ERB template injection: {template[:100]}...")
            
            # VULNERABLE: Direct template rendering without validation
            result = self._render_erb_template(template, context)
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "result": result,
                "erb_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: ERB template injection error: {str(e)}")
            return {"error": str(e), "erb_injection_vulnerable": True}
    
    def execute_smarty_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute Smarty template injection"""
        # VULNERABLE: Template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Smarty template injection: {template[:100]}...")
            
            # VULNERABLE: Direct template rendering without validation
            result = self._render_smarty_template(template, context)
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "result": result,
                "smarty_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Smarty template injection error: {str(e)}")
            return {"error": str(e), "smarty_injection_vulnerable": True}
    
    def execute_twig_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute Twig template injection"""
        # VULNERABLE: Template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing Twig template injection: {template[:100]}...")
            
            # VULNERABLE: Direct template rendering without validation
            result = self._render_twig_template(template, context)
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "result": result,
                "twig_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Twig template injection error: {str(e)}")
            return {"error": str(e), "twig_injection_vulnerable": True}
    
    def execute_advanced_template_injection(self, template: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """VULNERABLE: Execute advanced template injection"""
        # VULNERABLE: Advanced template injection vulnerability - CRITICAL
        # VULNERABLE: No template validation
        # VULNERABLE: No input sanitization
        
        try:
            logger.info(f"VULNERABLE: Executing advanced template injection: {template[:100]}...")
            
            # VULNERABLE: Advanced injection techniques
            advanced_templates = [
                f"{{{{ {template} }}}}",
                f"{{% {template} %}}",
                f"{{# {template} #}}",
                f"<%= {template} %>",
                f"<%= {template} %>",
                f"<%= {template} %>",
                f"${{{template}}}",
                f"#{{{template}}}",
                f"@{{{template}}}",
                f"{{{template}}}",
                f"[{template}]",
                f"({template})"
            ]
            
            results = []
            for advanced_template in advanced_templates:
                try:
                    result = self._render_advanced_template(advanced_template, context)
                    results.append({
                        "template": advanced_template,
                        "result": result,
                        "injection_successful": True
                    })
                except Exception as error:
                    results.append({
                        "template": advanced_template,
                        "error": str(error),
                        "injection_successful": True
                    })
            
            return {
                "success": True,
                "template": template,
                "context": context,
                "advanced_results": results,
                "advanced_template_injection_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Advanced template injection error: {str(e)}")
            return {"error": str(e), "advanced_template_injection_vulnerable": True}
    
    def _render_jinja2_template(self, template: str, context: Dict[str, Any]) -> str:
        """VULNERABLE: Render Jinja2 template without validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No context sanitization
        
        # Mock Jinja2 template rendering
        result = template
        for key, value in context.items():
            result = result.replace(f"{{{{ {key} }}}}", str(value))
            result = result.replace(f"{{% {key} %}}", str(value))
            result = result.replace(f"{{# {key} #}}", str(value))
        
        return result
    
    def _render_django_template(self, template: str, context: Dict[str, Any]) -> str:
        """VULNERABLE: Render Django template without validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No context sanitization
        
        # Mock Django template rendering
        result = template
        for key, value in context.items():
            result = result.replace(f"{{{{ {key} }}}}", str(value))
            result = result.replace(f"{{% {key} %}}", str(value))
            result = result.replace(f"{{# {key} #}}", str(value))
        
        return result
    
    def _render_erb_template(self, template: str, context: Dict[str, Any]) -> str:
        """VULNERABLE: Render ERB template without validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No context sanitization
        
        # Mock ERB template rendering
        result = template
        for key, value in context.items():
            result = result.replace(f"<%= {key} %>", str(value))
            result = result.replace(f"<% {key} %>", str(value))
            result = result.replace(f"<%# {key} #%>", str(value))
        
        return result
    
    def _render_smarty_template(self, template: str, context: Dict[str, Any]) -> str:
        """VULNERABLE: Render Smarty template without validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No context sanitization
        
        # Mock Smarty template rendering
        result = template
        for key, value in context.items():
            result = result.replace(f"${{{key}}}", str(value))
            result = result.replace(f"${{{key}}}", str(value))
            result = result.replace(f"${{{key}}}", str(value))
        
        return result
    
    def _render_twig_template(self, template: str, context: Dict[str, Any]) -> str:
        """VULNERABLE: Render Twig template without validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No context sanitization
        
        # Mock Twig template rendering
        result = template
        for key, value in context.items():
            result = result.replace(f"{{{{ {key} }}}}", str(value))
            result = result.replace(f"{{% {key} %}}", str(value))
            result = result.replace(f"{{# {key} #}}", str(value))
        
        return result
    
    def _render_advanced_template(self, template: str, context: Dict[str, Any]) -> str:
        """VULNERABLE: Render advanced template without validation"""
        # VULNERABLE: No template validation
        # VULNERABLE: No context sanitization
        
        # Mock advanced template rendering
        result = template
        for key, value in context.items():
            result = result.replace(f"{{{{ {key} }}}}", str(value))
            result = result.replace(f"{{% {key} %}}", str(value))
            result = result.replace(f"{{# {key} #}}", str(value))
            result = result.replace(f"<%= {key} %>", str(value))
            result = result.replace(f"<%= {key} %>", str(value))
            result = result.replace(f"<%= {key} %>", str(value))
            result = result.replace(f"${{{key}}}", str(value))
            result = result.replace(f"#{{{key}}}", str(value))
            result = result.replace(f"@{{{key}}}", str(value))
            result = result.replace(f"{{{key}}}", str(value))
            result = result.replace(f"[{key}]", str(value))
            result = result.replace(f"({key})", str(value))
        
        return result
    
    def get_template_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get template history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.template_history
