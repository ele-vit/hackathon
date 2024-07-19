from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from app.models.database import get_db

router = APIRouter()

@router.post("/sections/", response_model=schemas.Section)
def create_section(section: schemas.SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db=db, section=section)

@router.get("/sections/", response_model=List[schemas.Section])
def read_sections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, skip=skip, limit=limit)
    return sections

@router.get("/sections/{section_id}", response_model=schemas.Section)
def read_section(section_id: int, db: Session = Depends(get_db)):
    section = crud.get_section(db, section_id=section_id)
    if section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return section

@router.put("/sections/{section_id}", response_model=schemas.Section)
def update_section(section_id: int, section: schemas.SectionUpdate, db: Session = Depends(get_db)):
    return crud.update_section(db=db, section_id=section_id, section=section)

@router.delete("/sections/{section_id}", response_model=schemas.Section)
def delete_section(section_id: int, db: Session = Depends(get_db)):
    return crud.delete_section(db=db, section_id=section_id)
