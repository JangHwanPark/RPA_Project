tree = 0 #변수 선언
while tree < 10:
    #조건 : tree는 10보다 작음
    tree = tree +1
    #수행할 문장 : tree를 1씩 더한다.
    print("나무가 %d개 있습니다." % tree)

    #while문 종료 if문 시작
    if tree == 10:
        print("나무가 넘쳐납니다. (현재 %d개)" %tree)