from sqlalchemy.orm import Session
from backend.app.models import error_report
from app import schemas


def create_error_report(db: Session, error_report_schm: schemas.ErrorReportCreate):
    db_error_report = error_report.ErrorReport(
        section_id=error_report_schm.section_id, description=error_report_schm.description)
    db.add(db_error_report)
    db.commit()
    db.refresh(db_error_report)
    return db_error_report


def get_error_report(db: Session, error_report_id: int):
    return db.query(error_report.ErrorReport).filter(error_report.ErrorReport.id == error_report_id).first()


def get_error_reports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(error_report.ErrorReport).offset(skip).limit(limit).all()


def update_error_report(db: Session, error_report_id: int, error_report_schm: schemas.ErrorReportUpdate):
    db_error_report = db.query(error_report.ErrorReport).filter(
        error_report.ErrorReport.id == error_report_id).first()
    if db_error_report:
        db_error_report.section_id = error_report_schm.section_id
        db_error_report.description = error_report_schm.description
        db.commit()
        db.refresh(db_error_report)
    return db_error_report


def delete_error_report(db: Session, error_report_id: int):
    db_error_report = db.query(error_report.ErrorReport).filter(
        error_report.ErrorReport.id == error_report_id).first()
    if db_error_report:
        db.delete(db_error_report)
        db.commit()
    return db_error_report
