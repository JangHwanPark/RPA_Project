#while문 무한루프
tree = 0
while True:
    tree +=1
    print("{0}개".format(tree))
#조건이 참일시 break/ 없으면 무한루프
    if tree == 30000:
        print("창고를 비워야 합니다. (현재 개수 {0}개)".format(tree))
        break