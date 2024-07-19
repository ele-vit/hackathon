from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from app.models.database import get_db

router = APIRouter()


@router.post("/areas/", response_model=schemas.Area)
def create_area(area: schemas.AreaCreate, db: Session = Depends(get_db)):
    return crud.create_area(db=db, area=area)


@router.get("/areas/", response_model=List[schemas.Area])
def read_areas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    areas = crud.get_areas(db, skip=skip, limit=limit)
    return areas


@router.get("/areas/{area_id}", response_model=schemas.Area)
def read_area(area_id: int, db: Session = Depends(get_db)):
    area = crud.get_area(db, area_id=area_id)
    if area is None:
        raise HTTPException(status_code=404, detail="Area not found")
    return area


@router.put("/areas/{area_id}", response_model=schemas.Area)
def update_area(area_id: int, area: schemas.AreaUpdate, db: Session = Depends(get_db)):
    return crud.update_area(db=db, area_id=area_id, area=area)


@router.delete("/areas/{area_id}", response_model=schemas.Area)
def delete_area(area_id: int, db: Session = Depends(get_db)):
    return crud.delete_area(db=db, area_id=area_id)
