# Backend - Tech Resource Library API

FastAPI backend for the Tech Resource Library application.

## Structure

```
backend/
├── routes/              # API route handlers
│   ├── __init__.py      # Package initialization
│   ├── technologies.py  # Technology endpoints
│   └── resources.py     # Resource endpoints
├── main.py              # FastAPI app entry point
├── models.py            # SQLAlchemy models
├── database.py          # Database configuration
├── seed_data.py         # Database seeding script
├── requirements.txt     # Python dependencies
└── library.db           # SQLite database (auto-generated)
```

## Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize database:
   ```bash
   python seed_data.py
   ```

5. Run server:
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database

The application uses SQLite for simplicity. The database file `library.db` is created automatically when you run the seed script.

### Models

**Technology**
- id: Integer (Primary Key)
- name: String (Unique)
- description: String

**Resource**
- id: Integer (Primary Key)
- technology_id: Integer (Foreign Key)
- title: String
- url: String
- type: String (video/notes/reference)
- views: Integer
- language: String
- created_at: DateTime

## Adding New Endpoints

1. Create route handler in `routes/` directory
2. Import and include router in `main.py`
3. Test using Swagger UI

## Environment Variables

Create a `.env` file (optional):
```env
DATABASE_URL=sqlite:///./library.db
API_HOST=0.0.0.0
API_PORT=8000
```
