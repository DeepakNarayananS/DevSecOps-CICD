# Setup Checklist

Use this checklist to ensure you've completed all setup steps correctly.

## 📋 Pre-Deployment Checklist

### Prerequisites
- [ ] GitLab account created (free tier is fine)
- [ ] Git installed on your machine
- [ ] Python 3.11+ installed (optional, for local testing)
- [ ] Basic understanding of Git commands

## 🚀 Insecure Version Setup

### Step 1: Repository Setup
- [ ] Navigate to `DevSecOps-CICD/insecure-cicd/` folder
- [ ] Initialize Git repository (`git init`)
- [ ] Create new GitLab project named "insecure-cicd"
- [ ] Add remote origin
- [ ] Commit all files
- [ ] Push to GitLab

### Step 2: Verify Files
- [ ] `.gitlab-ci.yml` is present
- [ ] `requirements.txt` is present
- [ ] `vulnerable_app.py` is present
- [ ] `README.md` is present

### Step 3: Pipeline Configuration
- [ ] Go to GitLab project settings
- [ ] Navigate to Settings > CI/CD
- [ ] Verify runners are enabled
- [ ] Check that Auto DevOps is disabled (we're using custom pipeline)

### Step 4: Run Pipeline
- [ ] Go to CI/CD > Pipelines
- [ ] Click "Run Pipeline"
- [ ] Select `main` branch
- [ ] Click "Run Pipeline" button
- [ ] Wait for pipeline to complete (~5 minutes)

### Step 5: Verify Results
- [ ] Test stage: PASSED ✅
- [ ] Code Quality stage: PASSED ✅
- [ ] SAST stage: PASSED with warnings ⚠️
- [ ] SCA stage: FAILED ❌ (Expected - vulnerabilities found)
- [ ] DAST stage: PASSED with warnings ⚠️

### Step 6: Review Security Findings
- [ ] Click on `sca-scan` job
- [ ] Verify 4 vulnerabilities detected:
  - [ ] Flask 2.0.1 vulnerability
  - [ ] Jinja2 2.11.3 vulnerability
  - [ ] PyYAML 5.3.1 vulnerability
  - [ ] Requests 2.25.0 vulnerability
- [ ] Download DAST report artifact
- [ ] Open `dast-report.html` in browser

## ✅ Secure Version Setup

### Step 1: Repository Setup
- [ ] Navigate to `DevSecOps-CICD/secure-cicd/` folder
- [ ] Initialize Git repository (`git init`)
- [ ] Create new GitLab project named "secure-cicd"
- [ ] Add remote origin
- [ ] Commit all files
- [ ] Push to GitLab

### Step 2: Verify Files
- [ ] `.gitlab-ci.yml` is present
- [ ] `requirements.txt` is present
- [ ] `secure_app.py` is present
- [ ] `README.md` is present

### Step 3: Pipeline Configuration
- [ ] Go to GitLab project settings
- [ ] Navigate to Settings > CI/CD
- [ ] Verify runners are enabled
- [ ] Check that Auto DevOps is disabled

### Step 4: Run Pipeline
- [ ] Go to CI/CD > Pipelines
- [ ] Click "Run Pipeline"
- [ ] Select `main` branch
- [ ] Click "Run Pipeline" button
- [ ] Wait for pipeline to complete (~5 minutes)

### Step 5: Verify Results
- [ ] Test stage: PASSED ✅
- [ ] Code Quality stage: PASSED ✅
- [ ] SAST stage: PASSED ✅
- [ ] SCA stage: PASSED ✅ (No vulnerabilities)
- [ ] DAST stage: PASSED ✅

### Step 6: Review Security Findings
- [ ] Click on `sca-scan` job
- [ ] Verify "No vulnerabilities found" message
- [ ] Download DAST report artifact
- [ ] Compare with insecure version report

## 🧪 Local Testing (Optional)

### Insecure Version
- [ ] Navigate to `insecure-cicd/` folder
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Install Safety: `pip install safety`
- [ ] Run SCA scan: `safety check`
- [ ] Verify vulnerabilities are detected
- [ ] (Optional) Run app: `python vulnerable_app.py`
- [ ] (Optional) Test XSS: Visit `http://localhost:5000/search?q=<script>alert('XSS')</script>`

### Secure Version
- [ ] Navigate to `secure-cicd/` folder
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Install Safety: `pip install safety`
- [ ] Run SCA scan: `safety check`
- [ ] Verify no vulnerabilities found
- [ ] (Optional) Run app: `python secure_app.py`
- [ ] (Optional) Test XSS protection: Visit `http://localhost:5000/search?q=<script>alert('XSS')</script>`
- [ ] Verify script is escaped (displayed as text, not executed)

## 📚 Learning Checklist

### Understanding
- [ ] Read main README.md
- [ ] Read QUICK_START.md
- [ ] Read SECURITY_COMPARISON.md
- [ ] Read PIPELINE_EXPLAINED.md
- [ ] Understand what SCA does
- [ ] Understand what SAST does
- [ ] Understand what DAST does

### Comparison
- [ ] Compare both `.gitlab-ci.yml` files
- [ ] Compare `vulnerable_app.py` vs `secure_app.py`
- [ ] Compare `requirements.txt` files
- [ ] Compare pipeline results
- [ ] Compare security scan outputs

### Hands-On Practice
- [ ] Identify all vulnerabilities in insecure version
- [ ] Understand how each vulnerability works
- [ ] Understand how each fix works
- [ ] Try modifying code and re-running pipeline
- [ ] Experiment with different dependency versions

## 🎯 Verification Checklist

### Insecure Pipeline Should Show:
- [ ] ⚠️ XSS vulnerability in SAST
- [ ] ⚠️ Unsafe deserialization in SAST
- [ ] ❌ Flask 2.0.1 CVE in SCA
- [ ] ❌ Jinja2 2.11.3 CVE in SCA
- [ ] ❌ PyYAML 5.3.1 CVE in SCA
- [ ] ❌ Requests 2.25.0 CVEs in SCA
- [ ] ⚠️ Security warnings in DAST

### Secure Pipeline Should Show:
- [ ] ✅ No SAST vulnerabilities
- [ ] ✅ No SCA vulnerabilities
- [ ] ✅ Clean DAST scan
- [ ] ✅ All stages pass

## 🔧 Troubleshooting Checklist

### If Pipeline Doesn't Start:
- [ ] Check GitLab runners are enabled
- [ ] Verify `.gitlab-ci.yml` is in root of repository
- [ ] Check for YAML syntax errors
- [ ] Ensure you pushed to correct branch

### If SCA Stage Fails Unexpectedly:
- [ ] Verify `requirements.txt` exists
- [ ] Check file is committed to Git
- [ ] Ensure Safety tool can access internet
- [ ] Check GitLab runner has network access

### If DAST Stage Fails:
- [ ] Check network connectivity
- [ ] Verify OWASP ZAP image can be pulled
- [ ] Check timeout settings
- [ ] Ensure target URL is accessible

### If Local Testing Fails:
- [ ] Verify Python version (3.11+)
- [ ] Check virtual environment is activated
- [ ] Ensure all dependencies installed
- [ ] Check for port conflicts (5000)

## 📊 Success Criteria

### You've Successfully Completed Setup When:
- [ ] Both pipelines run to completion
- [ ] Insecure pipeline shows expected vulnerabilities
- [ ] Secure pipeline shows clean results
- [ ] You can explain the difference between SAST, SCA, and DAST
- [ ] You understand each vulnerability and its fix
- [ ] You can navigate GitLab CI/CD interface
- [ ] You can read and interpret security scan results

## 🎓 Next Steps After Setup

### Beginner Level:
- [ ] Study the code differences
- [ ] Read all documentation
- [ ] Try to explain vulnerabilities to someone else
- [ ] Create a presentation about your findings

### Intermediate Level:
- [ ] Add a new vulnerability to insecure version
- [ ] Fix it in secure version
- [ ] Modify pipeline to add more checks
- [ ] Experiment with different security tools

### Advanced Level:
- [ ] Integrate additional security scanners
- [ ] Create custom security rules
- [ ] Implement security gates (block on critical)
- [ ] Build a complete DevSecOps workflow
- [ ] Add container scanning
- [ ] Implement secret detection

## 📝 Documentation Review Checklist

- [ ] Read `README.md` (main overview)
- [ ] Read `QUICK_START.md` (fast setup)
- [ ] Read `SECURITY_COMPARISON.md` (vulnerability details)
- [ ] Read `PIPELINE_EXPLAINED.md` (pipeline flow)
- [ ] Read `PROJECT_SUMMARY.md` (what was added)
- [ ] Read `insecure-cicd/README.md` (insecure guide)
- [ ] Read `secure-cicd/README.md` (secure guide)

## ✅ Final Verification

### Before Considering Setup Complete:
- [ ] Both GitLab projects created
- [ ] Both pipelines run successfully
- [ ] Security findings match expectations
- [ ] All documentation reviewed
- [ ] Local testing completed (if applicable)
- [ ] You understand the key concepts
- [ ] You can explain the project to others

## 🎉 Completion

Once all items are checked, you've successfully set up the DevSecOps CI/CD demo!

### Share Your Success:
- [ ] Take screenshots of pipeline results
- [ ] Document your learnings
- [ ] Share with your team or classmates
- [ ] Consider contributing improvements

---

**Need Help?** Refer to the troubleshooting sections in the README files or review the PIPELINE_EXPLAINED.md for detailed explanations.

**Ready to Learn More?** Check out the extension ideas in PROJECT_SUMMARY.md!
