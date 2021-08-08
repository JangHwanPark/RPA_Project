#커피자판기 (예제)

coffe = 10
money = 300
#money는 0이 아니므로 항상 참이다. == 무한루프
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffe = coffe -1
    print("남은 커피의 양은%d개 입니다."% coffe)
    if coffe == 0:
        #만약 coffe가 0이 되면 해당 문장이 참이되므로 break가 호출
        print("커피가 없습니다.")
        break
        #프로그램이 종료됨