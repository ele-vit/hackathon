from pydantic import BaseModel
from typing import List

class SectionBase(BaseModel):
    name: str
    description: str

class SectionCreate(SectionBase):
    areas_responsables: List[int]

class SectionUpdate(SectionBase):
    areas_responsables: List[int]

class Section(SectionBase):
    id: int
    areas_responsables: List[int]

    class Config:
        from_attributes = True
