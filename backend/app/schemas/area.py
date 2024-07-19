from pydantic import BaseModel
from typing import List

class AreaBase(BaseModel):
    name: str

class AreaCreate(AreaBase):
    pass

class AreaUpdate(AreaBase):
    pass

class Area(AreaBase):
    id: int
    workers: List[int] = []

    class Config:
        from_attributes = True
