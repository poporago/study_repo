a = 10

def b():
    return 10

class C:
    pass


class Circle:
    def __init__(self, 반지름):
        if 반지름 < 0:
            raise ValueError()
        self.__PI = 3.14
        self.__반지름 = 반지름
    def 넓이(s):
        return s.__PI * s.__반지름 ** 2
    def 둘레(s):
        return 2 * s.__PI * s.__반지름
    

if __name__ == "__main__" :
    print("#넓이()를 검증합니다.")
    if Circle(10).넓이() - 314 <  1e-7 :
        print("넓이() 검증을 성공했습니다 : Success")
    else : 
        print("넓이() 검증을 실패했습니다 : Fail")
    print("# 둘레()를 검증합니다.")
    if Circle(10).둘레() - 62.8  < 1e-7 :
        print("둘레() 검증을 성공했습니다: Success")
    else :
        print("둘레() 검증을 실패했습니다: Fail")