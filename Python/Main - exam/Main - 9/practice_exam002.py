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