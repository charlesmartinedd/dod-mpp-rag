@echo off
echo ============================================================
echo   DoD MPP RAG Web Application Launcher
echo ============================================================
echo.

cd /d "%~dp0..\src"

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo.
echo Installing/updating dependencies...
pip install -q -r requirements_web.txt

echo.
echo ============================================================
echo   Starting Web Application
echo ============================================================
echo   URL: http://localhost:8501
echo   Press Ctrl+C to stop the server
echo ============================================================
echo.

python start_webapp.py

pause
