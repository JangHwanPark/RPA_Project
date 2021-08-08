#finally
from typing import final


class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를입력하세요 : "))
    num2 = int(input("두 번째 숫자를입력하세요 : "))
    if num1 >= 10 or num2 >=10: #if문이 만족할때
        raise BigNumberError("출력하기 원하는 메세지 입력 / 입력값 {0} , {1}".format(num1, num2))
         #에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) #에러발생시 문장처리안함
except ValueError: # 에러발생
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
# 프로그램의 작동여부 상관없이 출력
finally:
    print("계산기를 이용해주셔서 감사합니다.")