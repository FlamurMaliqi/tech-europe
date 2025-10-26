# 🔍 VULNERABILITY CHECKLIST

## ⚠️ Educational Vulnerability Lab - Complete Inventory

This document provides a comprehensive checklist of all intentionally vulnerable patterns added to this repository for educational purposes.

### 🚨 CRITICAL SAFETY WARNING
- **DO NOT** use this code in production
- **DO NOT** deploy to public internet
- **DO NOT** use real credentials or data
- **ONLY** use in isolated, offline environments

---

## 📊 Vulnerability Categories

### 🔍 SAST (Static Application Security Testing)

#### Advanced SQL Injection
- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:25`
- **Vulnerability**: Dynamic SQL query execution with string formatting
- **Severity**: Critical
- **Description**: Direct string formatting into SQL queries allowing arbitrary SQL execution
- **Test**: `POST /advanced-sql/dynamic-query` with malicious query template

- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:45`
- **Vulnerability**: UNION-based SQL injection
- **Severity**: Critical
- **Description**: UNION injection allowing data extraction from other tables
- **Test**: `POST /advanced-sql/union-injection` with UNION payload

- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:65`
- **Vulnerability**: Boolean-based blind SQL injection
- **Severity**: Critical
- **Description**: Blind SQL injection using boolean conditions
- **Test**: `POST /advanced-sql/blind-injection` with boolean payload

- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:85`
- **Vulnerability**: Time-based blind SQL injection
- **Severity**: Critical
- **Description**: Blind SQL injection using time delays
- **Test**: `POST /advanced-sql/blind-injection` with time-based payload

- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:105`
- **Vulnerability**: Error-based SQL injection
- **Severity**: Critical
- **Description**: SQL injection using error messages to extract data
- **Test**: `POST /advanced-sql/error-injection` with error-based payload

- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:125`
- **Vulnerability**: Stacked queries SQL injection
- **Severity**: Critical
- **Description**: Multiple SQL statements execution in single query
- **Test**: `POST /advanced-sql/stacked-queries` with stacked payload

- **File**: `agent/drive_thru/vulnerable_advanced_sql.py:145`
- **Vulnerability**: Second-order SQL injection
- **Severity**: Critical
- **Description**: SQL injection through stored malicious data
- **Test**: `POST /advanced-sql/second-order` with second-order payload

#### XXE (XML External Entity) Vulnerabilities
- **File**: `agent/drive_thru/vulnerable_xxe.py:25`
- **Vulnerability**: XML External Entity processing
- **Severity**: Critical
- **Description**: Processing external entities in XML without restrictions
- **Test**: `POST /xxe/parse-external-entities` with XXE payload

- **File**: `agent/drive_thru/vulnerable_xxe.py:45`
- **Vulnerability**: File-based XXE
- **Severity**: Critical
- **Description**: File access through XML external entities
- **Test**: `POST /xxe/parse-file-entities` with file:// entity

- **File**: `agent/drive_thru/vulnerable_xxe.py:65`
- **Vulnerability**: HTTP-based XXE
- **Severity**: Critical
- **Description**: HTTP requests through XML external entities
- **Test**: `POST /xxe/parse-http-entities` with http:// entity

- **File**: `agent/drive_thru/vulnerable_xxe.py:85`
- **Vulnerability**: Parameter entity XXE
- **Severity**: Critical
- **Description**: Parameter entity processing in XML
- **Test**: `POST /xxe/parse-parameter-entities` with parameter entity

- **File**: `agent/drive_thru/vulnerable_xxe.py:105`
- **Vulnerability**: Blind XXE
- **Severity**: Critical
- **Description**: Blind XXE without direct response
- **Test**: `POST /xxe/parse-blind-xxe` with blind XXE payload

#### SSRF (Server-Side Request Forgery) Vulnerabilities
- **File**: `agent/drive_thru/vulnerable_ssrf.py:25`
- **Vulnerability**: Unrestricted HTTP requests
- **Severity**: Critical
- **Description**: Making HTTP requests to any URL without restrictions
- **Test**: `POST /ssrf/unrestricted-request` with malicious URL

- **File**: `agent/drive_thru/vulnerable_ssrf.py:45`
- **Vulnerability**: Internal service requests
- **Severity**: Critical
- **Description**: Requests to internal services without protection
- **Test**: `POST /ssrf/internal-request` with internal endpoint

