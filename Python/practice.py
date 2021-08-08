# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(5): #range사용하면 순차적으로 커진다.
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분 되었습니다.")

#무한루프
# customer = "아이언맨"
# index =1
# while True:
#     print("{0}, 커피가 준비되었습니다.".format(customer, index))
#     index +=1

customer = "토르"
person = "Unkown"

while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")