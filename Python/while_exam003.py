#조건에 해당하는 선택지를 입력할때까지 무한루프
prompt = """
1.Add
2.Del
3.List
4.Quit

Enter number: """
number = 0
while number !=4:
    print(prompt)
    number = int(input())
    if number == 4:
        print("프로그램을 종료합니다.")