- **File**: `agent/drive_thru/vulnerable_ssrf.py:65`
- **Vulnerability**: Cloud metadata requests
- **Severity**: Critical
- **Description**: Requests to cloud metadata services
- **Test**: `POST /ssrf/cloud-metadata` with cloud provider

- **File**: `agent/drive_thru/vulnerable_ssrf.py:85`
- **Vulnerability**: File protocol requests
- **Severity**: Critical
- **Description**: File:// protocol requests for file access
- **Test**: `POST /ssrf/file-protocol` with file:// URL

- **File**: `agent/drive_thru/vulnerable_ssrf.py:105`
- **Vulnerability**: Gopher protocol requests
- **Severity**: Critical
- **Description**: Gopher:// protocol requests
- **Test**: `POST /ssrf/gopher-protocol` with gopher:// URL

- **File**: `agent/drive_thru/vulnerable_ssrf.py:125`
- **Vulnerability**: FTP protocol requests
- **Severity**: Critical
- **Description**: FTP:// protocol requests
- **Test**: `POST /ssrf/ftp-protocol` with ftp:// URL

- **File**: `agent/drive_thru/vulnerable_ssrf.py:145`
- **Vulnerability**: Direct socket connections
- **Severity**: Critical
- **Description**: Direct socket connections to any host/port
- **Test**: `POST /ssrf/socket-connection` with host/port

#### Advanced Remote Code Execution Vulnerabilities
- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:25`
- **Vulnerability**: Shell command execution
- **Severity**: Critical
- **Description**: Direct shell command execution without validation
- **Test**: `POST /advanced-rce/shell-command` with malicious command

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:45`
- **Vulnerability**: Python code execution
- **Severity**: Critical
- **Description**: Direct Python code execution without validation
- **Test**: `POST /advanced-rce/python-code` with malicious code

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:65`
- **Vulnerability**: Eval expression execution
- **Severity**: Critical
- **Description**: Eval expression execution without validation
- **Test**: `POST /advanced-rce/eval-expression` with malicious expression

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:85`
- **Vulnerability**: Compile code execution
- **Severity**: Critical
- **Description**: Compile and execute code without validation
- **Test**: `POST /advanced-rce/compile-code` with malicious code

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:105`
- **Vulnerability**: Pickle deserialization
- **Severity**: Critical
- **Description**: Pickle deserialization without validation
- **Test**: `POST /advanced-rce/pickle-deserialization` with malicious pickle

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:125`
- **Vulnerability**: Marshal deserialization
- **Severity**: Critical
- **Description**: Marshal deserialization without validation
- **Test**: `POST /advanced-rce/marshal-deserialization` with malicious marshal

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:145`
- **Vulnerability**: Dynamic module import
- **Severity**: Critical
- **Description**: Dynamic module import without validation
- **Test**: `POST /advanced-rce/dynamic-import` with malicious module

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:165`
- **Vulnerability**: File operations
- **Severity**: Critical
- **Description**: File operations without validation
- **Test**: `POST /advanced-rce/file-operations` with malicious operation

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:185`
- **Vulnerability**: Network operations
- **Severity**: Critical
- **Description**: Network operations without validation
- **Test**: `POST /advanced-rce/network-operations` with malicious network request

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:205`
- **Vulnerability**: System commands
- **Severity**: Critical
- **Description**: System commands without validation
- **Test**: `POST /advanced-rce/system-commands` with malicious command

- **File**: `agent/drive_thru/vulnerable_advanced_rce.py:225`
- **Vulnerability**: Popen commands
- **Severity**: Critical
- **Description**: Popen commands without validation
- **Test**: `POST /advanced-rce/popen-commands` with malicious command

