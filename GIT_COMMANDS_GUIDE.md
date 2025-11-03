# 🚀 Git Commands Guide - DevSecOps CI/CD Project

A comprehensive, step-by-step guide to all Git commands used in this project with visual examples and explanations.

---

## 📋 Table of Contents

1. [Initial Setup](#-initial-setup)
2. [Working with GitLab](#-working-with-gitlab)
3. [Working with GitHub](#-working-with-github)
4. [Daily Workflow](#-daily-workflow)
5. [Branch Management](#-branch-management)
6. [Troubleshooting](#-troubleshooting)
7. [Advanced Commands](#-advanced-commands)
8. [Quick Reference](#-quick-reference)

---

## 🎯 Initial Setup

### Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/DeepakNarayananS/DevSecOps-CICD.git
cd DevSecOps-CICD
```

**What this does:**
- Downloads the entire project to your local machine
- Creates a `.git` folder with version history
- Sets up `origin` remote pointing to GitHub

**Visual:**
```
GitHub Repository
       ↓
   [git clone]
       ↓
Local Machine
```

---

### Step 2: Configure Git (First Time Only)

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

**What this does:**
- Sets your identity for all commits
- Required for making commits
- Stored in `~/.gitconfig`

---

### Step 3: Check Repository Status

```bash
# View current status
git status
```

**Output Example:**
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**What this shows:**
- Current branch name
- Modified files
- Staged files
- Untracked files

---

## 🦊 Working with GitLab

### Step 1: Add GitLab Remote

```bash
# Add GitLab as a remote repository
git remote add gitlab https://gitlab.com/dnsoc-group/devsecops-cicd.git

# Verify remotes
git remote -v
```

**Output:**
```
gitlab  https://gitlab.com/dnsoc-group/devsecops-cicd.git (fetch)
gitlab  https://gitlab.com/dnsoc-group/devsecops-cicd.git (push)
origin  https://github.com/DeepakNarayananS/DevSecOps-CICD.git (fetch)
origin  https://github.com/DeepakNarayananS/DevSecOps-CICD.git (push)
```

**Visual:**
```
Local Repository
    ├── origin  → GitHub
    └── gitlab  → GitLab
```

---

### Step 2: Push to GitLab

```bash
# Push main branch to GitLab
git push gitlab main

# Push with upstream tracking
git push -u gitlab main
```

**What `-u` does:**
- Sets up tracking between local and remote branch
- Future pushes can use just `git push`
- Links local `main` to `gitlab/main`

**Visual:**
```
Local main
     ↓
[git push]
     ↓
GitLab main
     ↓
[Pipeline Triggered]
```

---

### Step 3: Pull from GitLab

```bash
# Fetch and merge changes from GitLab
git pull gitlab main

# Pull with rebase (cleaner history)
git pull gitlab main --rebase
```

**Difference:**
- **Merge**: Creates merge commit
- **Rebase**: Replays your commits on top

**Visual (Merge):**
```
Before:
  A---B---C  (local)
       \
        D---E  (gitlab)

After:
  A---B---C---M  (local)
       \     /
        D---E
```

**Visual (Rebase):**
```
Before:
  A---B---C  (local)
       \
        D---E  (gitlab)

After:
  A---D---E---B'---C'  (local)
```

---

## 🐙 Working with GitHub

### Step 1: Add GitHub Remote

```bash
# Add GitHub as a remote (if not already added)
git remote add github https://github.com/DeepakNarayananS/DevSecOps-CICD.git

# Or rename existing origin
git remote rename origin github
```

---

### Step 2: Push to GitHub

```bash
# Push to GitHub
git push github main

# Force push (use with caution!)
git push github main --force
```

**⚠️ Warning:** Force push overwrites remote history. Use only when necessary!

---

### Step 3: Sync Both Remotes

```bash
# Push to both GitLab and GitHub
git push gitlab main
git push github main

# Or create an alias (one-time setup)
git config alias.pushall '!git push gitlab main && git push github main'

# Then use
git pushall
```

**Visual:**
```
Local Repository
       ↓
   [git push]
    ↙     ↘
GitLab   GitHub
```

---

## 💼 Daily Workflow

### Step 1: Check Status

```bash
# Always start by checking status
git status
```

---

### Step 2: Make Changes

```bash
# Edit files in your editor
# Example: Edit vulnerable_app.py
```

---

### Step 3: Stage Changes

```bash
# Stage specific file
git add vulnerable_app.py

# Stage all Python files
git add *.py

# Stage all changes
git add .

# Stage all changes including deletions
git add -A
```

**What each does:**
- `git add <file>`: Stage specific file
- `git add *.py`: Stage all .py files
- `git add .`: Stage new and modified files
- `git add -A`: Stage everything (new, modified, deleted)

**Visual:**
```
Working Directory
       ↓
   [git add]
       ↓
Staging Area
       ↓
   [git commit]
       ↓
Local Repository
```

---

### Step 4: Commit Changes

```bash
# Commit with message
git commit -m "Fix: Update Flask to secure version"

# Commit with detailed message
git commit -m "Fix: Update Flask to secure version" -m "- Updated Flask from 2.0.1 to 3.0.0
- Fixes CVE-2023-30861
- All security tests now pass"

# Commit all tracked changes (skip staging)
git commit -am "Quick fix"
```

**Good Commit Messages:**
```
✅ Fix: Update vulnerable dependencies
✅ Feature: Add SAST scanning with Bandit
✅ Docs: Update README with new structure
✅ Refactor: Reorganize project structure
✅ Test: Add security test cases

❌ updated stuff
❌ fix
❌ changes
```

**Commit Message Format:**
```
Type: Short description (50 chars max)

Detailed explanation if needed (72 chars per line)
- Bullet points for multiple changes
- Reference issue numbers if applicable

Fixes #123
```

---

### Step 5: Push Changes

```bash
# Push to GitLab (triggers CI/CD pipeline)
git push gitlab main

# Push to GitHub (for backup/sharing)
git push github main
```

---

### Step 6: Verify Pipeline

```bash
# After pushing to GitLab, check pipeline status
# Visit: https://gitlab.com/dnsoc-group/devsecops-cicd/-/pipelines
```

**Visual:**
```
[git push gitlab main]
         ↓
   GitLab receives
         ↓
   Pipeline triggered
         ↓
    ┌─────────┐
    │  Test   │ ✅
    └─────────┘
         ↓
    ┌─────────┐
    │  Code   │ ✅
    │ Quality │
    └─────────┘
         ↓
    ┌─────────┐
    │  SAST   │ ⚠️
    └─────────┘
         ↓
    ┌─────────┐
    │   SCA   │ ⚠️
    └─────────┘
```

---

## 🌿 Branch Management

### Create a New Branch

```bash
# Create and switch to new branch
git checkout -b feature/add-dast-scanning

# Or using newer syntax
git switch -c feature/add-dast-scanning
```

**Visual:**
```
main
  │
  A---B---C
          │
          └─→ feature/add-dast-scanning
```

---

### Switch Between Branches

```bash
# Switch to existing branch
git checkout main
git switch main  # Newer syntax

# List all branches
git branch

# List all branches including remote
git branch -a
```

**Output:**
```
* main
  feature/add-dast-scanning
  remotes/gitlab/main
  remotes/github/main
```

---

### Merge Branches

```bash
# Switch to main branch
git checkout main

# Merge feature branch
git merge feature/add-dast-scanning

# Delete merged branch
git branch -d feature/add-dast-scanning
```

**Visual:**
```
Before:
main:     A---B---C
                  \
feature:           D---E

After merge:
main:     A---B---C---M
                  \   /
feature:           D-E
```

---

### Push Branch to Remote

```bash
# Push new branch to GitLab
git push gitlab feature/add-dast-scanning

# Push with upstream tracking
git push -u gitlab feature/add-dast-scanning
```

---

## 🔧 Troubleshooting

### Undo Last Commit (Keep Changes)

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1

# Undo last commit, discard changes (DANGEROUS!)
git reset --hard HEAD~1
```

**Visual:**
```
--soft:   Commit → Staging Area
--mixed:  Commit → Working Directory
--hard:   Commit → Deleted
```

---

### Discard Local Changes

```bash
# Discard changes in specific file
git checkout -- vulnerable_app.py
git restore vulnerable_app.py  # Newer syntax

# Discard all local changes
git checkout -- .
git restore .

# Remove untracked files
git clean -fd
```

**⚠️ Warning:** These commands permanently delete changes!

---

### Resolve Merge Conflicts

```bash
# When merge conflict occurs
git status  # Shows conflicted files

# Edit conflicted files manually
# Look for conflict markers:
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> branch-name

# After resolving
git add <resolved-file>
git commit -m "Merge: Resolve conflicts"
```

**Conflict Markers:**
```python
<<<<<<< HEAD
flask==2.0.1  # Your version
=======
flask==3.0.0  # Their version
>>>>>>> feature-branch
```

**After resolving:**
```python
flask==3.0.0  # Keep the secure version
```

---

### Fix "Rejected Push" Error

```bash
# Error: Updates were rejected because remote contains work

# Solution 1: Pull and merge
git pull gitlab main
git push gitlab main

# Solution 2: Pull with rebase
git pull gitlab main --rebase
git push gitlab main

# Solution 3: Force push (DANGEROUS - use only if you're sure!)
git push gitlab main --force
```

**When to use force push:**
- ✅ On your personal feature branch
- ✅ When you're the only one working on the branch
- ❌ NEVER on main/master branch
- ❌ NEVER on shared branches

---

### Recover Deleted Commits

```bash
# View reflog (history of HEAD movements)
git reflog

# Output shows:
# 7544d53 HEAD@{0}: commit: Docs update
# 47d3805 HEAD@{1}: commit: Secure code
# 8e60b14 HEAD@{2}: commit: Insecure code

# Recover to specific commit
git reset --hard HEAD@{2}
```

---

## 🎓 Advanced Commands

### View Commit History

```bash
# Simple log
git log

# One line per commit
git log --oneline

# With graph
git log --oneline --graph --all

# Last 5 commits
git log -5

# Commits by author
git log --author="Deepak"

# Commits in date range
git log --since="2 weeks ago"
```

**Beautiful Log Output:**
```bash
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

**Output:**
```
* 7544d53 - (HEAD -> main) Docs update (2 hours ago) <Deepak>
* 47d3805 - Secure code (3 hours ago) <Deepak>
* 8e60b14 - Insecure code (4 hours ago) <Deepak>
```

---

### View Changes

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged

# Show changes in specific file
git diff vulnerable_app.py

# Compare branches
git diff main..feature/add-dast

# Compare with remote
git diff main origin/main
```

---

### Stash Changes

```bash
# Save changes temporarily
git stash

# Save with message
git stash save "WIP: Adding DAST scanning"

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove stash
git stash pop

# Apply specific stash
git stash apply stash@{1}

# Delete stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

**Use Case:**
```bash
# Working on feature
git stash  # Save work

# Switch to fix urgent bug
git checkout main
# Fix bug
git commit -am "Hotfix: Critical security patch"
git push

# Return to feature
git checkout feature-branch
git stash pop  # Restore work
```

---

### Cherry-Pick Commits

```bash
# Apply specific commit from another branch
git cherry-pick <commit-hash>

# Example
git cherry-pick 7544d53
```

**Visual:**
```
main:     A---B---C
                  
feature:  D---E---F
              ↓
          [cherry-pick E]
              ↓
main:     A---B---C---E'
```

---

### Rebase Interactive

```bash
# Rebase last 3 commits
git rebase -i HEAD~3

# Opens editor with:
# pick 7544d53 Docs update
# pick 47d3805 Secure code
# pick 8e60b14 Insecure code

# Change 'pick' to:
# - reword: Change commit message
# - edit: Modify commit
# - squash: Combine with previous
# - drop: Remove commit
```

---

### Tagging Releases

```bash
# Create lightweight tag
git tag v1.0.0

# Create annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# List tags
git tag

# Push tag to remote
git push gitlab v1.0.0

# Push all tags
git push gitlab --tags

# Delete tag
git tag -d v1.0.0
git push gitlab :refs/tags/v1.0.0
```

---

## 📚 Quick Reference

### Essential Commands

```bash
# Status and Info
git status                    # Check status
git log --oneline            # View history
git diff                     # View changes

# Basic Workflow
git add .                    # Stage all changes
git commit -m "message"      # Commit changes
git push gitlab main         # Push to GitLab
git push github main         # Push to GitHub

# Branching
git branch                   # List branches
git checkout -b feature      # Create branch
git merge feature            # Merge branch
git branch -d feature        # Delete branch

# Syncing
git pull gitlab main         # Pull from GitLab
git fetch --all              # Fetch all remotes
git remote -v                # List remotes

# Undo
git reset HEAD~1             # Undo last commit
git checkout -- file         # Discard changes
git stash                    # Save changes temporarily
```

---

### Project-Specific Commands

```bash
# Initial Setup
git clone https://github.com/DeepakNarayananS/DevSecOps-CICD.git
cd DevSecOps-CICD
git remote add gitlab https://gitlab.com/dnsoc-group/devsecops-cicd.git

# Daily Workflow
git status
git add .
git commit -m "Insecure: Update vulnerable dependencies"
git push gitlab main         # Triggers CI/CD pipeline
git push github main         # Backup to GitHub

# Update Dependencies
git add requirements.txt
git commit -m "Fix: Update Flask to 3.0.0 (CVE-2023-30861)"
git push gitlab main

# Sync Both Remotes
git pull gitlab main
git pull github main
git push gitlab main
git push github main
```

---

### Commit Message Templates

```bash
# Insecure Code Changes
git commit -m "Insecure: Add vulnerable dependency example"
git commit -m "Insecure: Demonstrate XSS vulnerability"

# Secure Code Changes
git commit -m "Secure: Fix XSS with input escaping"
git commit -m "Secure: Update to safe dependencies"

# Documentation
git commit -m "Docs: Update README with new structure"
git commit -m "Docs: Add security comparison guide"

# Pipeline Changes
git commit -m "CI: Add SAST scanning stage"
git commit -m "CI: Configure SCA with Safety"

# Fixes
git commit -m "Fix: Resolve merge conflict in requirements.txt"
git commit -m "Fix: Correct YAML syntax in pipeline"
```

---

## 🎨 Git Workflow Visualization

### Complete Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT WORKFLOW                      │
└─────────────────────────────────────────────────────────────┘

1. Clone Repository
   GitHub/GitLab → Local Machine
   
2. Make Changes
   Edit Files → Working Directory
   
3. Stage Changes
   Working Directory → Staging Area
   [git add]
   
4. Commit Changes
   Staging Area → Local Repository
   [git commit]
   
5. Push to GitLab
   Local Repository → GitLab
   [git push gitlab main]
   
6. Pipeline Runs
   GitLab → CI/CD Pipeline
   Test → Code Quality → SAST → SCA
   
7. Push to GitHub
   Local Repository → GitHub
   [git push github main]
   
8. Pull Updates
   GitLab/GitHub → Local Repository
   [git pull]
```

---

### File States

```
┌──────────────┐
│  Untracked   │  New files not in Git
└──────────────┘
       ↓ [git add]
┌──────────────┐
│   Staged     │  Ready to commit
└──────────────┘
       ↓ [git commit]
┌──────────────┐
│  Committed   │  Saved in repository
└──────────────┘
       ↓ [git push]
┌──────────────┐
│    Remote    │  On GitLab/GitHub
└──────────────┘
```

---

## 🔐 Security Best Practices

### Commit Signing

```bash
# Generate GPG key
gpg --gen-key

# List keys
gpg --list-secret-keys --keyid-format LONG

# Configure Git to use key
git config --global user.signingkey <KEY_ID>

# Sign commits
git commit -S -m "Signed commit"

# Always sign commits
git config --global commit.gpgsign true
```

---

### Credential Management

```bash
# Cache credentials (15 minutes)
git config --global credential.helper cache

# Cache for 1 hour
git config --global credential.helper 'cache --timeout=3600'

# Store credentials (less secure)
git config --global credential.helper store

# Use SSH instead of HTTPS (recommended)
git remote set-url gitlab git@gitlab.com:dnsoc-group/devsecops-cicd.git
```

---

## 📖 Additional Resources

### Official Documentation
- [Git Documentation](https://git-scm.com/doc)
- [GitLab CI/CD Docs](https://docs.gitlab.com/ee/ci/)
- [GitHub Docs](https://docs.github.com/)

### Interactive Learning
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Git Immersion](http://gitimmersion.com/)
- [Oh My Git!](https://ohmygit.org/)

### Cheat Sheets
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitLab Git Cheat Sheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)

---

## 💡 Pro Tips

### Aliases for Common Commands

```bash
# Add to ~/.gitconfig or use git config --global

git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --oneline --graph --all'

# Usage
git st          # Instead of git status
git co main     # Instead of git checkout main
git visual      # Beautiful log
```

---

### Useful Configurations

```bash
# Colorful output
git config --global color.ui auto

# Default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim

# Default branch name
git config --global init.defaultBranch main

# Auto-correct typos
git config --global help.autocorrect 1

# Show original state in conflicts
git config --global merge.conflictstyle diff3
```

---

## 🎯 Summary

This guide covered:
- ✅ Initial repository setup
- ✅ Working with GitLab and GitHub
- ✅ Daily development workflow
- ✅ Branch management
- ✅ Troubleshooting common issues
- ✅ Advanced Git commands
- ✅ Security best practices

**Remember:**
- Commit often with clear messages
- Push to GitLab to trigger CI/CD
- Keep GitHub as backup
- Use branches for features
- Pull before you push

---

**Happy Coding! 🚀 Stay Secure! 🔐**
