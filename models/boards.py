from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from models.database import Base


class Board(Base):
    __tablename__ = 'boards'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    views_amount = Column(Integer, default=0)
    
    def __init__(self, content):
        self.content = content
