#init : 생성자(파이썬에서만 사용)
#객체 : class로 부터 만들어지는 녀석
#이때 002에서 만든 마린/탱크는 Unit클래스의 인스턴스이다.

#init함수에 정의된 self를 제외한 함수만큼 사용해야함

#멤버 변수 : 클래스 내 정의된 변수 (외부에서도 사용 가능?)
# ex 002 = self.name = name 부분

#Unit이라는 class 생성
class Unit:
    def __init__(self, name, hp, damage):
     self.name = name
     self.hp = hp
     self.damage = damage
     print("{0} 유닛이 생성되었습니다.".format(self.name))
     print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

#class사용
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("시즈탱크", 150 , 50)

# 레이스 (클로킹)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# 다크아칸 (마인드 컨트롤)
wraith2 = Unit("레이스(마인드 컨트롤)", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태 입니다.".format(wraith2.name))
# 파이썬에서는 어떤 객체에 추가로 변수를 외부에서 만들어서 사용 가능하다.