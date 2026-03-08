from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Technology, Resource
from pydantic import BaseModel

router = APIRouter()

class ResourceCreate(BaseModel):
    technology_name: str
    title: str
    url: str
    type: str
    views: int = 0

@router.get("/resources/{technology_name}")
def get_resources(technology_name: str, db: Session = Depends(get_db)):
    technology = db.query(Technology).filter(Technology.name.ilike(f"%{technology_name}%")).first()
    
    if not technology:
        raise HTTPException(status_code=404, detail="Technology not found")
    
    resources = db.query(Resource).filter(Resource.technology_id == technology.id).all()
    
    videos = [r for r in resources if r.type == "video"]
    notes = [r for r in resources if r.type == "notes"]
    references = [r for r in resources if r.type == "reference"]
    
    videos.sort(key=lambda x: x.views, reverse=True)
    notes.sort(key=lambda x: x.views, reverse=True)
    references.sort(key=lambda x: x.views, reverse=True)
    
    return {
        "technology": {"id": technology.id, "name": technology.name, "description": technology.description},
        "videos": [{"id": r.id, "title": r.title, "url": r.url, "views": r.views} for r in videos[:10]],
        "notes": [{"id": r.id, "title": r.title, "url": r.url, "views": r.views} for r in notes[:10]],
        "references": [{"id": r.id, "title": r.title, "url": r.url, "views": r.views} for r in references[:10]]
    }

@router.post("/resources")
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    technology = db.query(Technology).filter(Technology.name == resource.technology_name).first()
    
    if not technology:
        raise HTTPException(status_code=404, detail="Technology not found")
    
    new_resource = Resource(
        technology_id=technology.id,
        title=resource.title,
        url=resource.url,
        type=resource.type,
        views=resource.views
    )
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return {"id": new_resource.id, "message": "Resource created successfully"}

@router.delete("/resources/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    db.delete(resource)
    db.commit()
    return {"message": "Resource deleted successfully"}
