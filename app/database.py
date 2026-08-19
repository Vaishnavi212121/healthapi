from sqlalchemy import create_engine
from app.settings import settings

#DATABASE_URL = "sqlite:///./healthapi.db"

engine = create_engine(
    #DATABASE_URL,
    settings.database_url,
    connect_args={"check_same_thread": False}
)


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