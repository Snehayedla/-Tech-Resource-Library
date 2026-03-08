@echo off
echo Starting Tech Resource Library Backend...
echo.

cd backend

if not exist "venv\" (
    echo Creating virtual environment...
    py -m venv venv
    echo.
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt
echo.

if not exist "library.db" (
    echo Initializing database...
    python seed_data.py
    echo.
)

echo Starting FastAPI server...
echo Backend will be available at: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo.
uvicorn main:app --reload
