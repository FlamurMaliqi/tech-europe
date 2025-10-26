# 🔒 AIRGAP RUN - ISOLATED EXECUTION GUIDE

## 🎯 Purpose
This guide explains how to safely run the vulnerability lab in a completely isolated environment with no external network access.

## 🐳 Docker Isolation (Recommended)

### 1. Create Isolated Docker Network
```bash
# Create isolated network with no internet access
docker network create --internal vuln-lab-network
```

### 2. Build Application Container
```bash
# Build the application (see Dockerfile.vuln-lab)
docker build -f Dockerfile.vuln-lab -t vuln-lab-app .
```

### 3. Run in Isolated Environment
```bash
# Run with no network access except internal communication
docker run --rm -it \
  --network vuln-lab-network \
  --name vuln-lab-container \
  -p 8000:8000 \
  -p 3000:3000 \
  vuln-lab-app
```

### 4. Access Application
- API: `http://localhost:8000`
- Dashboard: `http://localhost:3000`
- **No external internet access** from container

## 🖥️ Virtual Machine Isolation

### 1. Create VM with No Network
```bash
# Using VirtualBox (example)
VBoxManage createvm --name vuln-lab-vm --ostype Linux_64
VBoxManage modifyvm vuln-lab-vm --memory 2048 --cpus 2
# DO NOT attach any network adapters
```

### 2. Install Dependencies Offline
```bash
# Copy all dependencies to VM via USB/shared folder
# Install Python, Node.js, and dependencies offline
```

### 3. Run Application
```bash
# Start services (no network access)
cd /path/to/tech-europe-secure
python agent/scripts/run_api.py &
cd dashboard && npm run dev &
```

## 🏠 Local Airgap Setup

### 1. Disable Network Interfaces
```bash
# macOS
sudo ifconfig en0 down
sudo ifconfig en1 down

# Linux
sudo ifdown eth0
sudo ifdown wlan0
```

### 2. Run Application
```bash
# Start services locally
cd agent && python scripts/run_api.py &
cd dashboard && npm run dev &
```

### 3. Re-enable Network (After Testing)
```bash
# macOS
sudo ifconfig en0 up
sudo ifconfig en1 up

# Linux
sudo ifup eth0
sudo ifup wlan0
```

## 🔧 Environment Variables for Lab Mode

### Required Lab Environment
```bash
# Set lab mode to enable vulnerable endpoints
export APP_ENV=lab
export VULN_LAB_MODE=true
export DEBUG_MODE=true

# Fake credentials (never use real ones)
export FAKE_DATABASE_URL=sqlite:///fake_lab.db
export FAKE_API_KEY=FAKE_1234567890abcdef
export FAKE_SECRET_TOKEN=FAKE_vulnerable_token_for_lab_only
```

## 🚨 Safety Checklist

### Before Running
- [ ] Network interfaces disabled or container isolated
- [ ] No real credentials in environment
- [ ] Lab mode environment variables set
- [ ] Safe restore script available
- [ ] No production data accessible

### During Testing
- [ ] Monitor for any external network attempts
- [ ] Verify no real credentials are logged
- [ ] Check that vulnerabilities are contained
- [ ] Document findings for learning

### After Testing
- [ ] Stop all services
- [ ] Run `SAFE_RESTORE.sh`
- [ ] Clear any temporary data
- [ ] Re-enable network if needed
- [ ] Review logs for any issues

## 🐛 Debugging in Airgap

### Check Network Isolation
```bash
# Should fail in airgap environment
curl -I https://google.com
ping 8.8.8.8

# Should work locally
curl -I http://localhost:8000/health
```

### Verify Lab Mode
```bash
# Check environment variables
echo $APP_ENV
echo $VULN_LAB_MODE

# Check vulnerable endpoints are enabled
curl http://localhost:8000/debug/creds
curl http://localhost:8000/admin/unlock
```

## 📊 Monitoring and Logging

### Enable Detailed Logging
```bash
export LOG_LEVEL=DEBUG
export LOG_VULNERABILITIES=true
export LOG_SECURITY_EVENTS=true
```

### Monitor for Security Events
```bash
# Watch logs for vulnerability triggers
tail -f logs/vuln-lab.log | grep "VULNERABLE:"
```

## 🔄 Cleanup Procedures

### Container Cleanup
```bash
# Stop and remove container
docker stop vuln-lab-container
docker rm vuln-lab-container
docker network rm vuln-lab-network
```

### VM Cleanup
```bash
# Remove VM and associated files
VBoxManage unregistervm vuln-lab-vm --delete
```

### Local Cleanup
```bash
# Run safe restore
./SAFE_RESTORE.sh

# Clear temporary files
rm -rf /tmp/vuln-lab-*
rm -rf logs/vuln-lab.log
```

## ⚠️ Emergency Procedures

### If External Access Detected
1. **IMMEDIATELY** stop all services
2. **DISCONNECT** from network
3. **REVIEW** logs for any external connections
4. **RESTORE** from safe backup
5. **INVESTIGATE** how external access occurred

### If Real Credentials Detected
1. **STOP** all services immediately
2. **DO NOT** commit any changes
3. **REVIEW** all environment variables
4. **REPLACE** any real credentials with fake ones
5. **RESTART** in proper airgap mode

---

**Remember: The goal is learning in a safe, isolated environment!**
