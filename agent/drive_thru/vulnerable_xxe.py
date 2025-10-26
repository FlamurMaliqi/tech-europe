"""
VULNERABLE: XXE (XML External Entity) vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import xml.etree.ElementTree as ET
import xml.dom.minidom
import requests
import logging
from typing import Dict, List, Optional, Any
from io import StringIO
import os
import tempfile

logger = logging.getLogger(__name__)

# VULNERABLE: XXE vulnerabilities
class VulnerableXXE:
    """VULNERABLE: XML External Entity vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No XXE protection
        # VULNERABLE: No XML validation
        # VULNERABLE: No entity restrictions
        self.xml_cache = {}
        self.entity_resolver_calls = []
        self.external_requests = []
    
    def parse_xml_with_external_entities(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with external entity references"""
        # VULNERABLE: XXE vulnerability - CRITICAL
        # VULNERABLE: No entity restrictions
        # VULNERABLE: No external entity protection
        
        try:
            logger.info(f"VULNERABLE: Parsing XML with external entities: {xml_content[:100]}...")
            
            # VULNERABLE: Parse XML without disabling external entities
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process XML without entity validation
            result = self._process_xml_element(root)
            
            return {
                "parsed": True,
                "content": result,
                "xxe_vulnerable": True,
                "external_entities_processed": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_file_entities(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with file:// entity references"""
        # VULNERABLE: File-based XXE vulnerability - CRITICAL
        # VULNERABLE: No file access restrictions
        # VULNERABLE: No entity validation
        
        try:
            logger.info(f"VULNERABLE: Parsing XML with file entities: {xml_content[:100]}...")
            
            # VULNERABLE: Parse XML allowing file:// entities
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process XML elements that might contain file references
            result = self._process_xml_with_file_access(root)
            
            return {
                "parsed": True,
                "content": result,
                "file_entities_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: File XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_http_entities(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with http:// entity references"""
        # VULNERABLE: HTTP-based XXE vulnerability - CRITICAL
        # VULNERABLE: No HTTP entity restrictions
        # VULNERABLE: No network access control
        
        try:
            logger.info(f"VULNERABLE: Parsing XML with HTTP entities: {xml_content[:100]}...")
            
            # VULNERABLE: Parse XML allowing http:// entities
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process XML elements that might contain HTTP references
            result = self._process_xml_with_http_access(root)
            
            return {
                "parsed": True,
                "content": result,
                "http_entities_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: HTTP XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_parameter_entities(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with parameter entity references"""
        # VULNERABLE: Parameter entity XXE vulnerability - CRITICAL
        # VULNERABLE: No parameter entity restrictions
        # VULNERABLE: No entity validation
        
        try:
            logger.info(f"VULNERABLE: Parsing XML with parameter entities: {xml_content[:100]}...")
            
            # VULNERABLE: Parse XML allowing parameter entities
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process XML with parameter entity expansion
            result = self._process_xml_with_parameter_entities(root)
            
            return {
                "parsed": True,
                "content": result,
                "parameter_entities_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Parameter entity XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_blind_xxe(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with blind XXE techniques"""
        # VULNERABLE: Blind XXE vulnerability - CRITICAL
        # VULNERABLE: No blind XXE protection
        # VULNERABLE: No out-of-band detection
        
        try:
            logger.info(f"VULNERABLE: Parsing XML with blind XXE: {xml_content[:100]}...")
            
            # VULNERABLE: Parse XML for blind XXE
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process XML for blind XXE techniques
            result = self._process_xml_blind_xxe(root)
            
            return {
                "parsed": True,
                "content": result,
                "blind_xxe_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Blind XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_soap_xxe(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with SOAP XXE vulnerabilities"""
        # VULNERABLE: SOAP XXE vulnerability - CRITICAL
        # VULNERABLE: No SOAP entity restrictions
        # VULNERABLE: No SOAP validation
        
        try:
            logger.info(f"VULNERABLE: Parsing SOAP XML with XXE: {xml_content[:100]}...")
            
            # VULNERABLE: Parse SOAP XML without entity protection
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process SOAP XML with XXE
            result = self._process_soap_xml_xxe(root)
            
            return {
                "parsed": True,
                "content": result,
                "soap_xxe_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: SOAP XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_svg_xxe(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with SVG XXE vulnerabilities"""
        # VULNERABLE: SVG XXE vulnerability - CRITICAL
        # VULNERABLE: No SVG entity restrictions
        # VULNERABLE: No SVG validation
        
        try:
            logger.info(f"VULNERABLE: Parsing SVG XML with XXE: {xml_content[:100]}...")
            
            # VULNERABLE: Parse SVG XML without entity protection
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process SVG XML with XXE
            result = self._process_svg_xml_xxe(root)
            
            return {
                "parsed": True,
                "content": result,
                "svg_xxe_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: SVG XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def parse_xml_with_office_xxe(self, xml_content: str) -> Dict[str, Any]:
        """VULNERABLE: Parse XML with Office document XXE vulnerabilities"""
        # VULNERABLE: Office XXE vulnerability - CRITICAL
        # VULNERABLE: No Office entity restrictions
        # VULNERABLE: No Office validation
        
        try:
            logger.info(f"VULNERABLE: Parsing Office XML with XXE: {xml_content[:100]}...")
            
            # VULNERABLE: Parse Office XML without entity protection
            root = ET.fromstring(xml_content)
            
            # VULNERABLE: Process Office XML with XXE
            result = self._process_office_xml_xxe(root)
            
            return {
                "parsed": True,
                "content": result,
                "office_xxe_processed": True,
                "xxe_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Office XXE parsing error: {str(e)}")
            return {"error": str(e), "xxe_vulnerable": True}
    
    def _process_xml_element(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process XML element without entity validation"""
        # VULNERABLE: No entity validation
        # VULNERABLE: No content validation
        
        result = {}
        
        if element.text and element.text.strip():
            result["text"] = element.text.strip()
        
        for child in element:
            child_result = self._process_xml_element(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_xml_with_file_access(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process XML with file access"""
        # VULNERABLE: File access without restrictions
        # VULNERABLE: No file path validation
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process text that might contain file paths
            text = element.text.strip()
            if text.startswith("file://"):
                # VULNERABLE: Attempt to read file
                try:
                    file_path = text.replace("file://", "")
                    with open(file_path, 'r') as f:
                        file_content = f.read()
                    result["file_content"] = file_content
                except Exception as e:
                    result["file_error"] = str(e)
            result["text"] = text
        
        for child in element:
            child_result = self._process_xml_with_file_access(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_xml_with_http_access(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process XML with HTTP access"""
        # VULNERABLE: HTTP access without restrictions
        # VULNERABLE: No URL validation
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process text that might contain HTTP URLs
            text = element.text.strip()
            if text.startswith("http://") or text.startswith("https://"):
                # VULNERABLE: Attempt to make HTTP request
                try:
                    response = requests.get(text, timeout=5)
                    result["http_content"] = response.text
                    result["http_status"] = response.status_code
                except Exception as e:
                    result["http_error"] = str(e)
            result["text"] = text
        
        for child in element:
            child_result = self._process_xml_with_http_access(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_xml_with_parameter_entities(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process XML with parameter entities"""
        # VULNERABLE: Parameter entity processing
        # VULNERABLE: No parameter validation
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process text with parameter entities
            text = element.text.strip()
            # VULNERABLE: Expand parameter entities
            if "%" in text:
                # VULNERABLE: Simple parameter entity expansion
                expanded_text = text.replace("%param;", "expanded_parameter")
                result["expanded_text"] = expanded_text
            result["text"] = text
        
        for child in element:
            child_result = self._process_xml_with_parameter_entities(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_xml_blind_xxe(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process XML for blind XXE"""
        # VULNERABLE: Blind XXE processing
        # VULNERABLE: No blind XXE detection
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process text for blind XXE
            text = element.text.strip()
            # VULNERABLE: Check for blind XXE patterns
            if "SYSTEM" in text or "PUBLIC" in text:
                result["blind_xxe_detected"] = True
                result["xxe_pattern"] = text
            result["text"] = text
        
        for child in element:
            child_result = self._process_xml_blind_xxe(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_soap_xml_xxe(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process SOAP XML with XXE"""
        # VULNERABLE: SOAP XXE processing
        # VULNERABLE: No SOAP validation
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process SOAP text
            text = element.text.strip()
            # VULNERABLE: Check for SOAP XXE patterns
            if "soap" in element.tag.lower() or "envelope" in element.tag.lower():
                result["soap_xxe_detected"] = True
            result["text"] = text
        
        for child in element:
            child_result = self._process_soap_xml_xxe(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_svg_xml_xxe(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process SVG XML with XXE"""
        # VULNERABLE: SVG XXE processing
        # VULNERABLE: No SVG validation
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process SVG text
            text = element.text.strip()
            # VULNERABLE: Check for SVG XXE patterns
            if "svg" in element.tag.lower() or "image" in element.tag.lower():
                result["svg_xxe_detected"] = True
            result["text"] = text
        
        for child in element:
            child_result = self._process_svg_xml_xxe(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _process_office_xml_xxe(self, element) -> Dict[str, Any]:
        """VULNERABLE: Process Office XML with XXE"""
        # VULNERABLE: Office XXE processing
        # VULNERABLE: No Office validation
        
        result = {}
        
        if element.text and element.text.strip():
            # VULNERABLE: Process Office text
            text = element.text.strip()
            # VULNERABLE: Check for Office XXE patterns
            if "office" in element.tag.lower() or "document" in element.tag.lower():
                result["office_xxe_detected"] = True
            result["text"] = text
        
        for child in element:
            child_result = self._process_office_xml_xxe(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
