from sqlalchemy.orm import Session
from backend.app.models import area
from app import schemas


def create_area(db: Session, area_schm: schemas.AreaCreate):
    db_area = area.Area(name=area_schm.name)
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def get_area(db: Session, area_id: int):
    return db.query(area.Area).filter(area.Area.id == area_id).first()


def get_areas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(area.Area).offset(skip).limit(limit).all()


def update_area(db: Session, area_id: int, area_schm: schemas.AreaUpdate):
    db_area = db.query(area.Area).filter(area.Area.id == area_id).first()
    if db_area:
        db_area.name = area_schm.name
        db.commit()
        db.refresh(db_area)
    return db_area


def delete_area(db: Session, area_id: int):
    db_area = db.query(area.Area).filter(area.Area.id == area_id).first()
    if db_area:
        db.delete(db_area)
        db.commit()
    return db_area
