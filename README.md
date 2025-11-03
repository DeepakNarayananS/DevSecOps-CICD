# DevSecOps CI/CD Security Demo

A hands-on project demonstrating DevSecOps practices with automated security testing in CI/CD pipelines. This project showcases vulnerable code with security issues and provides secure implementations for comparison.

## 🎯 Project Overview

This repository contains:
- **Root folder**: Intentionally vulnerable code with active CI/CD pipeline
- **secure/ folder**: Fixed, secure code for comparison (reference only)

The CI/CD pipeline automatically runs security tests on every commit, demonstrating how to catch vulnerabilities early in the development process.

## 🔍 What You'll Learn

### Security Testing Types

1. **SAST (Static Application Security Testing)**
   - Analyzes source code for security vulnerabilities
   - Uses Bandit to detect insecure Python patterns
   - Finds issues like hardcoded secrets, SQL injection risks

2. **SCA (Software Composition Analysis)**
   - Scans dependencies for known vulnerabilities
   - Uses Safety to check against CVE databases
   - Identifies outdated packages with security issues

3. **Code Quality**
   - Analyzes code complexity and maintainability
   - Uses Pylint for Python code quality checks
   - Ensures coding standards compliance

### Vulnerabilities Demonstrated

- **Vulnerable dependencies** (Flask 2.0.1, Jinja2 2.11.3, PyYAML 5.3.1)
- **XSS (Cross-Site Scripting)** through unescaped user input
- **Insecure deserialization** with unsafe YAML loading
- **Information disclosure** through debug mode

## 📁 Project Structure

```
DevSecOps-CICD/
├── .gitlab-ci.yml              # CI/CD pipeline configuration
├── requirements.txt            # Vulnerable dependencies
├── vulnerable_app.py           # Insecure Flask application
├── codequalitybug.py          # Code with quality issues
├── httpbug.py                 # HTTP security issues
├── unsafe.py                  # Unsafe code patterns
│
├── secure/                    # Secure implementations (reference)
│   ├── secure_app.py          # Fixed Flask application
│   ├── requirements.txt       # Updated secure dependencies
│   ├── codequalityfix.py      # Fixed code quality
│   ├── httpfix.py             # Fixed HTTP security
│   ├── safe.py                # Safe code patterns
│   └── README.md              # Secure implementation guide
│
└── Documentation/
    ├── README.md              # This file
    ├── QUICK_START.md         # 5-minute setup guide
    ├── SECURITY_COMPARISON.md # Vulnerability analysis
    ├── PIPELINE_EXPLAINED.md  # Pipeline details
    └── [other guides]
```

## 🚀 Quick Start

### Prerequisites

- GitLab account (free tier works)
- Git installed locally
- Python 3.11+ (optional, for local testing)

### Setup Instructions

1. **Fork or Clone this repository**
   ```bash
   git clone https://github.com/DeepakNarayananS/DevSecOps-CICD.git
   cd DevSecOps-CICD
   ```

2. **Push to your GitLab**
   ```bash
   git remote add gitlab https://gitlab.com/YOUR-USERNAME/devsecops-cicd.git
   git push gitlab main
   ```

3. **Watch the Pipeline Run**
   - Go to your GitLab project
   - Navigate to **CI/CD > Pipelines**
   - The pipeline runs automatically on push
   - Review security findings in each stage

### Expected Pipeline Results

The pipeline will show:
- ✅ **Test**: Pass (code compiles)
- ✅ **Code Quality**: Pass (with warnings)
- ⚠️ **SAST**: Pass (security issues detected in code)
- ⚠️ **SCA**: Pass (vulnerable dependencies detected)

This demonstrates how security issues are caught automatically!

## 📊 Pipeline Stages

### Stage 1: Test (30 seconds)
- Compiles Python code
- Checks for syntax errors
- Validates code can run

### Stage 2: Code Quality (45 seconds)
- Analyzes code complexity
- Checks coding standards
- Uses Pylint for quality metrics

### Stage 3: SAST (60 seconds)
- Static security analysis
- Scans for security anti-patterns
- Uses Bandit to find vulnerabilities

### Stage 4: SCA (20 seconds)
- Dependency vulnerability scanning
- Checks against CVE databases
- Uses Safety to identify vulnerable packages

**Expected Results:**
- **Current (Insecure)**: Multiple vulnerabilities detected ⚠️
- **After Fixes**: Clean security scan ✅

## 🔐 Vulnerabilities in This Project

### 1. Vulnerable Dependencies

**Current (Insecure):**
```
flask==2.0.1      # CVE-2023-30861 (HIGH)
jinja2==2.11.3    # CVE-2024-22195 (MEDIUM)
pyyaml==5.3.1     # CVE-2020-14343 (CRITICAL)
requests==2.25.0  # Multiple CVEs (MEDIUM)
```

**Fixed (In secure/ folder):**
```
flask==3.0.0      # Latest stable, all CVEs patched
jinja2==3.1.2     # Security fixes applied
pyyaml==6.0.1     # Safe by default
requests==2.31.0  # All security patches
```

### 2. XSS Vulnerability

**Current (Insecure):**
```python
@app.route('/search')
def search():
    query = request.args.get('q', '')
    template = f"<h1>Search Results for: {query}</h1>"
    return render_template_string(template)  # ⚠️ XSS Risk
```

