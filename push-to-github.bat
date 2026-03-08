@echo off
echo ========================================
echo  Push to GitHub
echo ========================================
echo.

REM Check if remote exists
git remote -v > nul 2>&1
if errorlevel 1 (
    echo ERROR: No remote repository configured!
    echo.
    echo Please run these commands first:
    echo   git remote add origin https://github.com/YOUR_USERNAME/tech-resource-library.git
    echo   git branch -M main
    echo.
    echo Replace YOUR_USERNAME with your actual GitHub username
    echo.
    pause
    exit /b 1
)

echo Current branch:
git branch
echo.

echo Checking for changes...
git status
echo.

set /p confirm="Do you want to push to GitHub? (y/n): "
if /i not "%confirm%"=="y" (
    echo Push cancelled.
    pause
    exit /b 0
)

echo.
echo Pushing to GitHub...
git push origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo  Push Failed!
    echo ========================================
    echo.
    echo Common solutions:
    echo 1. Make sure you created the repository on GitHub
    echo 2. Check your internet connection
    echo 3. Verify the remote URL: git remote -v
    echo 4. Try: git push -u origin main
    echo.
) else (
    echo.
    echo ========================================
    echo  Successfully Pushed to GitHub!
    echo ========================================
    echo.
    echo Your code is now on GitHub!
    echo View it at: https://github.com/YOUR_USERNAME/tech-resource-library
    echo.
)

pause
