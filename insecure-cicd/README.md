# Insecure CI/CD Pipeline Demo

⚠️ **WARNING**: This project contains intentionally vulnerable code for educational purposes. DO NOT use in production!

## Overview

This project demonstrates common security vulnerabilities in a CI/CD pipeline, including:
- **Vulnerable dependencies** (detected by SCA)
- **Insecure code patterns** (detected by SAST)
- **Runtime vulnerabilities** (detected by DAST)

## What's Inside

### Vulnerable Components

1. **Vulnerable Dependencies** (`requirements.txt`)
   - Flask 2.0.1 - Contains known CVEs
   - Jinja2 2.11.3 - XSS vulnerabilities
   - PyYAML 5.3.1 - Arbitrary code execution risk
   - Requests 2.25.0 - Outdated with security issues

2. **Insecure Code** (`vulnerable_app.py`)
   - XSS vulnerability through unescaped user input
   - Unsafe YAML deserialization
   - Debug mode enabled in production

## Security Tests in Pipeline

### 1. SAST (Static Application Security Testing)
- Scans source code for security vulnerabilities
- Detects hardcoded secrets, SQL injection, XSS patterns
- Runs automatically on every commit

### 2. SCA (Software Composition Analysis)
- Scans dependencies for known vulnerabilities
- Uses Safety tool to check against CVE database
- **Expected Result**: Multiple vulnerabilities detected ⚠️

### 3. DAST (Dynamic Application Security Testing)
- Scans running applications for vulnerabilities
- Uses OWASP ZAP to test for common web vulnerabilities
- Tests against example.com for demonstration

## Setup Instructions

### Prerequisites
- GitLab account (free tier works)
- Git installed on your machine
- Python 3.11+ (for local testing)

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd insecure-cicd
```

### Step 2: Push to GitLab
```bash
git remote add origin https://gitlab.com/<your-username>/insecure-cicd.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitLab CI/CD
1. Go to your GitLab project
2. Navigate to **Settings > CI/CD**
3. Ensure runners are enabled (shared runners work fine)

### Step 4: Trigger the Pipeline
The pipeline runs automatically on push. You can also:
1. Go to **CI/CD > Pipelines**
2. Click **Run Pipeline**
3. Select the `main` branch
4. Click **Run Pipeline**

## Understanding the Results

### SCA Results
1. Go to **CI/CD > Pipelines**
2. Click on the latest pipeline
3. Find the `sca-scan` job
4. Click to view the output
5. **Expected**: Multiple CVEs detected in dependencies

Example output:
```
⚠️ INSECURE VERSION - Vulnerabilities detected!
- Flask 2.0.1: CVE-2023-30861 (High severity)
- Jinja2 2.11.3: CVE-2024-22195 (Medium severity)
- PyYAML 5.3.1: CVE-2020-14343 (Critical severity)
```

### DAST Results
1. In the same pipeline, find the `dast-scan` job
2. Download the `dast-report.html` artifact
3. Open in a browser to see detailed findings
4. **Expected**: Various alerts and warnings

### SAST Results
1. Go to **Security & Compliance > Vulnerability Report**
2. View detected code vulnerabilities
3. **Expected**: XSS, insecure deserialization warnings

## Local Testing (Optional)

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run SCA Scan Locally
```bash
pip install safety
safety check
```

### Run the Vulnerable App (Educational Only)
```bash
python vulnerable_app.py
```
Visit: http://localhost:5000

**Test XSS**: http://localhost:5000/search?q=<script>alert('XSS')</script>

## Key Takeaways

1. **SCA is Essential**: Outdated dependencies are a major attack vector
2. **Multiple Layers**: Use SAST, SCA, and DAST together
3. **Automation**: Security checks should run on every commit
4. **Fail Fast**: Catch vulnerabilities before production

## Next Steps

Compare this with the `secure-cicd` folder to see:
- How to fix vulnerable dependencies
- Secure coding practices
- Clean pipeline results

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitLab Security Scanning](https://docs.gitlab.com/ee/user/application_security/)
- [Safety Documentation](https://pyup.io/safety/)
- [OWASP ZAP](https://www.zaproxy.org/)

## License

Educational use only. Not for production deployment.