#### Advanced Insecure Deserialization Vulnerabilities
- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:25`
- **Vulnerability**: Pickle deserialization
- **Severity**: Critical
- **Description**: Pickle deserialization without validation
- **Test**: `POST /advanced-deserialization/pickle` with malicious pickle data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:45`
- **Vulnerability**: Marshal deserialization
- **Severity**: Critical
- **Description**: Marshal deserialization without validation
- **Test**: `POST /advanced-deserialization/marshal` with malicious marshal data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:65`
- **Vulnerability**: JSON deserialization
- **Severity**: High
- **Description**: JSON deserialization without validation
- **Test**: `POST /advanced-deserialization/json` with malicious JSON data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:85`
- **Vulnerability**: YAML deserialization
- **Severity**: Critical
- **Description**: YAML deserialization without validation
- **Test**: `POST /advanced-deserialization/yaml` with malicious YAML data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:105`
- **Vulnerability**: XML deserialization
- **Severity**: High
- **Description**: XML deserialization without validation
- **Test**: `POST /advanced-deserialization/xml` with malicious XML data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:125`
- **Vulnerability**: Base64 deserialization
- **Severity**: High
- **Description**: Base64 deserialization without validation
- **Test**: `POST /advanced-deserialization/base64` with malicious base64 data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:145`
- **Vulnerability**: Compressed deserialization
- **Severity**: High
- **Description**: Compressed deserialization without validation
- **Test**: `POST /advanced-deserialization/compressed` with malicious compressed data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:165`
- **Vulnerability**: Custom format deserialization
- **Severity**: High
- **Description**: Custom format deserialization without validation
- **Test**: `POST /advanced-deserialization/custom-format` with malicious custom data

- **File**: `agent/drive_thru/vulnerable_advanced_deserialization.py:185`
- **Vulnerability**: Nested deserialization
- **Severity**: Critical
- **Description**: Nested deserialization without validation
- **Test**: `POST /advanced-deserialization/nested` with malicious nested data

