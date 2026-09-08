@echo off
title Foody Python Backend Server
cd /d "%~dp0backend_py"
echo ====================================================
echo Starting Foody Python Flask Server (SQLite Database)...
echo Local Customer URL: http://localhost:5000/
echo Admin Portal URL:   http://localhost:5000/admin.html
echo ====================================================
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
