from pydantic import BaseModel

class WorkerBase(BaseModel):
    name: str

class WorkerCreate(WorkerBase):
    pass

class WorkerUpdate(BaseModel):
    name: str

class Worker(WorkerBase):
    id: int

    class Config:
        from_attributes = True

# Similar schemas for Area, Section, and ErrorReport
