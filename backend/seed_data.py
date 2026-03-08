from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Technology, Resource

# Create tables
Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    # Check if data already exists
    if db.query(Technology).count() > 0:
        print("Database already seeded!")
        db.close()
        return
    
    # Add technologies
    technologies = [
        Technology(name="Python", description="High-level programming language for web, data science, and automation"),
        Technology(name="JavaScript", description="Programming language for web development and interactive websites"),
        Technology(name="React", description="JavaScript library for building user interfaces"),
        Technology(name="Java", description="Object-oriented programming language for enterprise applications"),
        Technology(name="SQL", description="Language for managing and querying relational databases"),
        Technology(name="Node.js", description="JavaScript runtime for server-side development"),
        Technology(name="TypeScript", description="Typed superset of JavaScript"),
        Technology(name="Django", description="High-level Python web framework"),
    ]
    
    db.add_all(technologies)
    db.commit()
    
    # Get Python technology
    python = db.query(Technology).filter(Technology.name == "Python").first()
    
    # Add Python resources
    python_resources = [
        Resource(technology_id=python.id, title="Python Full Course - Learn Python in 12 Hours", 
                url="https://youtube.com/watch?v=_uQrJ0TkZlc", type="video", views=2500000),
        Resource(technology_id=python.id, title="Python Tutorial for Beginners", 
                url="https://youtube.com/watch?v=rfscVS0vtbw", type="video", views=1800000),
        Resource(technology_id=python.id, title="Python Programming Tutorial", 
                url="https://youtube.com/watch?v=f79MRyMsjrQ", type="video", views=1500000),
        Resource(technology_id=python.id, title="Learn Python - Full Course for Beginners", 
                url="https://youtube.com/watch?v=rfscVS0vtbw", type="video", views=1200000),
        Resource(technology_id=python.id, title="Python Crash Course", 
                url="https://youtube.com/watch?v=JJmcL1N2KQs", type="video", views=900000),
        
        Resource(technology_id=python.id, title="Python Official Documentation", 
                url="https://docs.python.org/3/", type="reference", views=5000000),
        Resource(technology_id=python.id, title="Real Python Tutorials", 
                url="https://realpython.com/", type="notes", views=1200000),
        Resource(technology_id=python.id, title="Python Crash Course Book", 
                url="https://nostarch.com/pythoncrashcourse2e", type="reference", views=800000),
        Resource(technology_id=python.id, title="W3Schools Python Tutorial", 
                url="https://w3schools.com/python/", type="notes", views=3000000),
        Resource(technology_id=python.id, title="Python for Everybody", 
                url="https://py4e.com/", type="notes", views=600000),
        Resource(technology_id=python.id, title="Python Package Index (PyPI)", 
                url="https://pypi.org/", type="reference", views=2000000),
    ]
    
    # Get React technology
    react = db.query(Technology).filter(Technology.name == "React").first()
    
    # Add React resources
    react_resources = [
        Resource(technology_id=react.id, title="React Course - Beginner to Advanced", 
                url="https://youtube.com/watch?v=bMknfKXIFA8", type="video", views=3200000),
        Resource(technology_id=react.id, title="React JS Full Course 2023", 
                url="https://youtube.com/watch?v=CgkZ7MvWUAA", type="video", views=2100000),
        Resource(technology_id=react.id, title="React Tutorial for Beginners", 
                url="https://youtube.com/watch?v=SqcY0GlETPk", type="video", views=1900000),
        Resource(technology_id=react.id, title="React Hooks Course", 
                url="https://youtube.com/watch?v=TNhaISOUy6Q", type="video", views=1400000),
        
        Resource(technology_id=react.id, title="React Official Documentation", 
                url="https://react.dev/", type="reference", views=4500000),
        Resource(technology_id=react.id, title="React Tutorial - W3Schools", 
                url="https://w3schools.com/react/", type="notes", views=2100000),
        Resource(technology_id=react.id, title="React Handbook", 
                url="https://reacthandbook.dev/", type="notes", views=800000),
        Resource(technology_id=react.id, title="Create React App", 
                url="https://create-react-app.dev/", type="reference", views=1500000),
        Resource(technology_id=react.id, title="React Patterns", 
                url="https://reactpatterns.com/", type="notes", views=600000),
    ]
    
    # Get JavaScript technology
    javascript = db.query(Technology).filter(Technology.name == "JavaScript").first()
    
    # Add JavaScript resources
    js_resources = [
        Resource(technology_id=javascript.id, title="JavaScript Full Course", 
                url="https://youtube.com/watch?v=PkZNo7MFNFg", type="video", views=4000000),
        Resource(technology_id=javascript.id, title="JavaScript Tutorial for Beginners", 
                url="https://youtube.com/watch?v=W6NZfCO5SIk", type="video", views=2800000),
        Resource(technology_id=javascript.id, title="Modern JavaScript Tutorial", 
                url="https://youtube.com/watch?v=hdI2bqOjy3c", type="video", views=1600000),
        
        Resource(technology_id=javascript.id, title="MDN JavaScript Guide", 
                url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", type="reference", views=6000000),
        Resource(technology_id=javascript.id, title="JavaScript.info", 
                url="https://javascript.info/", type="notes", views=3500000),
        Resource(technology_id=javascript.id, title="Eloquent JavaScript Book", 
                url="https://eloquentjavascript.net/", type="notes", views=1800000),
        Resource(technology_id=javascript.id, title="JavaScript Reference - MDN", 
                url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference", type="reference", views=5000000),
    ]
    
    db.add_all(python_resources + react_resources + js_resources)
    db.commit()
    db.close()
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
