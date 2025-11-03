# DevSecOps CI/CD Security Demo

A beginner-friendly project demonstrating the difference between insecure and secure CI/CD pipelines with practical examples of SAST, SCA, and DAST security testing.

## 🎯 Project Overview

This project contains two parallel implementations:
- **insecure-cicd/**: Intentionally vulnerable code with security issues
- **secure-cicd/**: Fixed, secure version following best practices

Both folders include complete CI/CD pipelines with automated security testing to help you understand how to identify and fix common vulnerabilities.

## 🔍 What You'll Learn

### Security Testing Types

1. **SAST (Static Application Security Testing)**
   - Analyzes source code without running it
   - Finds vulnerabilities like SQL injection, XSS, hardcoded secrets
   - Runs fast and early in the pipeline

2. **SCA (Software Composition Analysis)**
   - Scans third-party dependencies for known vulnerabilities
   - Checks against CVE databases
   - Identifies outdated packages with security issues

3. **DAST (Dynamic Application Security Testing)**
   - Tests running applications
   - Simulates real-world attacks
   - Finds runtime vulnerabilities

### Common Vulnerabilities Demonstrated

- **CVE-affected dependencies** (outdated Flask, Jinja2, PyYAML)
- **XSS (Cross-Site Scripting)** through unescaped user input
- **Insecure deserialization** with unsafe YAML loading
- **Information disclosure** through debug mode

## 📁 Project Structure

```
DevSecOps-CICD/
├── insecure-cicd/              # Vulnerable implementation
│   ├── .gitlab-ci.yml          # CI/CD pipeline with security tests
│   ├── requirements.txt        # Vulnerable dependencies
│   ├── vulnerable_app.py       # Insecure Flask application
│   └── README.md               # Detailed setup guide
│
├── secure-cicd/                # Secure implementation
│   ├── .gitlab-ci.yml          # CI/CD pipeline with security tests
│   ├── requirements.txt        # Updated, secure dependencies
│   ├── secure_app.py           # Secure Flask application
│   └── README.md               # Detailed setup guide
│
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- GitLab account (free tier is sufficient)
- Git installed locally
- Python 3.11+ (optional, for local testing)
- Basic understanding of Git and CI/CD concepts

### Option 1: GitLab Setup (Recommended)

#### For Insecure Version:
```bash
# Clone and navigate
git clone <your-repo-url>
cd DevSecOps-CICD/insecure-cicd

# Create new GitLab project and push
git init
git add .
git commit -m "Initial commit - insecure version"
git remote add origin https://gitlab.com/<username>/insecure-cicd.git
git push -u origin main
```

#### For Secure Version:
```bash
# Navigate to secure folder
cd ../secure-cicd

# Create new GitLab project and push
git init
git add .
git commit -m "Initial commit - secure version"
git remote add origin https://gitlab.com/<username>/secure-cicd.git
git push -u origin main
```

### Option 2: Local Testing

#### Test Insecure Version:
```bash
cd insecure-cicd
pip install -r requirements.txt
pip install safety

# Run SCA scan
safety check

# Expected: Multiple vulnerabilities detected ⚠️
```

#### Test Secure Version:
```bash
cd secure-cicd
pip install -r requirements.txt
pip install safety

# Run SCA scan
safety check

# Expected: No vulnerabilities found ✅
```

## 📊 Understanding Pipeline Results

### Insecure Pipeline Results

When you run the insecure pipeline, you'll see:

**SCA Stage:**
```
⚠️ INSECURE VERSION - Vulnerabilities detected!
╒══════════════════════════════════════════════════════════════════════════════╕
│ REPORT                                                                       │
├──────────────────────────┬───────────────┬──────────────────┬───────────────┤
│ package                  │ installed     │ affected         │ ID            │
├──────────────────────────┼───────────────┼──────────────────┼───────────────┤
│ flask                    │ 2.0.1         │ <2.2.5           │ CVE-2023-30861│
│ jinja2                   │ 2.11.3        │ <3.1.0           │ CVE-2024-22195│
│ pyyaml                   │ 5.3.1         │ <5.4             │ CVE-2020-14343│
╘══════════════════════════╧═══════════════╧══════════════════╧═══════════════╛
```

**SAST Stage:**
- Detects XSS vulnerabilities
- Flags unsafe YAML deserialization
- Warns about debug mode enabled

**DAST Stage:**
- Identifies potential attack vectors
- Reports security misconfigurations

### Secure Pipeline Results

When you run the secure pipeline, you'll see:

**SCA Stage:**
```
✅ SECURE VERSION - No known vulnerabilities detected!
All dependencies are up-to-date and secure.
```

**SAST Stage:**
- No critical vulnerabilities
- Clean code quality report

**DAST Stage:**
- Minimal or no security alerts
- Proper security headers detected

## 🔧 How to Use This Project

### For Learning:

1. **Start with Insecure Version**
   - Deploy to GitLab
   - Run the pipeline
   - Review the security findings
   - Understand what each vulnerability means

2. **Compare with Secure Version**
   - Deploy the secure version
   - Run the pipeline
   - Compare the results
   - Study the code differences

3. **Experiment**
   - Try introducing new vulnerabilities
   - Test different security tools
   - Modify the pipeline configuration

### For Teaching:

1. **Classroom Demo**
   - Show both pipelines side-by-side
   - Explain each security test
   - Discuss real-world implications

2. **Hands-on Exercise**
   - Have students fix vulnerabilities
   - Guide them through the secure version
   - Review their implementations

3. **Assessment**
   - Ask students to identify vulnerabilities
   - Have them write secure code
   - Test their understanding of security tools

## 🛠️ Pipeline Configuration Details

### Common Pipeline Stages

Both pipelines include these stages:

```yaml
stages:
  - test          # Basic code compilation and syntax checks
  - code_quality  # Code quality and complexity analysis
  - sast          # Static application security testing
  - sca           # Software composition analysis
  - dast          # Dynamic application security testing
```

### SCA Configuration

```yaml
sca-scan:
  stage: sca
  image: python:3.11
  script:
    - pip install safety
    - pip install -r requirements.txt
    - safety check --json
```

**What it does:**
- Installs the Safety tool
- Scans all dependencies in requirements.txt
- Checks against the Safety vulnerability database
- Reports any known CVEs

### DAST Configuration

```yaml
dast-scan:
  stage: dast
  image: owasp/zap2docker-stable
  script:
    - /zap/zap-baseline.py -t https://www.example.com
```

**What it does:**
- Uses OWASP ZAP (Zed Attack Proxy)
- Performs baseline security scan
- Tests for common web vulnerabilities
- Generates detailed HTML report

## 📚 Key Concepts Explained

### Why SCA Matters

**Problem:** 80% of modern applications are composed of third-party libraries. If these libraries have vulnerabilities, your application is vulnerable too.

**Solution:** SCA tools automatically scan your dependencies and alert you to known vulnerabilities, allowing you to update before attackers exploit them.

### Why SAST Matters

**Problem:** Developers can accidentally introduce security vulnerabilities through coding mistakes.

**Solution:** SAST analyzes your source code to find security issues early, before the code is deployed.

### Why DAST Matters

**Problem:** Some vulnerabilities only appear when the application is running.

**Solution:** DAST tests your running application like an attacker would, finding issues that static analysis might miss.

## 🔐 Security Best Practices

### Dependency Management
- ✅ Keep dependencies up-to-date
- ✅ Use dependency lock files
- ✅ Regularly scan for vulnerabilities
- ✅ Remove unused dependencies

### Secure Coding
- ✅ Validate and sanitize all user input
- ✅ Use parameterized queries (prevent SQL injection)
- ✅ Escape output (prevent XSS)
- ✅ Use safe deserialization methods

### CI/CD Security
- ✅ Run security tests on every commit
- ✅ Fail builds on critical vulnerabilities
- ✅ Store security reports as artifacts
- ✅ Use multiple security testing layers

### Configuration
- ✅ Never commit secrets to Git
- ✅ Use environment variables
- ✅ Disable debug mode in production
- ✅ Implement proper error handling

## 🎓 Learning Path

### Beginner (Week 1)
1. Set up both projects in GitLab
2. Run the pipelines and observe results
3. Read through the code in both versions
4. Understand the basic vulnerabilities

### Intermediate (Week 2)
1. Modify the insecure code to add new vulnerabilities
2. Practice fixing vulnerabilities
3. Experiment with different security tools
4. Customize the pipeline configuration

### Advanced (Week 3)
1. Integrate additional security tools
2. Create custom security rules
3. Implement security gates
4. Build a complete DevSecOps workflow

## 🆘 Troubleshooting

### Pipeline Fails Immediately
- **Check**: GitLab runners are enabled
- **Solution**: Go to Settings > CI/CD > Runners

### SCA Scan Doesn't Find Vulnerabilities
- **Check**: requirements.txt is present
- **Solution**: Ensure the file is committed to Git

### DAST Scan Times Out
- **Check**: Network connectivity
- **Solution**: Adjust timeout in .gitlab-ci.yml

### Local Testing Issues
- **Check**: Python version (3.11+ required)
- **Solution**: Use virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📖 Additional Resources

### Documentation
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Safety Documentation](https://pyup.io/safety/)
- [OWASP ZAP User Guide](https://www.zaproxy.org/docs/)

### Learning Materials
- [DevSecOps Fundamentals](https://www.devsecops.org/)
- [Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [GitLab Security Training](https://about.gitlab.com/learn/)

### Tools
- [Safety](https://pyup.io/safety/) - Python dependency scanner
- [OWASP ZAP](https://www.zaproxy.org/) - Web application security scanner
- [GitLab Security Scanners](https://docs.gitlab.com/ee/user/application_security/)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test both insecure and secure versions
5. Submit a pull request

## 📝 License

This project is licensed for educational use. Feel free to use it for learning, teaching, and training purposes.

## ⚠️ Disclaimer

The insecure-cicd folder contains intentionally vulnerable code for educational purposes only. Never deploy this code to production or expose it to the internet.

## 💡 Next Steps

1. **Deploy both versions** to GitLab
2. **Run the pipelines** and compare results
3. **Study the code differences** between insecure and secure
4. **Experiment** with your own modifications
5. **Share** your learnings with others

## 📧 Support

If you have questions or need help:
- Check the individual README files in each folder
- Review the troubleshooting section
- Open an issue in the repository
- Consult the additional resources

---

**Happy Learning! 🚀 Stay Secure! 🔐**
