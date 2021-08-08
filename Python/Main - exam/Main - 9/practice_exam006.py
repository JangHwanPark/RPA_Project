# 다중 상속
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
     self.name = name
     self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # AttackUnit은 Unit상속 받음
    def __init__(self, name, hp, damage):
     Unit.__init__(self, name, hp)
     self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
        .format(self.name, location, self.damage))
    # location은 전달받은값 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴/사망 하였습니다.".format(self.name))

# 드랍쉽 : 공격 불가, 수송기
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [Speed {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyri = FlyableAttackUnit("발키리", 200, 6, 5)
valkyri.fly(valkyri.name, "3시")