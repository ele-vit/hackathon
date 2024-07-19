from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)