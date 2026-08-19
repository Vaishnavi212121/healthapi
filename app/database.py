from sqlalchemy import create_engine
from app.settings import settings
from sqlalchemy.orm import declarative_base, sessionmaker

#DATABASE_URL = "sqlite:///./healthapi.db"

engine = create_engine(
    #DATABASE_URL,
    settings.database_url,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def check_database():
    try:
        with engine.connect():
            return {
                "status": "healthy",
                "message": "Database connection successful"
            }

    except Exception as e:
        return {
            "status": "unhealthy",
            "message": f"Database connection failed: {str(e)}"
        }