import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"  # 데이터베이스 접속 주소, SQLite 사용, postgresql도 사용 가능

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}
) 

# add메서드, commit 메서드 # rollback메서드
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 데이터베이스에 접속하기 위해 필요한 클래스 , autocommit=False commit을 해야 실제로 DB에 반영

Base = declarative_base() # 데이터베이스 모델 

@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally : 
        db.close()