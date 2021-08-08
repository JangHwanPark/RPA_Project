#n번 출력후 종료되는 프로그램
#n = 입력 받은 수

bitcoin = int(input("구매할 수량을 입력하세요:"))

while bitcoin < 20:
    bitcoin = bitcoin +1
    print("매도주문이 접수되었습니다. 보유수량{0}".format(bitcoin))
    if bitcoin == 20:
        print("금액이 부족합니다. 보유코인%dcoin" % bitcoin)