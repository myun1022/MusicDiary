from datetime import date

from pydantic import BaseModel

class DiaryInput(BaseModel):
    title: str
    content: str

class DiaryResponse(BaseModel):
     id: int
     title: str
     content: str
     createdAt: date