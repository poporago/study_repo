__all__ = ["Student","StudentList"]  #패키지에서 읽을 모듈지정

from .student import Student  #. 상대경로지정
from .studentlist import StudentList

a = "모듈입니다."
def b():
    print("school모듈입니다.")