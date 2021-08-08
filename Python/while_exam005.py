#자동판매기 (예제)

coffee = 10
while True:
    money = int(input("돈을 넣어주세요:"))
    if money == 300:
        print("커피를 드리겠습니다.")
        coffee = coffee -1
        print("남은 커피의 양은 %d잔 입니다." % coffee)
    elif money > 300:
        coffee = coffee -1
        print("거스름돈은 %d입니다. 커피를 드리겠습니다." % (money -300))
        print("남은 커피의 양은 %d잔 입니다." % coffee)
    else:
        print("금액이 부족합니다. 잔액 환불")
        print("남은 커피의 양은 %d잔 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 소진되었습니다. 판매중지")
        break