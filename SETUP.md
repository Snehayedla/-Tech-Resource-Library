# Setup Guide - Tech Resource Library

This guide will help you set up and run the Tech Resource Library application.

## Prerequisites

Before starting, ensure you have the following installed:

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify: `py --version` or `python --version`

2. **Node.js 16 or higher** (includes npm)
   - Download from: https://nodejs.org/
   - Verify: `node --version` and `npm --version`

3. **Git** (optional, for cloning)
   - Download from: https://git-scm.com/downloads

## Quick Setup (Windows)

### Option 1: Automated Setup (Recommended)

1. Double-click `setup.bat`
2. Wait for the setup to complete
3. Double-click `start-all.bat` to run both servers
4. Open http://localhost:5173 in your browser

### Option 2: Manual Setup

#### Backend Setup

1. Open Command Prompt or PowerShell
2. Navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Create virtual environment:
   ```bash
   py -m venv venv
   ```

4. Activate virtual environment:
   ```bash
   venv\Scripts\activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Initialize database:
   ```bash
   python seed_data.py
   ```

7. Start backend server:
   ```bash
   uvicorn main:app --reload
   ```

Backend will run at: http://localhost:8000

#### Frontend Setup

1. Open a new Command Prompt or PowerShell window
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start frontend server:
   ```bash
   npm run dev
   ```

Frontend will run at: http://localhost:5173

## Quick Setup (macOS/Linux)

### Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed_data.py
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Verification

After setup, verify everything is working:

1. **Backend**: Visit http://localhost:8000/docs
   - You should see the Swagger API documentation

2. **Frontend**: Visit http://localhost:5173
   - You should see the Tech Resource Library home page

3. **Test Search**: Search for "Python" or "React"
   - You should see categorized resources

## Troubleshooting

### Backend Issues

**"Python not found"**
- Install Python from python.org
- Ensure Python is added to PATH during installation

**"pip not found"**
- Reinstall Python with pip included
- Or install pip separately

**"Port 8000 already in use"**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

**"Database not found"**
```bash
cd backend
python seed_data.py
```

### Frontend Issues

**"npm not found"**
- Install Node.js from nodejs.org
- Restart your terminal after installation

**"Port 5173 already in use"**
- Vite will automatically use port 5174
- Or kill the process using port 5173

**"Cannot connect to backend"**
- Ensure backend is running on port 8000
- Check CORS settings in `backend/main.py`

### Database Issues

**"No resources found"**
- Re-run the seed script:
  ```bash
  cd backend
  python seed_data.py
  ```

**"Database locked"**
- Close all connections to the database
- Restart the backend server

## Development Mode

Both servers run in development mode with hot-reload:
- Backend: Changes to Python files auto-reload
- Frontend: Changes to React files auto-reload

## Production Build

### Frontend Production Build

```bash
cd frontend
npm run build
npm run preview
```

### Backend Production

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Next Steps

After successful setup:

1. Explore the API documentation at http://localhost:8000/docs
2. Try searching for different technologies
3. Check out the code structure in the README.md
4. Read CONTRIBUTING.md if you want to contribute

## Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review the main README.md
3. Check backend/README.md and frontend/README.md
4. Create an issue on GitHub (if applicable)

## Quick Reference

| Component | URL | Description |
|-----------|-----|-------------|
| Frontend | http://localhost:5173 | Main application |
| Backend API | http://localhost:8000 | API server |
| API Docs (Swagger) | http://localhost:8000/docs | Interactive API documentation |
| API Docs (ReDoc) | http://localhost:8000/redoc | Alternative API documentation |

## Batch Scripts (Windows)

- `setup.bat` - Complete setup (run once)
- `start-all.bat` - Start both servers
- `start-backend.bat` - Start backend only
- `start-frontend.bat` - Start frontend only

Happy coding! 🚀
