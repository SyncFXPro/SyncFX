@echo off
cd /d %~dp0

:top
cls
echo ----------------------------------------
echo     SyncFX Terminal Command Runner
echo ----------------------------------------

set /p usercmd=What command do you want to run? 

echo.
echo Running: %usercmd%
echo.

:: Run command live, capture error level
call %usercmd%
set "exitcode=%ERRORLEVEL%"

echo.
if "%exitcode%"=="0" (
    echo [SUCCESS] Command completed successfully.
) else (
    echo [ERROR] That command returned an error code: %exitcode%
    echo Make sure the command is valid or spelled correctly.
)

echo.
pause
goto top
