@echo off
REM Quick GitHub setup script for Windows
REM Run this after creating a GitHub repository

echo.
echo 🚀 ChatApp GitHub Push Script
echo ==============================
echo.
echo Before running this script, please:
echo   1. Create a GitHub account at https://github.com
echo   2. Create a new repository named 'chatapp'
echo   3. Copy the repository URL
echo.
set /p REPO_URL="Enter your GitHub repository URL (https://github.com/...): "

echo.
echo Adding remote and pushing code...
git remote add origin %REPO_URL%
git branch -M main
git push -u origin main

echo.
echo ✅ Code pushed to GitHub!
echo.
echo Next steps:
echo   1. Go to https://render.com
echo   2. Create new Web Service
echo   3. Connect your GitHub repository
echo   4. Deploy!
echo.
pause
