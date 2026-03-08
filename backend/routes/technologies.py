from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Technology

router = APIRouter()

@router.get("/technologies")
def get_technologies(db: Session = Depends(get_db)):
    technologies = db.query(Technology).all()
    return [{"id": t.id, "name": t.name, "description": t.description} for t in technologies]
