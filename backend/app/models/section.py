from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Association Table
area_section = Table(
    'area_section', Base.metadata,
    Column('area_id', Integer, ForeignKey('areas.id')),
    Column('section_id', Integer, ForeignKey('sections.id'))
)

class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    areas = relationship('Area', secondary=area_section, back_populates='sections')
    error_reports = relationship("ErrorReport", back_populates="section")
