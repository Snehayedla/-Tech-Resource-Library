from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Technology(Base):
    __tablename__ = "technologies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    resources = relationship("Resource", back_populates="technology")

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(Integer, primary_key=True, index=True)
    technology_id = Column(Integer, ForeignKey("technologies.id"))
    title = Column(String)
    url = Column(String)
    type = Column(String)  # video, notes, reference
    views = Column(Integer, default=0)
    language = Column(String, default="English")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    technology = relationship("Technology", back_populates="resources")
