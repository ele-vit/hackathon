from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from app.models.database import get_db

router = APIRouter()


@router.post("/workers/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db=db, worker=worker)


@router.get("/workers/", response_model=List[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    workers = crud.get_workers(db, skip=skip, limit=limit)
    return workers


@router.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker(worker_id: int, db: Session = Depends(get_db)):
    worker = crud.get_worker(db, worker_id=worker_id)
    if worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker


@router.put("/workers/{worker_id}", response_model=schemas.Worker)
def update_worker(worker_id: int, worker: schemas.WorkerUpdate, db: Session = Depends(get_db)):
    return crud.update_worker(db=db, worker_id=worker_id, worker=worker)


@router.delete("/workers/{worker_id}", response_model=schemas.Worker)
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    return crud.delete_worker(db=db, worker_id=worker_id)
