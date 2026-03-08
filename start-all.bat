@echo off
echo ========================================
echo  Tech Resource Library - Quick Start
echo ========================================
echo.
echo Starting both Backend and Frontend...
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C in each window to stop servers
echo.
pause

start "Backend Server" cmd /k "cd backend && call venv\Scripts\activate.bat && uvicorn main:app --reload"
timeout /t 3 /nobreak > nul
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo.
echo Both servers are starting in separate windows...
echo.
