#while문 처음으로 돌아가기

a = 0
while a < 10:
    a = a+1
    if a % 2 ==  0: continue
    #a가 짝수일때 continue실행됨 = 홀수만 출력
    #짝수만 출력시 a % 2 != 0 <- 짝수 식
    print("{0}".format(a))