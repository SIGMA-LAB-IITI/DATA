@echo off
setlocal

:: Change this to your actual repository path
set REPO_PATH=C:\Users\SIGMA-W-VT\DATA

:: Change this to your desired commit message
set COMMIT_MESSAGE=Automatic commit

:: Navigate to the repository directory
cd %REPO_PATH%

:: Add all changes and commit
git add .
git commit -m "%COMMIT_MESSAGE%"

:: Push to the remote repository (change origin and branch as needed)
git push origin main

endlocal