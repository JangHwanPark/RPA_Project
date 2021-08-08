#사용자에게 입력 받기
dinner = input("오늘 저녁메뉴는 무엇을 먹을까요? ")
if dinner == "고민중이에요": #입력값
    #입력값 true시 아래 print값 출력 : 새로운 질문
    menu = input("어떤음식이 먹고싶어요? (한식, 중식, 일식, 양식")
    #조건시작1
    if menu == "한식":
        print("비빔밥 어때요?")
    #조건2
    elif menu == "중식":
       print("마라탕 어때요?")
    #조건3
    elif menu == "일식":
       print("초밥은 어때요?")
    #외 ... (조건4)
    elif menu == "양식":
        print("아웃백은 어때요?")
    else:
        print("이런! 입맛이 까다롭군요")
        print("배민이나 키세요 ㅡㅡ")
else:
    print("이미 먹고싶은메뉴가 있거나 밥생각이없나보네요")
