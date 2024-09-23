from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI() # 모든 동작이 실행되는 핵심 객체

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello") # /hello 라는 URL요청이 발생하면 해당 함수를 실행하여 결과를 리턴하라
# def hello():
#     return {"message" : "안녕하세요 파이보"} # FastAPI에서는 딕셔너리를 자동으로 JSON으로 리턴한다.


app.include_router(question_router.router)


### RUN USAGE ####
# unvicorn main:app --reload   # reload option: 프로그램이 변경되면 서버 재시작 없이 그 내용을 반영하라