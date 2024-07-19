from sqlalchemy.orm import Session
from backend.app.models import section
from app import schemas


def create_section(db: Session, section_schm: schemas.SectionCreate):
    db_section = section.Section(
        name=section_schm.name, description=section_schm.description)
    db_section.areas = db.query(section.Area).filter(
        section.Area.id.in_(section_schm.areas_responsables)).all()
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


def get_section(db: Session, section_id: int):
    return db.query(section.Section).filter(section.Section.id == section_id).first()


def get_sections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(section.Section).offset(skip).limit(limit).all()


def update_section(db: Session, section_id: int, section_schm: schemas.SectionUpdate):
    db_section = db.query(section.Section).filter(
        section.Section.id == section_id).first()
    if db_section:
        db_section.name = section_schm.name
        db_section.description = section_schm.description
        db_section.areas = db.query(section.Area).filter(
            section.Area.id.in_(section_schm.areas_responsables)).all()
        db.commit()
        db.refresh(db_section)
    return db_section


def delete_section(db: Session, section_id: int):
    db_section = db.query(section.Section).filter(
        section.Section.id == section_id).first()
    if db_section:
        db.delete(db_section)
        db.commit()
    return db_section
