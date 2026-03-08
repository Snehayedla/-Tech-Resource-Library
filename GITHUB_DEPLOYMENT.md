# GitHub Deployment Guide

This guide will help you deploy the Tech Resource Library project to GitHub.

## Prerequisites

- Git installed on your system
- GitHub account (create one at https://github.com if you don't have)

## Step-by-Step Deployment

### 1. Configure Git (First Time Only)

Open Command Prompt or PowerShell and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email.

### 2. Initialize Git Repository (Already Done)

The repository is already initialized. You can verify with:

```bash
git status
```

### 3. Add All Files to Git

```bash
git add .
```

This stages all files for commit.

### 4. Create First Commit

```bash
git commit -m "Initial commit: Tech Resource Library full-stack application"
```

### 5. Create GitHub Repository

1. Go to https://github.com
2. Click the "+" icon in the top right
3. Select "New repository"
4. Fill in the details:
   - **Repository name**: `tech-resource-library` (or your preferred name)
   - **Description**: "Full-stack web application for curated tech learning resources"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

### 6. Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/tech-resource-library.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 7. Verify Deployment

1. Refresh your GitHub repository page
2. You should see all your project files
3. The README.md will be displayed on the repository homepage

## Quick Commands Reference

```bash
# Check repository status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline
```

## Making Future Updates

After making changes to your code:

```bash
# 1. Check what changed
git status

# 2. Add changes
git add .

# 3. Commit with descriptive message
git commit -m "Description of what you changed"

# 4. Push to GitHub
git push origin main
```

## Common Issues and Solutions

### Issue: "Permission denied (publickey)"

**Solution**: Set up SSH key or use HTTPS with personal access token

For HTTPS with token:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Use token as password when pushing

### Issue: "Repository not found"

**Solution**: Check the remote URL

```bash
git remote -v
git remote set-url origin https://github.com/YOUR_USERNAME/tech-resource-library.git
```

### Issue: "Failed to push some refs"

**Solution**: Pull first, then push

```bash
git pull origin main --rebase
git push origin main
```

### Issue: "Large files warning"

**Solution**: The .gitignore already excludes large files like node_modules, venv, and database files.

## What Gets Pushed to GitHub

✅ **Included:**
- All source code (frontend & backend)
- Configuration files
- Documentation (README, setup guides)
- Requirements files (package.json, requirements.txt)

❌ **Excluded (via .gitignore):**
- node_modules/
- venv/
- __pycache__/
- *.db (database files)
- .env files
- IDE settings

## Repository Structure on GitHub

```
tech-resource-library/
├── backend/              # Backend API code
├── frontend/             # React frontend code
├── README.md             # Main documentation
├── SETUP.md              # Setup instructions
├── CONTRIBUTING.md       # Contribution guidelines
├── .gitignore            # Git ignore rules
└── setup scripts         # Batch files for Windows
```

## Next Steps After GitHub Deployment

1. **Add Repository Description**: Edit repository settings on GitHub
2. **Add Topics**: Add relevant topics like `react`, `fastapi`, `python`, `javascript`
3. **Enable Issues**: For bug tracking and feature requests
4. **Add License**: Consider adding MIT or Apache 2.0 license
5. **Deploy to Vercel**: Follow DEPLOYMENT.md for Vercel deployment

## Collaboration

To allow others to contribute:

1. Share your repository URL
2. Others can fork your repository
3. They make changes and create pull requests
4. You review and merge their changes

## GitHub Repository URL

After deployment, your repository will be at:
```
https://github.com/YOUR_USERNAME/tech-resource-library
```

Share this URL with others to showcase your project!

## Cloning Your Repository

Others (or you on another machine) can clone with:

```bash
git clone https://github.com/YOUR_USERNAME/tech-resource-library.git
cd tech-resource-library
```

Then follow SETUP.md to install dependencies and run the project.

---

**Need Help?**
- GitHub Docs: https://docs.github.com
- Git Basics: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
- Create an issue in your repository for project-specific questions
