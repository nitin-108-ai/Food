@echo off
title Foody Python Backend Server
cd /d "%~dp0backend_py"
echo ====================================================
echo Starting Foody Python Flask Server (SQLite Database)...
echo Local Customer URL: http://localhost:5000/
echo Admin Portal URL:   http://localhost:5000/admin.html
echo ====================================================
"C:\Users\nitin\AppData\Local\Programs\Python\Python312\python.exe" app.py
pause
