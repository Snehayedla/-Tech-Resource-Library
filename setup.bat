@echo off
echo ========================================
echo  Tech Resource Library - Setup
echo ========================================
echo.
echo This script will set up the entire project
echo.
pause

REM Backend Setup
echo.
echo [1/4] Setting up Backend...
echo ========================================
cd backend

if not exist "venv\" (
    echo Creating Python virtual environment...
    py -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Please ensure Python is installed
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo Initializing database with seed data...
python seed_data.py
if errorlevel 1 (
    echo ERROR: Failed to initialize database
    pause
    exit /b 1
)

cd ..

REM Frontend Setup
echo.
echo [2/4] Setting up Frontend...
echo ========================================
cd frontend

echo Installing Node.js dependencies...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install Node dependencies
    echo Please ensure Node.js and npm are installed
    pause
    exit /b 1
)

cd ..

echo.
echo [3/4] Verifying Setup...
echo ========================================
echo Checking database...
cd backend
call venv\Scripts\python.exe -c "from database import SessionLocal; from models import Technology; db = SessionLocal(); count = db.query(Technology).count(); print(f'✓ Database initialized with {count} technologies'); db.close()"
cd ..

echo.
echo [4/4] Setup Complete!
echo ========================================
echo.
echo ✓ Backend setup complete
echo ✓ Frontend setup complete
echo ✓ Database initialized
echo.
echo Next steps:
echo   1. Run 'start-all.bat' to start both servers
echo   2. Or run 'start-backend.bat' and 'start-frontend.bat' separately
echo   3. Open http://localhost:5173 in your browser
echo.
echo API Documentation: http://localhost:8000/docs
echo.
pause
