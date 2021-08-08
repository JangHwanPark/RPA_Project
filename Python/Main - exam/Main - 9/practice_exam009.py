#super
#pass
#연산자 오버로딩
# 부모클래스에서 정의한 메소드 외 자식클래스에서 정의한 메소드를 사용하고싶을때
# 메소드를 새롭게 정의해서 사용할수있는데 이를 오버로딩이라 한다.

# 다중 상속
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
     self.name = name
     self.hp = hp
     self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}방향으로 이동합니다. [speed {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # AttackUnit은 Unit상속 받음
    def __init__(self, name, hp, speed, damage):
     Unit.__init__(self, name, hp, speed)
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
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class  buildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) #super는 ()를 붙여아하고 self는 사용하지 않는다.
        self.location = location
