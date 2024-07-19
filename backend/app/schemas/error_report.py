from pydantic import BaseModel

class ErrorReportBase(BaseModel):
    description: str

class ErrorReportCreate(ErrorReportBase):
    section_id: int

class ErrorReportUpdate(ErrorReportBase):
    section_id: int

class ErrorReport(ErrorReportBase):
    id: int
    section_id: int

    class Config:
        from_attributes = True
