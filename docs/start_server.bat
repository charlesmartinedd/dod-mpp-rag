@echo off
REM Start local HTTP server for hosting glossary
cd /d "%~dp0"
echo Starting HTTP Server on http://localhost:8000
echo Glossary URL: http://localhost:8000/glossary.html
echo.
echo Press Ctrl+C to stop the server
echo.
python -m http.server 8000
pause
