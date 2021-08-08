# absent = [2,5] #경석
# no_book = [7]
# for student in range(1,11): #1 ~ 10까지
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#한줄 for문
# students =[1,2,3,4,5]
# print(students)
# students= [i+100 for i in students]
# print(students)

#학생 이름을 길이로 변환
# students = ["Irom man","Thor","I am Groot"]
# students = [ len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변환
# students = ["Iron man","Thor","I am Groot"]
# students = [i.upper() for i in students]
# print(students)

#if 50명
#if 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐
#if 소요시간 5분 ~ 15분 사이의 승객만 매칭해야한다.
from random import* #난수
cnt = 0 #총 탑승 수
for i in range(1,51): #1~50이라는 수(승객)
    time = randrange(5,51) #5분~50분 소요 시간
    if 5 <= time <= 15: #현재 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1 #매칭될 경우 카운트 증가
    else: #매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))

    print("총 탑승 승객 : {0}분".format(cnt))