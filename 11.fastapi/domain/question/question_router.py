from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix = "/api/question",
) # API 라우팅 핵심 객체

@router.get("/list")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all() # protected 변수 / private 변수 / public변수
    db.close()
    return _question_list