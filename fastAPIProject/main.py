from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel
import os

# FastAPI 앱 생성
app = FastAPI()

# MySQL 연결 문자열
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:12345678@localhost:3306/MusicDiary"




# SQLAlchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 선언
Base = declarative_base()

# 테스트용 라우트
@app.get("/")
async def test_db_connection():
    try:
        # 데이터베이스 연결 테스트를 위해 세션을 열고 닫습니다.
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"message": "Database connection successful"}
    except Exception as e:
        return {"message": f"Database connection failed: {str(e)}"}

# 사용자 모델
class User(BaseModel):
    id: int
    username: str
    email: str

# 사용자 생성 라우트
@app.post("/users/")
async def create_user(user: User):
    db = SessionLocal()
    db.execute(
        text("INSERT INTO users (id, username, email) VALUES (:id, :username, :email)"),
        {"id": user.id, "username": user.username, "email": user.email}
    )
    db.commit()
    return {"message": "User created successfully"}
