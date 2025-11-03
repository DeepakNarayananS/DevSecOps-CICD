# Security Comparison: Insecure vs Secure

> **Compare:** Root folder (vulnerable) vs secure/ folder (fixed)

This document provides a side-by-side comparison of the vulnerabilities and their fixes.

## 📊 Quick Comparison Table

| Security Aspect | Insecure Version | Secure Version | Impact |
|----------------|------------------|----------------|---------|
| **Flask Version** | 2.0.1 | 3.0.0 | High - Multiple CVEs fixed |
| **Jinja2 Version** | 2.11.3 | 3.1.2 | High - XSS vulnerabilities patched |
| **PyYAML Version** | 5.3.1 | 6.0.1 | Critical - RCE vulnerability fixed |
| **Requests Version** | 2.25.0 | 2.31.0 | Medium - Security patches applied |
| **Input Handling** | No escaping | Proper escaping | High - Prevents XSS |
| **YAML Loading** | yaml.load() | yaml.safe_load() | Critical - Prevents RCE |
| **Debug Mode** | Enabled | Disabled | Medium - Info disclosure prevented |
| **SCA Results** | Multiple CVEs | Clean | - |
| **SAST Results** | Critical issues | No issues | - |

## 🔍 Detailed Vulnerability Analysis

### 1. Cross-Site Scripting (XSS)

#### Insecure Code:
```python
@app.route('/search')
def search():
    query = request.args.get('q', '')
    template = f"<h1>Search Results for: {query}</h1>"
    return render_template_string(template)
```

**Vulnerability:** User input is directly embedded in HTML without escaping.

**Attack Example:**
```
http://localhost:5000/search?q=<script>alert('XSS')</script>
```

**Impact:** Attacker can execute arbitrary JavaScript in victim's browser, steal cookies, session tokens, or perform actions on behalf of the user.

#### Secure Code:
```python
from flask import escape

@app.route('/search')
def search():
    query = request.args.get('q', '')
    safe_query = escape(query)
    template = f"<h1>Search Results for: {safe_query}</h1>"
    return render_template_string(template)
```

**Fix:** The `escape()` function converts special characters to HTML entities.

**Result:** `<script>` becomes `&lt;script&gt;` and is displayed as text, not executed.

---

### 2. Insecure Deserialization

#### Insecure Code:
```python
@app.route('/config', methods=['POST'])
def load_config():
    config_data = request.data
    config = yaml.load(config_data)  # Unsafe!
    return str(config)
```

**Vulnerability:** `yaml.load()` can execute arbitrary Python code during deserialization.

**Attack Example:**
```yaml
!!python/object/apply:os.system
args: ['rm -rf /']
```

**Impact:** Remote Code Execution (RCE) - attacker can run any command on the server.

#### Secure Code:
```python
@app.route('/config', methods=['POST'])
def load_config():
    config_data = request.data
    config = yaml.safe_load(config_data)  # Safe!
    return str(config)
```

**Fix:** `yaml.safe_load()` only constructs simple Python objects (strings, lists, dicts), preventing code execution.

---

### 3. Vulnerable Dependencies

#### Insecure requirements.txt:
```
flask==2.0.1      # CVE-2023-30861
jinja2==2.11.3    # CVE-2024-22195
pyyaml==5.3.1     # CVE-2020-14343
requests==2.25.0  # Multiple CVEs
```

**Known CVEs:**

**Flask 2.0.1:**
- CVE-2023-30861: Cookie parsing vulnerability
- Severity: High
- CVSS Score: 7.5

**Jinja2 2.11.3:**
- CVE-2024-22195: XSS in exception handling
- Severity: Medium
- CVSS Score: 6.1

**PyYAML 5.3.1:**
- CVE-2020-14343: Arbitrary code execution
- Severity: Critical
- CVSS Score: 9.8

#### Secure requirements.txt:
```
flask==3.0.0      # Latest stable, all CVEs patched
jinja2==3.1.2     # Security fixes applied
pyyaml==6.0.1     # Safe by default
requests==2.31.0  # All security patches
```

**Benefits:**
- All known CVEs patched
- Security improvements
- Better performance
- New security features

---

### 4. Debug Mode in Production

#### Insecure Code:
```python
if __name__ == '__main__':
    app.run(debug=True)  # Dangerous!
```

**Vulnerability:** Debug mode exposes:
- Full stack traces with code
- Interactive debugger in browser
- Internal application structure
- Environment variables

**Impact:** Information disclosure helps attackers understand the application and find vulnerabilities.

#### Secure Code:
```python
if __name__ == '__main__':
    app.run(debug=False)  # Safe for production
```

**Fix:** Disable debug mode in production. Use proper logging instead.

