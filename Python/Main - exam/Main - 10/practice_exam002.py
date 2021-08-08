#의도적으로 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를입력하세요 : "))
    num2 = int(input("두 번째 숫자를입력하세요 : "))
    if num1 >= 10 or num2 >=10: #if문이 만족할때
        raise ValueError #에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) #에러발생시 문장처리안함
except ValueError: # 에러발생
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")