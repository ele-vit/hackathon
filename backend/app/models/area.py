from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Area(Base):
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    workers = relationship("Worker", back_populates="area")
    sections = relationship("Section", secondary="area_section", back_populates="areas")
