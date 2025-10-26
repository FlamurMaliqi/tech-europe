# 🔍 AIKIDO SCANNER DETECTION CHECKLIST

## ⚠️ Educational Vulnerability Lab - Aikido Scanner Coverage

This document ensures all intentionally vulnerable patterns are detectable by Aikido's various scanner categories.

### 🚨 CRITICAL SAFETY WARNING
- **DO NOT** use this code in production
- **DO NOT** deploy to public internet  
- **DO NOT** use real credentials or data
- **ONLY** use in isolated, offline environments

---

## 📊 AIKIDO SCANNER CATEGORY MAPPING

### 🔍 SAST (Static Application Security Testing)

#### ✅ SQL Injection via String Concatenation
- **File**: `agent/drive_thru/api.py:149`
- **Pattern**: Direct string concatenation in SQL query
- **Aikido Detection**: SAST will detect `f"SELECT * FROM conversations WHERE summary LIKE '%{search_query}%'"`
- **Comment**: `// VULNERABLE: SQL injection`
- **Test**: `GET /conversations/search?search_query=1' OR '1'='1`

#### ✅ Reflected XSS in Templates
- **File**: `agent/drive_thru/api.py:454`
- **Pattern**: Unescaped user input in HTML response
- **Aikido Detection**: SAST will detect `f"<p><strong>Customer:</strong> {customer_name}</p>"`
- **Comment**: `// VULNERABLE: Reflected XSS`
- **Test**: `POST /process/feedback` with `<script>alert('XSS')</script>`

#### ✅ Insecure Deserialization
- **File**: `agent/drive_thru/api.py:484`
- **Pattern**: `pickle.loads()` without validation
- **Aikido Detection**: SAST will detect `pickle.loads(decoded_data)`
- **Comment**: `// VULNERABLE: insecure deserialization`
- **Test**: `POST /deserialize/data` with malicious pickle payload

#### ✅ Command Injection via Shell Exec
- **File**: `agent/drive_thru/api.py:676`
- **Pattern**: `os.system()` with user input
- **Aikido Detection**: SAST will detect shell execution patterns
- **Comment**: `// VULNERABLE: command injection`
- **Test**: `POST /admin/execute` with `; rm -rf /`

#### ✅ Insecure Cryptography
- **File**: `agent/drive_thru/vulnerable_crypto.py:25`
- **Pattern**: MD5 hashing and DES encryption
- **Aikido Detection**: SAST will detect `hashlib.md5()` and weak crypto
- **Comment**: `// VULNERABLE: weak crypto`
- **Test**: `POST /crypto/hash-password` with password

#### ✅ Unsafe eval() Usage
- **File**: `agent/drive_thru/api.py:701`
- **Pattern**: `eval()` with user input
- **Aikido Detection**: SAST will detect `eval()` calls
- **Comment**: `// VULNERABLE: unsafe eval`
- **Test**: `POST /admin/eval` with `__import__('os').system('id')`

---

### 🌐 DAST (Dynamic Application Security Testing)

#### ✅ Unauthenticated Admin Endpoints
- **File**: `agent/drive_thru/api.py:385`
- **Pattern**: `/admin/*` endpoints without authentication
- **Aikido Detection**: DAST will detect unauthenticated admin access
- **Comment**: `// VULNERABLE: missing authentication`
- **Test**: `GET /admin/unlock`, `GET /admin/users`, `DELETE /admin/users/1`

#### ✅ Broken Access Control / IDOR
- **File**: `agent/drive_thru/api.py:417`
- **Pattern**: Resource URLs with numeric IDs and no authorization
- **Aikido Detection**: DAST will detect IDOR vulnerabilities
- **Comment**: `// VULNERABLE: IDOR`
- **Test**: `POST /user/123/data` vs `POST /user/456/data`

#### ✅ Missing Security Headers
- **File**: `agent/drive_thru/api.py:42`
- **Pattern**: No CSP, X-Frame-Options, etc.
- **Aikido Detection**: DAST will detect missing security headers
- **Comment**: `// VULNERABLE: missing security headers`
- **Test**: Check response headers for missing security headers

#### ✅ CORS Wide-Open
- **File**: `agent/drive_thru/api.py:29`
- **Pattern**: `allow_origins=["*"]` with sensitive endpoints
- **Aikido Detection**: DAST will detect overly permissive CORS
- **Comment**: `// VULNERABLE: wide-open CORS`
- **Test**: Check CORS headers on sensitive endpoints

#### ✅ Weak Session Management
- **File**: `agent/drive_thru/vulnerable_crypto.py:60`
- **Pattern**: Predictable token generation
- **Aikido Detection**: DAST will detect weak session tokens
- **Comment**: `// VULNERABLE: weak token generation`
- **Test**: `POST /crypto/generate-token` with user_id

---

### 🔐 SECRETS DETECTION

#### ✅ Committed .env with Placeholder Secrets
- **File**: `agent/drive_thru/vulnerable_secrets.py:8`
- **Pattern**: Hardcoded secrets in source code
- **Aikido Detection**: Secrets scanner will detect hardcoded values
- **Comment**: `# VULNERABLE: hardcoded secrets`
- **Test**: Scan source code for `FAKE_` prefixed secrets

