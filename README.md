# 📚 Tech Resource Library

> A full-stack web application that helps students find curated learning resources for popular programming technologies in one place.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat&logo=react)](https://reactjs.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite)](https://www.sqlite.org/)

## 🎯 Project Overview

Tech Resource Library is a full-stack platform where students can search for any programming technology and instantly access curated learning resources including YouTube videos, tutorials, notes, and official documentation - all categorized and sorted by popularity. This eliminates the need to search across multiple platforms.

### Key Features

- 🔍 **Smart Search** - Find resources for 19+ technologies instantly
- 📊 **Categorized Content** - Videos, Notes, and References organized separately  
- 🎯 **Popularity Sorting** - Resources ranked by views and community recommendations
- 🚀 **Fast & Lightweight** - Built with modern tech stack for optimal performance
- 🎨 **Clean UI** - Intuitive, beginner-friendly interface
- 🔓 **No Authentication** - Open access for all students
- 📱 **Responsive Design** - Works seamlessly on all devices
- 💾 **638+ Resources** - Comprehensive collection across 19 technologies

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database (no setup required)
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - Lightning-fast ASGI server

### Frontend
- **React 18** - UI library with hooks
- **Vite** - Next-generation frontend tooling
- **React Router** - Client-side routing
- **Axios** - Promise-based HTTP client
- **CSS3** - Modern styling

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Node.js 16+** and npm ([Download](https://nodejs.org/))
- **Git** ([Download](https://git-scm.com/downloads))

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd tech-resource-library
```

### 2️⃣ Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database with seed data
python seed_data.py

# Start the backend server
uvicorn main:app --reload
```

✅ Backend will be running at: **http://localhost:8000**
📖 API Documentation (Swagger): **http://localhost:8000/docs**

### 3️⃣ Frontend Setup

Open a new terminal window:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend will be running at: **http://localhost:5173**

## 📁 Project Structure

```
tech-resource-library/
│
├── backend/                         # Backend API (FastAPI + SQLite)
│   ├── routes/                      # API route handlers
│   │   ├── __init__.py              # Routes package initialization
│   │   ├── technologies.py          # GET /technologies endpoint
│   │   └── resources.py             # GET/POST/DELETE /resources endpoints
│   │
│   ├── api/                         # Vercel serverless functions
│   │   └── index.py                 # Vercel entry point
│   │
│   ├── main.py                      # FastAPI app entry point & CORS config
│   ├── models.py                    # SQLAlchemy models (Technology, Resource)
│   ├── database.py                  # Database connection & session management
│   ├── seed_data.py                 # Database initialization with 638+ resources
│   ├── requirements.txt             # Python dependencies (FastAPI, SQLAlchemy, etc.)
│   ├── .env.example                 # Environment variables template
│   ├── vercel.json                  # Vercel deployment configuration
│   └── library.db                   # SQLite database (auto-generated)
│
├── frontend/                        # React frontend (Vite)
│   ├── src/
│   │   ├── components/              # Reusable React components
│   │   │   ├── SearchBar.jsx        # Search input with suggestions
│   │   │   └── ResourceCard.jsx     # Resource display card
│   │   │
│   │   ├── pages/                   # Page components
│   │   │   ├── Home.jsx             # Landing page with search & tech cards
│   │   │   └── Results.jsx          # Search results with categorized resources
│   │   │
│   │   ├── services/                # API integration layer
│   │   │   └── api.js               # Axios HTTP client & API methods
│   │   │
│   │   ├── App.jsx                  # Main app with React Router
│   │   ├── main.jsx                 # React entry point
│   │   └── index.css                # Global styles & responsive design
│   │
│   ├── index.html                   # HTML template
│   ├── package.json                 # Node dependencies & scripts
│   ├── vite.config.js               # Vite build configuration
│   └── .env.example                 # Frontend environment variables
│
├── .gitignore                       # Git ignore rules (node_modules, venv, .db)
├── .vscode/                         # VS Code settings (optional)
├── LICENSE                          # MIT License
├── README.md                        # Project documentation (this file)
│
└── Windows Scripts/                 # Quick start scripts for Windows
    ├── setup.bat                    # Complete project setup
    ├── start-all.bat                # Start both servers
    ├── start-backend.bat            # Start backend only
    └── start-frontend.bat           # Start frontend only
```

### Key Files Explained

**Backend:**
- `main.py` - FastAPI application with CORS middleware and route registration
- `models.py` - Database schema: Technology (id, name, description) & Resource (id, technology_id, title, url, type, views, language, created_at)
- `database.py` - SQLAlchemy engine, session factory, and database connection
- `seed_data.py` - Populates database with 19 technologies and 638+ curated resources
- `routes/technologies.py` - Returns list of all available technologies
- `routes/resources.py` - Returns categorized resources (videos/notes/references) for a technology

**Frontend:**
- `App.jsx` - React Router setup with Home and Results routes
- `pages/Home.jsx` - Search interface with technology cards
- `pages/Results.jsx` - Displays resources in 3 categories (Videos, Notes, References)
- `components/SearchBar.jsx` - Search input component
- `components/ResourceCard.jsx` - Individual resource display card
- `services/api.js` - Centralized API calls using Axios

## 🔌 API Endpoints

### Technologies

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/technologies` | Get all available technologies | Array of technology objects |

### Resources

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| GET | `/resources/{technology_name}` | Get resources for a specific technology | - | Object with videos, notes, references |
| POST | `/resources` | Add a new resource | `ResourceCreate` | Created resource with ID |
| DELETE | `/resources/{id}` | Delete a resource by ID | - | Success message |

### Example API Responses

**GET /technologies**
```json
[
  {
    "id": 1,
    "name": "Python",
    "description": "High-level programming language"
  }
]
```

**GET /resources/Python**
```json
{
  "technology": {
    "id": 1,
    "name": "Python",
    "description": "High-level programming language"
  },
  "videos": [
    {
      "id": 1,
      "title": "Python Tutorial for Beginners",
      "url": "https://youtube.com/...",
      "views": 5000000
    }
  ],
  "notes": [...],
  "references": [...]
}
```

## 💾 Database Schema

### Technologies Table
```sql
CREATE TABLE technologies (
    id INTEGER PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL,
    description VARCHAR
);
```

### Resources Table
```sql
CREATE TABLE resources (
    id INTEGER PRIMARY KEY,
    technology_id INTEGER NOT NULL,
    title VARCHAR NOT NULL,
    url VARCHAR NOT NULL,
    type VARCHAR NOT NULL,  -- 'video', 'notes', or 'reference'
    views INTEGER DEFAULT 0,
    language VARCHAR DEFAULT 'English',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (technology_id) REFERENCES technologies(id)
);
```

## 🎓 Available Technologies

The application includes resources for 19 popular technologies:

- **Languages**: Python, Java, JavaScript, TypeScript, SQL
- **Frontend**: React, Next.js, HTML, CSS
- **Backend**: Node.js, Django, FastAPI, Spring Boot
- **Databases**: MongoDB, PostgreSQL, Redis
- **Tools**: Git, Docker, Linux

Each technology includes:
- 📹 Top 10 YouTube videos (from channels like Telusko, freeCodeCamp, Programming with Mosh)
- 📝 Top 10 tutorials and notes (from GeeksforGeeks, W3Schools, MDN, etc.)
- 📖 Top 10 references (official docs, GitHub repos, developer guides)

## 🎮 Usage Guide

1. **Start both servers** (backend and frontend)
2. **Open your browser** and navigate to `http://localhost:5173`
3. **Search for a technology** (e.g., "Python", "React", "JavaScript")
4. **Browse categorized resources**:
   - 🎥 Videos section with embedded previews
   - 📝 Notes section with tutorial links
   - 📖 References section with documentation
5. **Click any resource** to open it in a new tab

## 🔧 Development

### Adding New Technologies

1. Add technology to database via API or seed script
2. Add resources for that technology
3. Resources will automatically appear in search results

### Running Tests

```bash
# Backend tests (if implemented)
cd backend
pytest

# Frontend tests (if implemented)
cd frontend
npm test
```

### Building for Production

```bash
# Frontend production build
cd frontend
npm run build

# Serve production build
npm run preview
```

## 🐛 Troubleshooting

### Backend Issues

**Port 8000 already in use:**
```bash
# Kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

**Database not found:**
```bash
# Re-run seed script
python seed_data.py
```

### Frontend Issues

**Port 5173 already in use:**
- Vite will automatically use port 5174
- Update CORS in `backend/main.py` if needed

**API connection failed:**
- Ensure backend is running on port 8000
- Check CORS settings in `backend/main.py`

## 📝 Environment Variables

Create a `.env` file in the backend directory (optional):

```env
DATABASE_URL=sqlite:///./library.db
API_HOST=0.0.0.0
API_PORT=8000
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ for students learning to code

## 🙏 Acknowledgments

- FastAPI for the amazing web framework
- React team for the powerful UI library
- All content creators whose resources are featured
- Open source community

---

**Happy Learning! 🚀**
