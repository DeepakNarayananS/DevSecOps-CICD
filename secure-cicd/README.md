# Secure CI/CD Pipeline Demo

✅ **SECURE**: This project demonstrates security best practices in a CI/CD pipeline.

## Overview

This project shows how to properly secure a CI/CD pipeline with:
- **Updated, secure dependencies** (verified by SCA)
- **Secure code patterns** (validated by SAST)
- **Runtime security** (tested by DAST)

## What's Inside

### Secure Components

1. **Secure Dependencies** (`requirements.txt`)
   - Flask 3.0.0 - Latest stable with security patches
   - Jinja2 3.1.2 - All XSS vulnerabilities patched
   - PyYAML 6.0.1 - Safe loading enforced
   - Requests 2.31.0 - Latest with all security fixes

2. **Secure Code** (`secure_app.py`)
   - Proper input escaping to prevent XSS
   - Safe YAML deserialization
   - Debug mode disabled for production
   - Security headers implemented

## Security Tests in Pipeline

### 1. SAST (Static Application Security Testing)
- Scans source code for security vulnerabilities
- Validates secure coding practices
- **Expected Result**: No critical issues ✅

### 2. SCA (Software Composition Analysis)
- Scans dependencies for known vulnerabilities
- Uses Safety tool to check against CVE database
- **Expected Result**: No vulnerabilities detected ✅

### 3. DAST (Dynamic Application Security Testing)
- Scans running applications for vulnerabilities
- Uses OWASP ZAP with security configurations
- **Expected Result**: Minimal or no alerts ✅

## Setup Instructions

### Prerequisites
- GitLab account (free tier works)
- Git installed on your machine
- Python 3.11+ (for local testing)

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd secure-cicd
```

### Step 2: Push to GitLab
```bash
git remote add origin https://gitlab.com/<your-username>/secure-cicd.git
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
5. **Expected**: Clean scan with no vulnerabilities

Example output:
```
✅ SECURE VERSION - No known vulnerabilities detected!
All dependencies are up-to-date and secure.
```

### DAST Results
1. In the same pipeline, find the `dast-scan` job
2. Download the `dast-report.html` artifact
3. Open in a browser to see the clean report
4. **Expected**: No critical alerts

### SAST Results
1. Go to **Security & Compliance > Vulnerability Report**
2. View the security status
3. **Expected**: No vulnerabilities or only informational items

## Local Testing

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run SCA Scan Locally
```bash
pip install safety
safety check
```
Expected output: "No known security vulnerabilities found"

### Run the Secure App
```bash
python secure_app.py
```
Visit: http://localhost:5000

**Test XSS Protection**: http://localhost:5000/search?q=<script>alert('XSS')</script>
- The script tags will be escaped and displayed as text, not executed

## Security Best Practices Demonstrated

### 1. Dependency Management
- ✅ Use latest stable versions
- ✅ Regular dependency updates
- ✅ Automated vulnerability scanning
- ✅ Lock file for reproducible builds

### 2. Secure Coding
- ✅ Input validation and sanitization
- ✅ Output encoding (escape user input)
- ✅ Safe deserialization (yaml.safe_load)
- ✅ Disable debug mode in production

### 3. CI/CD Security
- ✅ Automated security scans on every commit
- ✅ Multiple security testing layers (SAST, SCA, DAST)
- ✅ Pipeline fails on critical vulnerabilities
- ✅ Security reports as artifacts

### 4. Configuration Security
- ✅ No hardcoded secrets
- ✅ Environment-based configuration
- ✅ Secure defaults
- ✅ Principle of least privilege

## Comparison with Insecure Version

| Aspect | Insecure | Secure |
|--------|----------|--------|
| Flask Version | 2.0.1 (vulnerable) | 3.0.0 (patched) |
| Input Handling | Raw user input | Escaped/validated |
| YAML Loading | yaml.load() | yaml.safe_load() |
| Debug Mode | Enabled | Disabled |
| SCA Results | Multiple CVEs | Clean |
| SAST Results | Critical issues | No issues |

## Pipeline Stages Explained

### Stage 1: Test
- Compiles Python code
- Runs basic syntax checks
- Fast feedback on code quality

### Stage 2: Code Quality
- Analyzes code complexity
- Checks for code smells
- Ensures maintainability

### Stage 3: SAST
- Static analysis of source code
- Detects security anti-patterns
- Finds potential vulnerabilities

### Stage 4: SCA
- Scans all dependencies
- Checks against CVE databases
- Validates license compliance

### Stage 5: DAST
- Dynamic testing of running app
- Simulates real attacks
- Tests runtime behavior

## Continuous Improvement

### Regular Maintenance
1. **Weekly**: Check for dependency updates
2. **Monthly**: Review security advisories
3. **Quarterly**: Update security tools
4. **Annually**: Security architecture review

### Monitoring
- Set up alerts for new CVEs
- Monitor pipeline success rates
- Track security metrics
- Review security reports

## Resources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [GitLab Security Best Practices](https://docs.gitlab.com/ee/user/application_security/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Flask Security Considerations](https://flask.palletsprojects.com/en/latest/security/)

## Contributing

When contributing, ensure:
1. All dependencies are up-to-date
2. Code passes all security scans
3. No new vulnerabilities introduced
4. Security tests are updated

## License

MIT License - Use freely for educational and production purposes.

## Support

For questions or issues:
- Open an issue in the repository
- Review the comparison with `insecure-cicd` folder
- Check GitLab CI/CD documentation
