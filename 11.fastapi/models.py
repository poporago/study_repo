from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # 질문과 답변을 연결하기 위한 속성, ForeignKey 사용
    question = relationship("Question", backref="answers") # 답변 모델에서 질문 모델을 참조하기 위한 속성, backref : 역참조기능 ans.question <-> q.answers 둘다 가능