from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import technologies, resources

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tech Resource Library API",
    description="API for managing and retrieving technology learning resources including videos, notes, and references",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://localhost:5174", 
        "http://localhost:3000",
        "https://*.vercel.app",  # Allow all Vercel preview deployments
        "*"  # Allow all origins for production (adjust as needed)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(technologies.router, tags=["Technologies"])
app.include_router(resources.router, tags=["Resources"])

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Tech Resource Library API",
        "docs": "/docs",
        "redoc": "/redoc"
    }
