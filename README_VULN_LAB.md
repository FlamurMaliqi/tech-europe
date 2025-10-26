# ⚠️ VULNERABILITY LAB - EDUCATIONAL PURPOSES ONLY ⚠️

## 🚨 CRITICAL SAFETY WARNING 🚨

**THIS REPOSITORY CONTAINS INTENTIONALLY VULNERABLE CODE FOR EDUCATIONAL PURPOSES ONLY**

### ⛔ NEVER DEPLOY TO PRODUCTION ⛔
- **DO NOT** deploy this code to any public-facing environment
- **DO NOT** use real credentials, API keys, or production data
- **DO NOT** connect to real external services
- **DO NOT** run this on systems with access to sensitive data

### 🎯 Purpose
This repository has been modified to include intentionally vulnerable patterns for:
- Security training and education
- Vulnerability assessment practice
- SAST/DAST/SCA scanner testing
- Controlled penetration testing exercises
- Security awareness training

### 🔒 Safety Measures
- All secrets use `FAKE_` prefix pattern
- Vulnerabilities are clearly marked with `// VULNERABLE:` comments
- Designed for isolated, offline environments only
- No real external service connections

### 🏃‍♂️ Quick Start (Safe Mode)
1. **Run in isolated container**: See `AIRGAP_RUN.md`
2. **Use fake credentials only**: All secrets are clearly marked as fake
3. **Never expose to internet**: Run only on localhost/isolated networks
4. **Restore safe state**: Use `SAFE_RESTORE.sh` when done

### 📋 Vulnerability Categories Included
- **SAST**: SQL injection, XSS, deserialization, weak crypto
- **DAST**: Missing auth, IDOR, security headers
- **SCA**: Vulnerable dependencies with known CVEs
- **Secrets**: Fake credentials in logs/configs
- **CSPM**: Container/IaC misconfigurations
- **Runtime**: Debug endpoints, permissive settings

### 🔄 Restoring Safe State
After testing, restore the repository to a safe state:
```bash
./SAFE_RESTORE.sh
```

### 📚 Documentation
- `VULN_CHECKLIST.md` - Complete vulnerability inventory
- `vuln_manifest.json` - Structured vulnerability data
- `AIRGAP_RUN.md` - Safe execution instructions

### ⚖️ Legal Notice
This code is provided for educational purposes only. Users are responsible for:
- Ensuring safe, isolated execution environments
- Not using this code in production systems
- Following all applicable laws and regulations
- Obtaining proper authorization before testing

### 🆘 Emergency Contacts
If you accidentally expose this code to production:
1. **IMMEDIATELY** disconnect from network
2. **DO NOT** commit any real credentials
3. **RESTORE** from safe backup immediately
4. **REVIEW** all changes before re-deployment

---

**Remember: This is a learning tool, not a production system!**
