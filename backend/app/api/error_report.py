from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from app.models.database import get_db

router = APIRouter()


@router.post("/error_reports/", response_model=schemas.ErrorReport)
def create_error_report(error_report: schemas.ErrorReportCreate, db: Session = Depends(get_db)):
    return crud.create_error_report(db=db, error_report=error_report)


@router.get("/error_reports/", response_model=List[schemas.ErrorReport])
def read_error_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    error_reports = crud.get_error_reports(db, skip=skip, limit=limit)
    return error_reports


@router.get("/error_reports/{error_report_id}", response_model=schemas.ErrorReport)
def read_error_report(error_report_id: int, db: Session = Depends(get_db)):
    error_report = crud.get_error_report(db, error_report_id=error_report_id)
    if error_report is None:
        raise HTTPException(status_code=404, detail="Error report not found")
    return error_report


@router.put("/error_reports/{error_report_id}", response_model=schemas.ErrorReport)
def update_error_report(error_report_id: int, error_report: schemas.ErrorReportUpdate, db: Session = Depends(get_db)):
    return crud.update_error_report(db=db, error_report_id=error_report_id, error_report=error_report)


@router.delete("/error_reports/{error_report_id}", response_model=schemas.ErrorReport)
def delete_error_report(error_report_id: int, db: Session = Depends(get_db)):
    return crud.delete_error_report(db=db, error_report_id=error_report_id)
