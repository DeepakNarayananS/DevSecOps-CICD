# Quick Start Guide

Get up and running with the DevSecOps CI/CD demo in 5 minutes!

## 🚀 Fastest Path to Results

### Step 1: Fork or Clone (1 minute)

```bash
# Clone the repository
git clone https://github.com/DeepakNarayananS/DevSecOps-CICD.git
cd DevSecOps-CICD
```

### Step 2: Push to GitLab (2 minutes)

```bash
# Add your GitLab remote
git remote add gitlab https://gitlab.com/YOUR-USERNAME/devsecops-cicd.git

# Push to GitLab (triggers pipeline)
git push gitlab main
```

### Step 3: Watch the Pipeline (2 minutes)

1. Go to your GitLab project
2. Click **CI/CD > Pipelines**
3. Watch the pipeline run automatically
4. Click on individual jobs to see results

## 📊 What to Look For

### Pipeline Stages:

**Test Stage** - Look for:
```
✅ Running basic test stage
✅ Code compiles successfully
```

**Code Quality Stage** - Look for:
```
✅ Running code quality checks
⚠️ Some quality issues detected (expected)
```

**SAST Stage** - Look for:
```
⚠️ Running SAST scan
⚠️ Security issues detected in code
```

**SCA Stage** - Look for:
```
⚠️ VULNERABILITIES FOUND: 4
- Flask 2.0.1: CVE-2023-30861 (HIGH)
- Jinja2 2.11.3: CVE-2024-22195 (MEDIUM)
- PyYAML 5.3.1: CVE-2020-14343 (CRITICAL)
```

## 🧪 Local Testing (Optional)

Want to test locally before pushing to GitLab?

```bash
# Install dependencies
pip install -r requirements.txt
pip install safety bandit

# Run SCA scan
safety check

# Run SAST scan
bandit -r . -f json

# Current version: Shows vulnerabilities ⚠️
# After fixes: Shows clean ✅
```

## 🎯 Next Steps

1. **Review Results** - Check the pipeline output for security findings
2. **Compare Code** - Look at root folder (insecure) vs secure/ folder (fixed)
3. **Apply Fixes** - Copy files from secure/ to root and push to see clean results
4. **Learn More** - Read README.md and SECURITY_COMPARISON.md

## 💡 Pro Tips

- **Artifacts**: Download DAST reports from the pipeline artifacts
- **Security Dashboard**: Check GitLab's Security & Compliance tab
- **Logs**: Click on any job to see detailed logs
- **Re-run**: Click "Run Pipeline" to test again after changes

## ❓ Troubleshooting

**Pipeline doesn't start?**
- Check that GitLab runners are enabled in Settings > CI/CD

**SCA job fails?**
- This is expected for the insecure version!
- Check the job logs to see which vulnerabilities were found

**Need help?**
- Check the main README.md
- Review the SECURITY_COMPARISON.md
- Look at the detailed README in each folder

## 📖 Documentation Structure

```
DevSecOps-CICD/
├── README.md                    # Main overview (start here)
├── QUICK_START.md              # This file
├── SECURITY_COMPARISON.md      # Detailed vulnerability analysis
├── insecure-cicd/
│   └── README.md               # Insecure version guide
└── secure-cicd/
    └── README.md               # Secure version guide
```

---

**Ready to start? Pick a version and deploy! 🚀**
