@echo off
title Foody - Localhost Server
echo ================================================================
echo             Starting Foody Food Ordering System
echo ================================================================
echo.
echo Customer Web App:   http://localhost:5000/
echo Admin Dashboard:    http://localhost:5000/admin.html
echo API Base URL:       http://localhost:5000/api/v1
echo.
echo ================================================================

cd /d "%~dp0Food.Ordering.System5-main\Website2\backend_py"

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python app.py
) else (
    if exist "C:\Users\nitin\AppData\Local\Programs\Python\Python312\python.exe" (
        "C:\Users\nitin\AppData\Local\Programs\Python\Python312\python.exe" app.py
    ) else (
        echo [ERROR] Python not found! Please install Python or add it to your PATH.
        pause
    )
)
pause