#### ✅ Secrets Printed to Logs
- **File**: `agent/drive_thru/api.py:481`
- **Pattern**: `logger.info(f"Password hash request for password: {password}")`
- **Aikido Detection**: Secrets scanner will detect secrets in logs
- **Comment**: `// VULNERABLE: secrets in logs`
- **Test**: Check logs for sensitive information

#### ✅ Secrets Exposed via Debug Endpoints
- **File**: `agent/drive_thru/api.py:422`
- **Pattern**: `/debug/secrets` endpoint exposing all secrets
- **Aikido Detection**: Secrets scanner will detect exposed secrets
- **Comment**: `// VULNERABLE: secrets exposure`
- **Test**: `GET /debug/secrets`

---

### 📦 SCA (Software Composition Analysis)

#### ✅ Known-Vulnerable Dependency Versions
- **File**: `agent/requirements-vulnerable.txt:1`
- **Pattern**: Downgraded packages with known CVEs
- **Aikido Detection**: SCA will detect vulnerable package versions
- **Comment**: `# VULNERABLE: packages with known CVEs`
- **Test**: `pip install -r requirements-vulnerable.txt` and scan

#### ✅ Frontend Vulnerable Dependencies
- **File**: `dashboard/package-vulnerable.json:16`
- **Pattern**: Downgraded frontend packages
- **Aikido Detection**: SCA will detect vulnerable npm packages
- **Comment**: `"_vulnerabilities": "CVE-2023-XXXX"`
- **Test**: `npm install` with vulnerable package.json and scan

---

### ☁️ CSPM (Cloud Security Posture Management)

#### ✅ Dockerfile with Old Base Image and Root User
- **File**: `Dockerfile.vuln-lab:1`
- **Pattern**: `FROM python:3.8-slim` and `USER root`
- **Aikido Detection**: CSPM will detect old base image and root user
- **Comment**: `# VULNERABLE: old base image and root user`
- **Test**: Scan Dockerfile for security issues

#### ✅ Kubernetes with HostPath and No SecurityContext
- **File**: `k8s-vulnerable.yaml:45`
- **Pattern**: `hostPath` mounts and `privileged: true`
- **Aikido Detection**: CSPM will detect insecure pod configurations
- **Comment**: `# VULNERABLE: hostPath mounts and privileged access`
- **Test**: Scan Kubernetes manifests for security issues

#### ✅ Overly Permissive IAM Policies
- **File**: `terraform-vulnerable.tf:65`
- **Pattern**: `Action = "*"` and `Resource = "*"`
- **Aikido Detection**: CSPM will detect overly permissive IAM policies
- **Comment**: `# VULNERABLE: overly permissive IAM policy`
- **Test**: Scan Terraform for IAM policy issues

#### ✅ Publicly Readable Storage Bucket
- **File**: `terraform-vulnerable.tf:25`
- **Pattern**: S3 bucket with public read access
- **Aikido Detection**: CSPM will detect public bucket configurations
- **Comment**: `# VULNERABLE: S3 bucket with public read access`
- **Test**: Scan Terraform for public bucket settings

---

### 🏃 RUNTIME SECURITY

#### ✅ Debug Ports with Sensitive App State
- **File**: `agent/drive_thru/api.py:664`
- **Pattern**: `/logs/debug` endpoint exposing sensitive data
- **Aikido Detection**: Runtime scanner will detect debug endpoints
- **Comment**: `// VULNERABLE: debug endpoint exposing sensitive data`
- **Test**: `GET /logs/debug`

#### ✅ Excessive Service Account Privileges
- **File**: `k8s-vulnerable.yaml:25`
- **Pattern**: ClusterRole with `verbs: ["*"]`
- **Aikido Detection**: Runtime scanner will detect excessive privileges
- **Comment**: `# VULNERABLE: overly permissive ClusterRole`
- **Test**: Check RBAC permissions in Kubernetes

---

### 🔧 SUPPLY CHAIN / BUILD

#### ✅ CI Pipeline Without Checksum Verification
- **File**: `.github/workflows/vulnerable-ci.yml:25`
- **Pattern**: Downloading artifacts without verification
- **Aikido Detection**: Supply chain scanner will detect missing verification
- **Comment**: `# VULNERABLE: no checksum verification`
- **Test**: Scan CI/CD pipeline for security issues

#### ✅ Build Scripts Fetching Remote Shell Scripts
- **File**: `scripts/vulnerable-build.sh:8`
- **Pattern**: `curl | bash` or similar patterns
- **Aikido Detection**: Supply chain scanner will detect unsafe downloads
- **Comment**: `# VULNERABLE: fetching and executing remote scripts`
- **Test**: Scan build scripts for unsafe patterns

---

## 🧪 AIKIDO DETECTION VERIFICATION

