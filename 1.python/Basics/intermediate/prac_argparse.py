# CLI 환경에서 모델의 데이터, 환경 등 여러 옵션과 파라미터를 설정하기 위한 argparse 모듈
# 입력된 스크립트에서 어떻게 argument를 파싱할지 정의할 수 있다.

import argparse

parser = argparse.ArgumentParser(description="just test") # 인자값을 받을 수 있는 인스턴스를 생성합니다. # 스크립트에 -h 옵션을 주어 실행하였을 때 노출

#인자 값 등록
parser.add_argument("-d", "--decimal", dest="decimal", action="store")  #dest : 객체에 추가될 attribute의 이름
parser.add_argument("-f", "--fast", dest="fast", action="store_true")

# 입력받은 인자 값을 args에 저장합니다.
args = parser.parse_args() 

print(args.decimal)
print(args.fast)

#python python/run.py -d 1 - f