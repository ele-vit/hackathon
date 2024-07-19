from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class ErrorReport(Base):
    __tablename__ = 'error_reports'
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'))
    description = Column(String, index=True)

    section = relationship("Section", back_populates="error_reports")