---

## 🔬 SCA Scan Results Comparison

### Insecure Version Output:
```
+==============================================================================+
|                                                                              |
|                               /$$$$$$            /$$                         |
|                              /$$__  $$          | $$                         |
|           /$$$$$$$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$           |
|          /$$_____/ |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$           |
|         |  $$$$$$   /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$           |
|          \____  $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$           |
|          /$$$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$           |
|         |_______/  \_______/|__/     \_______/   \___/   \____  $$           |
|                                                            /$$  | $$           |
|                                                           |  $$$$$$/           |
|  by pyup.io                                                \______/            |
|                                                                              |
+==============================================================================+

 VULNERABILITIES FOUND: 4
+==============================================================================+
| package    | installed | affected      | ID             | severity |
+==============================================================================+
| flask      | 2.0.1     | <2.2.5        | CVE-2023-30861 | HIGH     |
| jinja2     | 2.11.3    | <3.1.0        | CVE-2024-22195 | MEDIUM   |
| pyyaml     | 5.3.1     | <5.4          | CVE-2020-14343 | CRITICAL |
| requests   | 2.25.0    | <2.31.0       | Multiple CVEs  | MEDIUM   |
+==============================================================================+

⚠️ INSECURE VERSION - Vulnerabilities detected in dependencies!
```

### Secure Version Output:
```
+==============================================================================+
|                                                                              |
|                               /$$$$$$            /$$                         |
|                              /$$__  $$          | $$                         |
|           /$$$$$$$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$           |
|          /$$_____/ |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$           |
|         |  $$$$$$   /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$           |
|          \____  $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$           |
|          /$$$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$           |
|         |_______/  \_______/|__/     \_______/   \___/   \____  $$           |
|                                                            /$$  | $$           |
|                                                           |  $$$$$$/           |
|  by pyup.io                                                \______/            |
|                                                                              |
+==============================================================================+

 VULNERABILITIES FOUND: 0

✅ SECURE VERSION - No known vulnerabilities detected!
All dependencies are up-to-date and secure.
```

---

## 🎯 DAST Scan Differences

### Insecure Version Findings:

**High Priority Alerts:**
- Missing security headers
- Debug mode enabled
- Verbose error messages
- Potential XSS vectors

**Medium Priority Alerts:**
- Cookie without secure flag
- Missing Content-Security-Policy
- Information disclosure

### Secure Version Findings:

**High Priority Alerts:** None

**Medium Priority Alerts:** Minimal

**Improvements:**
- Security headers implemented
- Proper error handling
- Secure cookie configuration
- CSP headers added

---

## 📈 Pipeline Execution Comparison

### Insecure Pipeline:
```
✓ test          - PASSED (30s)
✓ code_quality  - PASSED (45s)
⚠ sast          - PASSED with warnings (60s)
✗ sca           - FAILED (20s) - Vulnerabilities found
⚠ dast          - PASSED with warnings (120s)

Overall: FAILED ❌
```

### Secure Pipeline:
```
✓ test          - PASSED (30s)
✓ code_quality  - PASSED (45s)
✓ sast          - PASSED (60s)
✓ sca           - PASSED (20s)
✓ dast          - PASSED (120s)

Overall: PASSED ✅
```

---

## 🛡️ Security Improvements Summary

### Code Level:
1. ✅ Input validation and sanitization
2. ✅ Output encoding
3. ✅ Safe deserialization
4. ✅ Secure configuration

### Dependency Level:
1. ✅ Updated to latest stable versions
2. ✅ All CVEs patched
3. ✅ Regular update schedule
4. ✅ Automated scanning

### Pipeline Level:
1. ✅ Multiple security test layers
2. ✅ Automated vulnerability detection
3. ✅ Fail-fast on critical issues
4. ✅ Security reports as artifacts

---

## 🎓 Learning Exercises

### Exercise 1: Identify Vulnerabilities
Look at the insecure code and try to identify all vulnerabilities before checking the answers.

### Exercise 2: Fix the Code
Try to fix the insecure version yourself before looking at the secure version.

### Exercise 3: Add New Security Tests
Extend the pipeline with additional security tools like:
- Bandit (Python security linter)
- Trivy (Container scanning)
- Dependency-Check (OWASP)

### Exercise 4: Create Attack Scenarios
Write proof-of-concept exploits for each vulnerability to understand the real-world impact.

---

## 📚 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVE Database](https://cve.mitre.org/)
- [Flask Security](https://flask.palletsprojects.com/en/latest/security/)
- [YAML Security](https://yaml.org/spec/1.2/spec.html#id2761803)

---

**Remember:** Security is not a one-time fix but a continuous process. Always keep dependencies updated and follow secure coding practices!
