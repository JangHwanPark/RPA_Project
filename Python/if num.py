#등급 입력
Rating = input("고객님의 현재 등급을 입력하세요.")
index = int(input("가격을 입력하세요."))
if Rating == "A":
    index *= 0.7
    print("고객님은 A등급입니다. {0}원 할인 받으실수 있습니다.".format(index))
elif Rating == "B":
    index *= 0.85
    print("고객님은 B등급입니다. {0}원 할인 받으실수 있습니다.".format(index))
elif Rating == "C":
    index *= 0.92
    print("고객님은 C등급입니다. {0}원 할인 받으실수 있습니다.".format(index))
elif Rating == "Z":
    index += 5000
    print("고객님은 Z등급입니다. 5000원의 배송료가 부과되어 {0}원 입니다.".format(index))
else:
    print("잘못입력하셨습니다. 다시 입력해주세요(A,B,C,Z)")