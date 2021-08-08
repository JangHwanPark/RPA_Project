#Class 

#마린 : 공격유닛, 군인. 총을 쏠수 있음
name = "마린" #이름
hp = 40 #체력
damage = 5 #공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

#탱크 : 공격유닛, 탱크. 포를 쓸수있다. 일반 모드 / 시즈 모드
tank_name = "시즈 탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
