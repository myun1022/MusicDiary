from datetime import date
from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends

from .models import Diary
from sqlalchemy.orm import Session
from .schemas import DiaryInput, DiaryResponse

router = APIRouter(prefix="/api")

@router.post("/diary")
def create_diary(diary: DiaryInput, db: Session = Depends(get_db)):
    new_diary = Diary(
        title=diary.title,
        content=diary.content,
        createdAt=date.today()
    )

    #music 가지고 오고 저장하는 코드

    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)
    return new_diary

@router.get("/diary", response_model=List[DiaryResponse])
def read_diaries(db: Session = Depends(get_db)):
    diaries = db.query(Diary).all()
    return diaries

@router.get("/api/diary/{id}")
def read_diary(id: int, db: Session = Depends(get_db)):
    diary = db.query(Diary).filter(Diary.id == id).first()
    if diary is None:
        raise HTTPException(status_code=404, detail="Diary not found")
    return diary