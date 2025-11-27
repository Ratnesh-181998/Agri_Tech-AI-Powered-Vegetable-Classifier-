# Ninjacart CV Classification - GitHub Upload Script
# This script automates the GitHub upload process

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Ninjacart CV Classification" -ForegroundColor Green
Write-Host "  GitHub Upload Assistant" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/downloads" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Prompt for GitHub repository URL
Write-Host "Enter your GitHub repository URL:" -ForegroundColor Yellow
Write-Host "(Example: https://github.com/username/Ninjacart-CV-Classification.git)" -ForegroundColor Gray
$repoUrl = Read-Host "Repository URL"

if ([string]::IsNullOrWhiteSpace($repoUrl)) {
    Write-Host "✗ Repository URL is required!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Starting Upload Process" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Initialize Git repository
Write-Host "[1/6] Initializing Git repository..." -ForegroundColor Yellow
git init
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to initialize Git repository" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Git repository initialized" -ForegroundColor Green
Write-Host ""

# Add all files
Write-Host "[2/6] Adding files to staging area..." -ForegroundColor Yellow
Write-Host "(This respects .gitignore - large files will be excluded)" -ForegroundColor Gray
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to add files" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Files added successfully" -ForegroundColor Green
Write-Host ""

# Show what will be committed
Write-Host "Files to be committed:" -ForegroundColor Cyan
git status --short
Write-Host ""

# Confirm before committing
Write-Host "Do you want to proceed with the commit? (Y/N)" -ForegroundColor Yellow
$confirm = Read-Host
if ($confirm -ne "Y" -and $confirm -ne "y") {
    Write-Host "Upload cancelled by user" -ForegroundColor Yellow
    exit 0
}

# Create commit
Write-Host ""
Write-Host "[3/6] Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Ninjacart CV Classification - Full-stack AI vegetable classifier with 5 models"
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to create commit" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Commit created successfully" -ForegroundColor Green
Write-Host ""

# Rename branch to main
Write-Host "[4/6] Renaming branch to 'main'..." -ForegroundColor Yellow
git branch -M main
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to rename branch" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Branch renamed to 'main'" -ForegroundColor Green
Write-Host ""

# Add remote
Write-Host "[5/6] Adding remote repository..." -ForegroundColor Yellow
git remote add origin $repoUrl
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠ Remote 'origin' might already exist. Removing and re-adding..." -ForegroundColor Yellow
    git remote remove origin
    git remote add origin $repoUrl
}
Write-Host "✓ Remote repository added" -ForegroundColor Green
Write-Host ""

# Push to GitHub
Write-Host "[6/6] Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "(You may be prompted for GitHub credentials)" -ForegroundColor Gray
git push -u origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to push to GitHub" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "1. Authentication failed - Use a Personal Access Token instead of password" -ForegroundColor Gray
    Write-Host "2. Repository doesn't exist - Create it on GitHub first" -ForegroundColor Gray
    Write-Host "3. Network issues - Check your internet connection" -ForegroundColor Gray
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ✓ Upload Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your project has been successfully uploaded to GitHub!" -ForegroundColor Green
Write-Host "Repository URL: $repoUrl" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Visit your repository on GitHub" -ForegroundColor Gray
Write-Host "2. Add a description and topics in repository settings" -ForegroundColor Gray
Write-Host "3. (Optional) Add screenshots to enhance the README" -ForegroundColor Gray
Write-Host ""
Write-Host "Thank you for using Ninjacart CV Classification! 🚀" -ForegroundColor Green
