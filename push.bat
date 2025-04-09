@echo off
cd /d %~dp0

echo Staging all changes...
git add .

echo.
set /p commitMsg="Enter commit message: "
git commit -m "%commitMsg%"

echo.
echo Pushing to GitHub...
git push

echo.
echo ✅ All done!
pause
