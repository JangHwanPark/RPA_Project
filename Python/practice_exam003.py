# file 생성 후 내용 추가
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 :0", file=score_file)
# print("영어 :50", file=score_file)
# score_file.close()

#기존 file에 내용 추가
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# file 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# score_file = open("score.txt", "r" , encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# file이 몇줄인지 모르는 상황
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score에 있는 내용이 모두 출력되어야함
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readline() #list형태로 저장
for line in lines:
    print(line, end="")

score_file.close()