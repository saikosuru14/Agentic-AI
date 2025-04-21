from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Set up PostgreSQL connection string (adjust credentials as needed)
DATABASE_URL = "postgresql://postgres:Welcome@123@localhost/agent_ai_db"

# Create engine to connect to the PostgreSQL database
engine = create_engine(DATABASE_URL, echo=True)

# Create a session local class that can be used to create new session instances
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initializes the database by creating all tables defined in models.py"""
    Base.metadata.create_all(bind=engine)

# Utility function to get the current database session (useful for API requests)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
