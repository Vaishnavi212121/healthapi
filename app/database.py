from sqlalchemy import create_engine
from app.settings import settings
from sqlalchemy.orm import declarative_base, sessionmaker #creates a base class that SQLAlchemy models inherit from.


#method in sql used to conn db
engine = create_engine( #the actual connection object to the DB SQLite here
    settings.database_url, ##DATABASE_URL = "sqlite:///./healthapi.db" from setting 
    connect_args={"check_same_thread": False} #SQLite-specific
)

#SessionLocal that produces new session objects when called as
SessionLocal = sessionmaker( #sessionmaker doesn't create a session , it creates a factory
    autocommit=False,#nothing writes to the DB until you explicitly call .commit()
    autoflush=False,
    bind=engine #connects the session factory to your database engine.
)

Base = declarative_base() #creates the base class for SQLAlchemy models.

def check_database(): # checks for db
    try:
        with engine.connect(): # try opening db conn ,if work then healthy db
            return {
                "status": "healthy",
                "message": "Database connection successful"
            }

    except Exception as e:
        return {
            "status": "unhealthy",
            "message": f"Database connection failed: {str(e)}"
        }
        