"""
VULNERABLE: Advanced Insecure Deserialization vulnerabilities
DO NOT USE IN PRODUCTION - FOR EDUCATIONAL PURPOSES ONLY
"""

import pickle
import marshal
import json
import yaml
import xml.etree.ElementTree as ET
import logging
from typing import Dict, List, Optional, Any
import base64
import zlib
import time

logger = logging.getLogger(__name__)

# VULNERABLE: Advanced Insecure Deserialization vulnerabilities
class VulnerableAdvancedDeserialization:
    """VULNERABLE: Advanced Insecure Deserialization vulnerabilities"""
    
    def __init__(self):
        # VULNERABLE: No deserialization protection
        # VULNERABLE: No input validation
        # VULNERABLE: No deserialization restrictions
        self.deserialization_history = []
        self.deserialized_objects = []
    
    def deserialize_pickle_data(self, pickle_data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Deserialize pickle data without validation"""
        # VULNERABLE: Pickle deserialization vulnerability - CRITICAL
        # VULNERABLE: No pickle validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing pickle data: {len(pickle_data)} bytes")
            
            # VULNERABLE: Direct pickle deserialization
            result = pickle.loads(pickle_data)
            
            self.deserialization_history.append({
                "type": "pickle",
                "data": pickle_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": "pickle",
                "data": pickle_data,
                "deserialized": result,
                "pickle_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Pickle deserialization error: {str(e)}")
            return {"error": str(e), "pickle_vulnerable": True}
    
    def deserialize_marshal_data(self, marshal_data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Deserialize marshal data without validation"""
        # VULNERABLE: Marshal deserialization vulnerability - CRITICAL
        # VULNERABLE: No marshal validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing marshal data: {len(marshal_data)} bytes")
            
            # VULNERABLE: Direct marshal deserialization
            result = marshal.loads(marshal_data)
            
            self.deserialization_history.append({
                "type": "marshal",
                "data": marshal_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": "marshal",
                "data": marshal_data,
                "deserialized": result,
                "marshal_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Marshal deserialization error: {str(e)}")
            return {"error": str(e), "marshal_vulnerable": True}
    
    def deserialize_json_data(self, json_data: str) -> Dict[str, Any]:
        """VULNERABLE: Deserialize JSON data without validation"""
        # VULNERABLE: JSON deserialization vulnerability - HIGH
        # VULNERABLE: No JSON validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing JSON data: {json_data[:100]}...")
            
            # VULNERABLE: Direct JSON deserialization
            result = json.loads(json_data)
            
            self.deserialization_history.append({
                "type": "json",
                "data": json_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": "json",
                "data": json_data,
                "deserialized": result,
                "json_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: JSON deserialization error: {str(e)}")
            return {"error": str(e), "json_vulnerable": True}
    
    def deserialize_yaml_data(self, yaml_data: str) -> Dict[str, Any]:
        """VULNERABLE: Deserialize YAML data without validation"""
        # VULNERABLE: YAML deserialization vulnerability - CRITICAL
        # VULNERABLE: No YAML validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing YAML data: {yaml_data[:100]}...")
            
            # VULNERABLE: Direct YAML deserialization
            result = yaml.safe_load(yaml_data)
            
            self.deserialization_history.append({
                "type": "yaml",
                "data": yaml_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": "yaml",
                "data": yaml_data,
                "deserialized": result,
                "yaml_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: YAML deserialization error: {str(e)}")
            return {"error": str(e), "yaml_vulnerable": True}
    
    def deserialize_xml_data(self, xml_data: str) -> Dict[str, Any]:
        """VULNERABLE: Deserialize XML data without validation"""
        # VULNERABLE: XML deserialization vulnerability - HIGH
        # VULNERABLE: No XML validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing XML data: {xml_data[:100]}...")
            
            # VULNERABLE: Direct XML deserialization
            root = ET.fromstring(xml_data)
            result = self._xml_to_dict(root)
            
            self.deserialization_history.append({
                "type": "xml",
                "data": xml_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": "xml",
                "data": xml_data,
                "deserialized": result,
                "xml_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: XML deserialization error: {str(e)}")
            return {"error": str(e), "xml_vulnerable": True}
    
    def deserialize_base64_data(self, base64_data: str) -> Dict[str, Any]:
        """VULNERABLE: Deserialize base64 encoded data without validation"""
        # VULNERABLE: Base64 deserialization vulnerability - HIGH
        # VULNERABLE: No base64 validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing base64 data: {base64_data[:100]}...")
            
            # VULNERABLE: Direct base64 deserialization
            decoded_data = base64.b64decode(base64_data)
            
            # VULNERABLE: Try to deserialize as pickle
            try:
                result = pickle.loads(decoded_data)
                deserialization_type = "pickle"
            except:
                # VULNERABLE: Try to deserialize as marshal
                try:
                    result = marshal.loads(decoded_data)
                    deserialization_type = "marshal"
                except:
                    # VULNERABLE: Return raw decoded data
                    result = decoded_data.decode('utf-8', errors='ignore')
                    deserialization_type = "raw"
            
            self.deserialization_history.append({
                "type": f"base64_{deserialization_type}",
                "data": base64_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": f"base64_{deserialization_type}",
                "data": base64_data,
                "deserialized": result,
                "base64_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Base64 deserialization error: {str(e)}")
            return {"error": str(e), "base64_vulnerable": True}
    
    def deserialize_compressed_data(self, compressed_data: bytes) -> Dict[str, Any]:
        """VULNERABLE: Deserialize compressed data without validation"""
        # VULNERABLE: Compressed deserialization vulnerability - HIGH
        # VULNERABLE: No compression validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing compressed data: {len(compressed_data)} bytes")
            
            # VULNERABLE: Direct decompression
            decompressed_data = zlib.decompress(compressed_data)
            
            # VULNERABLE: Try to deserialize decompressed data
            try:
                result = pickle.loads(decompressed_data)
                deserialization_type = "pickle"
            except:
                try:
                    result = marshal.loads(decompressed_data)
                    deserialization_type = "marshal"
                except:
                    result = decompressed_data.decode('utf-8', errors='ignore')
                    deserialization_type = "raw"
            
            self.deserialization_history.append({
                "type": f"compressed_{deserialization_type}",
                "data": compressed_data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": f"compressed_{deserialization_type}",
                "data": compressed_data,
                "deserialized": result,
                "compressed_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Compressed deserialization error: {str(e)}")
            return {"error": str(e), "compressed_vulnerable": True}
    
    def deserialize_custom_format(self, data: str, format_type: str) -> Dict[str, Any]:
        """VULNERABLE: Deserialize custom format data without validation"""
        # VULNERABLE: Custom format deserialization vulnerability - HIGH
        # VULNERABLE: No format validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing custom format {format_type}: {data[:100]}...")
            
            # VULNERABLE: Custom deserialization based on format
            if format_type == "eval":
                # VULNERABLE: Eval deserialization
                result = eval(data)
            elif format_type == "exec":
                # VULNERABLE: Exec deserialization
                exec(data)
                result = "Executed"
            elif format_type == "compile":
                # VULNERABLE: Compile deserialization
                compiled = compile(data, "<string>", "exec")
                exec(compiled)
                result = "Compiled and executed"
            else:
                # VULNERABLE: Default to eval
                result = eval(data)
            
            self.deserialization_history.append({
                "type": f"custom_{format_type}",
                "data": data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": f"custom_{format_type}",
                "data": data,
                "deserialized": result,
                "custom_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Custom deserialization error: {str(e)}")
            return {"error": str(e), "custom_vulnerable": True}
    
    def deserialize_nested_data(self, data: str) -> Dict[str, Any]:
        """VULNERABLE: Deserialize nested data without validation"""
        # VULNERABLE: Nested deserialization vulnerability - CRITICAL
        # VULNERABLE: No nesting validation
        # VULNERABLE: No deserialization restrictions
        
        try:
            logger.info(f"VULNERABLE: Deserializing nested data: {data[:100]}...")
            
            # VULNERABLE: Parse nested structure
            parsed_data = json.loads(data)
            
            # VULNERABLE: Recursively deserialize nested data
            result = self._recursive_deserialize(parsed_data)
            
            self.deserialization_history.append({
                "type": "nested",
                "data": data,
                "result": result,
                "timestamp": time.time()
            })
            
            return {
                "success": True,
                "type": "nested",
                "data": data,
                "deserialized": result,
                "nested_vulnerable": True
            }
            
        except Exception as e:
            logger.error(f"VULNERABLE: Nested deserialization error: {str(e)}")
            return {"error": str(e), "nested_vulnerable": True}
    
    def _xml_to_dict(self, element) -> Dict[str, Any]:
        """VULNERABLE: Convert XML to dict without validation"""
        # VULNERABLE: No XML validation
        # VULNERABLE: No content validation
        
        result = {}
        
        if element.text and element.text.strip():
            result["text"] = element.text.strip()
        
        for child in element:
            child_result = self._xml_to_dict(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result
    
    def _recursive_deserialize(self, data: Any) -> Any:
        """VULNERABLE: Recursively deserialize data without validation"""
        # VULNERABLE: No recursion validation
        # VULNERABLE: No depth limits
        
        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                result[key] = self._recursive_deserialize(value)
            return result
        elif isinstance(data, list):
            return [self._recursive_deserialize(item) for item in data]
        elif isinstance(data, str):
            # VULNERABLE: Try to deserialize string data
            try:
                if data.startswith("pickle:"):
                    return pickle.loads(base64.b64decode(data[7:]))
                elif data.startswith("marshal:"):
                    return marshal.loads(base64.b64decode(data[8:]))
                elif data.startswith("eval:"):
                    return eval(data[5:])
                else:
                    return data
            except:
                return data
        else:
            return data
    
    def get_deserialization_history(self) -> List[Dict[str, Any]]:
        """VULNERABLE: Get deserialization history without access control"""
        # VULNERABLE: No access control
        # VULNERABLE: No data filtering
        # VULNERABLE: No data masking
        
        return self.deserialization_history