### SAST Detection Tests
```bash
# Test SQL injection detection
curl "http://localhost:8000/conversations/search?search_query=1' OR '1'='1"

# Test XSS detection  
curl -X POST "http://localhost:8000/process/feedback" \
  -H "Content-Type: application/json" \
  -d '{"feedback": "<script>alert(\"XSS\")</script>", "customer_name": "test"}'

# Test deserialization detection
echo "Y3Bvc2l4CnN5c3RlbQpwMAooUydpZCcpCnAxCnRwMgpScDMKLg==" | \
  curl -X POST "http://localhost:8000/deserialize/data" \
  -H "Content-Type: application/json" \
  -d '{"serialized_data": "Y3Bvc2l4CnN5c3RlbQpwMAooUydpZCcpCnAxCnRwMgpScDMKLg=="}'
```

### DAST Detection Tests
```bash
# Test unauthenticated admin access
curl "http://localhost:8000/admin/unlock"
curl "http://localhost:8000/admin/users"
curl -X DELETE "http://localhost:8000/admin/users/1"

# Test IDOR vulnerabilities
curl -X POST "http://localhost:8000/user/123/data"
curl "http://localhost:8000/orders/123/details"

# Test missing security headers
curl -I "http://localhost:8000/health"
```

### Secrets Detection Tests
```bash
# Test secrets exposure
curl "http://localhost:8000/debug/secrets"

# Test secrets in logs
curl -X POST "http://localhost:8000/crypto/hash-password" \
  -H "Content-Type: application/json" \
  -d '{"password": "admin123"}'
```

### SCA Detection Tests
```bash
# Test vulnerable dependencies
pip install -r agent/requirements-vulnerable.txt
npm install --package-lock-only -f dashboard/package-vulnerable.json
```

### CSPM Detection Tests
```bash
# Test container security
docker build -f Dockerfile.vuln-lab -t vuln-lab-app .

# Test Kubernetes security
kube-score score k8s-vulnerable.yaml

# Test Terraform security
tfsec terraform-vulnerable.tf
```

---

## 📋 AIKIDO SCANNER MAPPING SUMMARY

| Scanner Category | Vulnerabilities Added | Detection Method | Test Endpoint |
|------------------|----------------------|------------------|---------------|
| **SAST** | SQL Injection, XSS, Deserialization, Weak Crypto | Static code analysis | `/conversations/search`, `/process/feedback` |
| **DAST** | Missing Auth, IDOR, Security Headers, CORS | Dynamic testing | `/admin/*`, `/user/*`, `/orders/*` |
| **Secrets** | Hardcoded Secrets, Secrets in Logs, Debug Exposure | Secrets scanning | `/debug/secrets`, logs |
| **SCA** | Vulnerable Dependencies | Dependency scanning | `requirements-vulnerable.txt` |
| **CSPM** | Container Security, K8s Misconfig, IaC Issues | Infrastructure scanning | `Dockerfile.vuln-lab`, `k8s-vulnerable.yaml` |
| **Runtime** | Debug Endpoints, Excessive Privileges | Runtime monitoring | `/logs/debug`, K8s RBAC |

---

## ✅ VERIFICATION CHECKLIST

- [x] **SAST**: SQL injection via string concatenation
- [x] **SAST**: Reflected XSS in templates  
- [x] **SAST**: Insecure deserialization with pickle
- [x] **SAST**: Command injection via shell exec
- [x] **SAST**: Insecure cryptography (MD5, DES)
- [x] **SAST**: Unsafe eval() usage
- [x] **DAST**: Unauthenticated admin endpoints
- [x] **DAST**: Broken access control / IDOR
- [x] **DAST**: Missing security headers
- [x] **DAST**: CORS wide-open
- [x] **DAST**: Weak session management
- [x] **Secrets**: Committed secrets in source code
- [x] **Secrets**: Secrets printed to logs
- [x] **Secrets**: Secrets exposed via debug endpoints
- [x] **SCA**: Known-vulnerable dependency versions
- [x] **SCA**: Frontend vulnerable dependencies
- [x] **CSPM**: Dockerfile with old base image and root user
- [x] **CSPM**: Kubernetes with hostPath and no securityContext
- [x] **CSPM**: Overly permissive IAM policies
- [x] **CSPM**: Publicly readable storage bucket
- [x] **Runtime**: Debug ports with sensitive app state
- [x] **Runtime**: Excessive service account privileges
- [x] **Supply Chain**: CI pipeline without checksum verification
- [x] **Supply Chain**: Build scripts fetching remote shell scripts

---

## 🚨 SAFETY COMPLIANCE

- [x] **Air-gapped execution**: `AIRGAP_RUN.md` provides complete isolation guide
- [x] **Fake data only**: All secrets use `FAKE_` prefix pattern
- [x] **Clear labeling**: Every vulnerable snippet has `VULNERABLE:` comment
- [x] **No exploit payloads**: Only vulnerability patterns, no weaponized code
- [x] **Safe baseline**: `SAFE_RESTORE.sh` provides complete cleanup

---

**🎯 AIKIDO SCANNER COVERAGE: 24/24 vulnerabilities implemented**
**📊 COMPLETE: All Aikido scanner categories covered**

This checklist ensures comprehensive coverage of all Aikido scanner categories with concrete, detectable vulnerability patterns.