#### Advanced Path Traversal Vulnerabilities
- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:25`
- **Vulnerability**: File read with path traversal
- **Severity**: Critical
- **Description**: Reading files with path traversal without validation
- **Test**: `POST /advanced-path-traversal/read-file` with ../../../etc/passwd

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:45`
- **Vulnerability**: File write with path traversal
- **Severity**: Critical
- **Description**: Writing files with path traversal without validation
- **Test**: `POST /advanced-path-traversal/write-file` with ../../../tmp/malicious

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:65`
- **Vulnerability**: File deletion with path traversal
- **Severity**: Critical
- **Description**: Deleting files with path traversal without validation
- **Test**: `POST /advanced-path-traversal/delete-file` with ../../../important/file

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:85`
- **Vulnerability**: Directory listing with path traversal
- **Severity**: Critical
- **Description**: Listing directories with path traversal without validation
- **Test**: `POST /advanced-path-traversal/list-directory` with ../../../etc

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:105`
- **Vulnerability**: File copy with path traversal
- **Severity**: Critical
- **Description**: Copying files with path traversal without validation
- **Test**: `POST /advanced-path-traversal/copy-file` with ../../../etc/passwd

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:125`
- **Vulnerability**: File move with path traversal
- **Severity**: Critical
- **Description**: Moving files with path traversal without validation
- **Test**: `POST /advanced-path-traversal/move-file` with ../../../etc/passwd

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:145`
- **Vulnerability**: Directory creation with path traversal
- **Severity**: Critical
- **Description**: Creating directories with path traversal without validation
- **Test**: `POST /advanced-path-traversal/create-directory` with ../../../tmp/malicious

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:165`
- **Vulnerability**: Directory removal with path traversal
- **Severity**: Critical
- **Description**: Removing directories with path traversal without validation
- **Test**: `POST /advanced-path-traversal/remove-directory` with ../../../important

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:185`
- **Vulnerability**: File info with path traversal
- **Severity**: Critical
- **Description**: Getting file info with path traversal without validation
- **Test**: `POST /advanced-path-traversal/file-info` with ../../../etc/passwd

- **File**: `agent/drive_thru/vulnerable_advanced_path_traversal.py:205`
- **Vulnerability**: File execution with path traversal
- **Severity**: Critical
- **Description**: Executing files with path traversal without validation
- **Test**: `POST /advanced-path-traversal/execute-file` with ../../../bin/malicious

#### SQL Injection
- **File**: `agent/drive_thru/api.py:149`
- **Vulnerability**: Direct string concatenation into SQL query
- **Severity**: High
- **Description**: User input is directly concatenated into SQL query without parameterization
- **Test**: `GET /conversations/search?search_query=1' OR '1'='1`

#### Reflected XSS
- **File**: `agent/drive_thru/api.py:454`
- **Vulnerability**: No input sanitization or output encoding
- **Severity**: Medium
- **Description**: User input is directly output in HTML without sanitization
- **Test**: `POST /process/feedback` with `<script>alert('XSS')</script>`

#### Insecure Deserialization
- **File**: `agent/drive_thru/api.py:484`
- **Vulnerability**: Using pickle for deserialization without validation
- **Severity**: Critical
- **Description**: Arbitrary code execution through malicious pickle data
- **Test**: `POST /deserialize/data` with malicious pickle payload

#### Weak Crypto
- **File**: `agent/drive_thru/vulnerable_crypto.py:25`
- **Vulnerability**: MD5 password hashing
- **Severity**: High
- **Description**: MD5 is cryptographically broken and fast
- **Test**: `POST /crypto/hash-password` with password

- **File**: `agent/drive_thru/vulnerable_crypto.py:35`
- **Vulnerability**: DES encryption with weak key
- **Severity**: High
- **Description**: DES has weak 56-bit key and is deprecated
- **Test**: `POST /crypto/encrypt` with data

#### Hardcoded Secrets
- **File**: `agent/drive_thru/vulnerable_secrets.py:8`
- **Vulnerability**: Hardcoded secrets in source code
- **Severity**: Critical
- **Description**: Secrets are hardcoded in source code instead of using secure storage
- **Test**: Review source code for hardcoded values

---

### 🌐 DAST (Dynamic Application Security Testing)

#### Missing Authentication
- **File**: `agent/drive_thru/api.py:385`
- **Vulnerability**: No authentication required for admin functions
- **Severity**: High
- **Description**: Admin endpoints are accessible without authentication
- **Test**: `GET /admin/unlock`, `GET /admin/users`, `DELETE /admin/users/1`

#### IDOR (Insecure Direct Object Reference)
- **File**: `agent/drive_thru/api.py:417`
- **Vulnerability**: No authorization check for user data access
- **Severity**: Medium
- **Description**: Users can access any user's data by changing user ID
- **Test**: `POST /user/123/data` vs `POST /user/456/data`

- **File**: `agent/drive_thru/api.py:587`
- **Vulnerability**: No authorization check for order access
- **Severity**: Medium
- **Description**: Users can access any order by changing order ID
- **Test**: `GET /orders/123/details` vs `GET /orders/456/details`

#### Missing Security Headers
- **File**: `agent/drive_thru/api.py:42`
- **Vulnerability**: No security headers implemented
- **Severity**: Medium
- **Description**: Missing CSP, X-Frame-Options, X-Content-Type-Options, etc.
- **Test**: Check response headers for missing security headers

---

### 📦 SCA (Software Composition Analysis)

#### Vulnerable Dependencies
- **File**: `agent/requirements-vulnerable.txt`
- **Vulnerability**: Packages with known CVEs
- **Severity**: High
- **Description**: Downgraded packages to versions with known vulnerabilities
- **Test**: Run `pip install -r requirements-vulnerable.txt` and scan

- **File**: `dashboard/package-vulnerable.json`
- **Vulnerability**: Frontend packages with known CVEs
- **Severity**: High
- **Description**: Downgraded frontend packages to vulnerable versions
- **Test**: Run `npm install` with vulnerable package.json and scan

---

### 🔐 Secrets Scanning

#### Secrets in Logs
- **File**: `agent/drive_thru/api.py:481`
- **Vulnerability**: Logging sensitive data in plaintext
- **Severity**: High
- **Description**: Passwords, tokens, and sensitive data logged in plaintext
- **Test**: Check logs for sensitive information

- **File**: `agent/drive_thru/data_pipeline.py:40`
- **Vulnerability**: Logging environment variables
- **Severity**: High
- **Description**: Database URLs and API keys logged in plaintext
- **Test**: Check logs for environment variables

#### Secrets Exposure
- **File**: `agent/drive_thru/api.py:422`
- **Vulnerability**: Exposing all secrets in debug endpoint
- **Severity**: Critical
- **Description**: All secrets exposed through debug endpoint
- **Test**: `GET /debug/secrets`

---

### ☁️ CSPM (Cloud Security Posture Management)

#### Container Security
- **File**: `Dockerfile.vuln-lab:4`
- **Vulnerability**: Running as root user
- **Severity**: High
- **Description**: Container runs as root user instead of non-privileged user
- **Test**: Check container user with `docker exec -it container id`

- **File**: `Dockerfile.vuln-lab:1`
- **Vulnerability**: Old base image with known vulnerabilities
- **Severity**: Medium
- **Description**: Using outdated base image with known security issues
- **Test**: Scan base image for vulnerabilities

#### Kubernetes Misconfigurations
- **File**: `k8s-vulnerable.yaml:25`
- **Vulnerability**: Overly permissive ClusterRole
- **Severity**: Critical
- **Description**: ClusterRole with full access to all resources
- **Test**: Check RBAC permissions

- **File**: `k8s-vulnerable.yaml:45`
- **Vulnerability**: Privileged containers
- **Severity**: High
- **Description**: Containers running with privileged access
- **Test**: Check pod security context

#### Terraform Misconfigurations
- **File**: `terraform-vulnerable.tf:25`
- **Vulnerability**: S3 bucket with public read access
- **Severity**: High
- **Description**: S3 bucket allows public read access
- **Test**: Check S3 bucket policy

- **File**: `terraform-vulnerable.tf:45`
- **Vulnerability**: Security group allowing all traffic
- **Severity**: Critical
- **Description**: Security group allows all ingress and egress traffic
- **Test**: Check security group rules

- **File**: `terraform-vulnerable.tf:65`
- **Vulnerability**: IAM policy with full access
- **Severity**: Critical
- **Description**: IAM policy grants full access to all resources
- **Test**: Check IAM policy permissions

---

### 🏃 Runtime Security

#### Debug Endpoints
- **File**: `agent/drive_thru/api.py:664`
- **Vulnerability**: Debug endpoint exposing sensitive data
- **Severity**: High
- **Description**: Debug endpoint exposes logs with sensitive information
- **Test**: `GET /logs/debug`

#### Privileged Containers
- **File**: `k8s-vulnerable.yaml:45`
- **Vulnerability**: Containers running with privileged access
- **Severity**: High
- **Description**: Containers have privileged access to host system
- **Test**: Check pod security context

#### Host Access
- **File**: `k8s-vulnerable.yaml:45`
- **Vulnerability**: Host path mounts
- **Severity**: High
- **Description**: Containers mount host directories
- **Test**: Check volume mounts

---

## 🧪 Testing Instructions

### 1. SAST Testing
```bash
# Run static analysis tools
bandit -r agent/
semgrep --config=auto agent/
```

### 2. DAST Testing
```bash
# Test API endpoints
curl -X GET "http://localhost:8000/admin/unlock"
curl -X POST "http://localhost:8000/user/123/data"
curl -X GET "http://localhost:8000/orders/123/details"
```

### 3. SCA Testing
```bash
# Scan Python dependencies
safety check -r agent/requirements-vulnerable.txt
pip-audit -r agent/requirements-vulnerable.txt

