from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "user" #added tablename

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False, default="USER")