from sqlalchemy.orm import Session
from backend.app.models import worker
from app import schemas


def create_worker(db: Session, section_schm: schemas.WorkerCreate):
    db_worker = worker.Worker(name=section_schm.name)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def get_worker(db: Session, worker_id: int):
    return db.query(worker.Worker).filter(worker.Worker.id == worker_id).first()


def get_workers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(worker.Worker).offset(skip).limit(limit).all()


def update_worker(db: Session, worker_id: int, section_schm: schemas.WorkerUpdate):
    db_worker = db.query(worker.Worker).filter(
        worker.Worker.id == worker_id).first()
    if db_worker:
        db_worker.name = section_schm.name
        db.commit()
        db.refresh(db_worker)
    return db_worker


def delete_worker(db: Session, worker_id: int):
    db_worker = db.query(worker.Worker).filter(
        worker.Worker.id == worker_id).first()
    if db_worker:
        db.delete(db_worker)
        db.commit()
    return db_worker