# Scan Node.js dependencies
npm audit --audit-level=moderate
```

### 4. Secrets Scanning
```bash
# Scan for secrets
trufflehog filesystem agent/
git-secrets --scan
```

### 5. CSPM Testing
```bash
# Scan Kubernetes manifests
kube-score score k8s-vulnerable.yaml
kubeaudit all -f k8s-vulnerable.yaml

# Scan Terraform configurations
tfsec terraform-vulnerable.tf
checkov -f terraform-vulnerable.tf
```

---

## 📈 Scanner Mapping

| Vulnerability Type | Aikido Scanner | Description |
|-------------------|----------------|-------------|
| SQL Injection | SAST | Static analysis of SQL queries |
| XSS | SAST | Static analysis of output encoding |
| Deserialization | SAST | Static analysis of deserialization |
| Weak Crypto | SAST | Static analysis of crypto usage |
| Missing Auth | DAST | Dynamic testing of authentication |
| IDOR | DAST | Dynamic testing of authorization |
| Security Headers | DAST | Dynamic testing of HTTP headers |
| Vulnerable Deps | SCA | Software composition analysis |
| Secrets in Logs | Secrets | Secrets scanning in logs |
| Secrets Exposure | Secrets | Secrets scanning in code |
| Container Security | CSPM | Container security posture |
| IAM Misconfig | CSPM | Cloud security posture |
| Runtime Security | Runtime | Runtime security monitoring |

---

## 🔄 Restore Instructions

After testing, restore the repository to a safe state:

```bash
# Run the safe restore script
./SAFE_RESTORE.sh

# Or manually restore
git checkout main
git clean -fd
```

---

## 📚 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Controls](https://www.cisecurity.org/controls/)

---

**Remember: This is a learning tool, not a production system!**
