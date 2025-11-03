# Quick Start Guide

Get up and running with the DevSecOps CI/CD demo in 5 minutes!

## 🚀 Fastest Path to Results

### Step 1: Choose Your Version (2 minutes)

Pick one to start with:
- **Insecure version** - See vulnerabilities in action
- **Secure version** - See clean security scans

### Step 2: Deploy to GitLab (2 minutes)

```bash
# Navigate to your chosen folder
cd DevSecOps-CICD/insecure-cicd
# OR
cd DevSecOps-CICD/secure-cicd

# Initialize and push
git init
git add .
git commit -m "Initial commit"
git remote add origin https://gitlab.com/YOUR-USERNAME/YOUR-PROJECT.git
git push -u origin main
```

### Step 3: Watch the Pipeline (1 minute)

1. Go to your GitLab project
2. Click **CI/CD > Pipelines**
3. Watch the pipeline run automatically
4. Click on individual jobs to see results

## 📊 What to Look For

### In the Insecure Pipeline:

**SCA Job** - Look for:
```
⚠️ VULNERABILITIES FOUND: 4
- Flask 2.0.1: CVE-2023-30861 (HIGH)
- Jinja2 2.11.3: CVE-2024-22195 (MEDIUM)
- PyYAML 5.3.1: CVE-2020-14343 (CRITICAL)
```

**SAST Job** - Look for:
- XSS vulnerability warnings
- Insecure deserialization alerts
- Debug mode warnings

### In the Secure Pipeline:

**SCA Job** - Look for:
```
✅ No known vulnerabilities detected!
```

**SAST Job** - Look for:
- Clean scan results
- No critical issues

## 🧪 Local Testing (Optional)

Want to test locally before pushing to GitLab?

```bash
# Install dependencies
pip install -r requirements.txt
pip install safety

# Run SCA scan
safety check

# Insecure version: Shows vulnerabilities ⚠️
# Secure version: Shows clean ✅
```

## 🎯 Next Steps

1. **Compare Results** - Deploy both versions and compare pipeline outputs
2. **Read the Code** - Look at the differences between vulnerable_app.py and secure_app.py
3. **Experiment** - Try modifying the code and see how it affects security scans
4. **Learn More** - Read the detailed READMEs in each folder

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