**Fixed (In secure/ folder):**
```python
from flask import escape

@app.route('/search')
def search():
    query = request.args.get('q', '')
    safe_query = escape(query)  # ✅ Escaped
    template = f"<h1>Search Results for: {safe_query}</h1>"
    return render_template_string(template)
```

### 3. Insecure Deserialization

**Current (Insecure):**
```python
config = yaml.load(config_data)  # ⚠️ Can execute arbitrary code
```

**Fixed (In secure/ folder):**
```python
config = yaml.safe_load(config_data)  # ✅ Safe loading only
```

## 🧪 Local Testing

### Test Vulnerable Dependencies

```bash
# Install dependencies
pip install -r requirements.txt
pip install safety

# Run SCA scan
safety check

# Expected: Multiple vulnerabilities detected
```

### Test Secure Dependencies

```bash
# Navigate to secure folder
cd secure/

# Install dependencies
pip install -r requirements.txt
pip install safety

# Run SCA scan
safety check

# Expected: No vulnerabilities found
```

### Run the Applications

**Insecure Version:**
```bash
python vulnerable_app.py
# Visit: http://localhost:5000
# Test XSS: http://localhost:5000/search?q=<script>alert('XSS')</script>
```

**Secure Version:**
```bash
cd secure/
python secure_app.py
# Visit: http://localhost:5000
# Test XSS protection: Script will be escaped and displayed as text
```

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
- **[SECURITY_COMPARISON.md](SECURITY_COMPARISON.md)** - Detailed vulnerability analysis
- **[PIPELINE_EXPLAINED.md](PIPELINE_EXPLAINED.md)** - How the pipeline works
- **[SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)** - Step-by-step setup guide
- **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - Visual diagrams and examples

## 🎓 Learning Path

### Beginner (Week 1)
1. Set up the project in GitLab
2. Run the pipeline and observe results
3. Read through the vulnerable code
4. Compare with secure implementations

### Intermediate (Week 2)
1. Understand each vulnerability
2. Study the fixes in secure/ folder
3. Try fixing vulnerabilities yourself
4. Experiment with the pipeline

### Advanced (Week 3)
1. Add more security tests
2. Integrate additional tools
3. Create custom security rules
4. Apply to your own projects

## 🔧 How to Fix the Vulnerabilities

### Step 1: Update Dependencies
```bash
# Edit requirements.txt
flask==3.0.0
jinja2==3.1.2
pyyaml==6.0.1
requests==2.31.0
```

### Step 2: Fix Code Issues
- Escape user input to prevent XSS
- Use `yaml.safe_load()` instead of `yaml.load()`
- Disable debug mode in production
- Add input validation

### Step 3: Re-run Pipeline
```bash
git add requirements.txt vulnerable_app.py
git commit -m "Fix: Update dependencies and secure code"
git push
```

### Step 4: Verify
- Pipeline should show clean results ✅
- No vulnerabilities detected
- All security tests pass

## 🛡️ Security Best Practices

### Dependency Management
- ✅ Keep dependencies up-to-date
- ✅ Use dependency lock files
- ✅ Regularly scan for vulnerabilities
- ✅ Remove unused dependencies

### Secure Coding
- ✅ Validate and sanitize all user input
- ✅ Use parameterized queries
- ✅ Escape output to prevent XSS
- ✅ Use safe deserialization methods

### CI/CD Security
- ✅ Run security tests on every commit
- ✅ Fail builds on critical vulnerabilities
- ✅ Store security reports as artifacts
- ✅ Use multiple security testing layers

## 📊 Comparison: Before vs After

| Aspect | Current (Insecure) | After Fixes (Secure) |
|--------|-------------------|---------------------|
| Flask Version | 2.0.1 (vulnerable) | 3.0.0 (patched) |
| Input Handling | Raw user input | Escaped/validated |
| YAML Loading | yaml.load() | yaml.safe_load() |
| Debug Mode | Enabled | Disabled |
| SCA Results | Multiple CVEs | Clean |
| SAST Results | Security issues | No issues |
| Pipeline Status | ⚠️ Warnings | ✅ Pass |

## 🆘 Troubleshooting

### Pipeline Doesn't Start
- Check that `.gitlab-ci.yml` is in repository root
- Verify GitLab runners are enabled
- Ensure you're on GitLab (not just GitHub)

### SCA Stage Shows Warnings
- **This is expected!** The insecure version has vulnerable dependencies
- This demonstrates why dependency scanning is important
- Check secure/ folder for fixed versions

### Local Testing Fails
- Verify Python 3.11+ is installed
- Use virtual environment
- Check all dependencies are installed

## 🤝 Contributing

This is an educational project. Feel free to:
- Report issues
- Suggest improvements
- Add more vulnerability examples
- Improve documentation

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

## ⚠️ Disclaimer

This project contains intentionally vulnerable code for educational purposes. 
**DO NOT deploy this code to production or expose it to the internet.**

## 🔗 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Safety Documentation](https://pyup.io/safety/)
- [Bandit Documentation](https://bandit.readthedocs.io/)

## 📧 Support

- **GitHub**: https://github.com/DeepakNarayananS/DevSecOps-CICD
- **GitLab**: https://gitlab.com/dnsoc-group/devsecops-cicd

---

**Learn DevSecOps by doing! 🚀 Stay Secure! 🔐**
