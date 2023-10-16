from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base

class Agenda(Base):
    __tablename__ = "agenda"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phone = Column(String(255),unique=True)
    email = Column(String(255),unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
