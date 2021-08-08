# 패키지 : 모듈들을 모아놓은 집합
# 하나의 디렉터리에 여러 모듈 파일을 모아논것

#패키지 사용
# import travel.thailand #class나 패키지는 바로 임포트할 수 없음
# trip_to =travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to1 = vietnam.VietnamPackage()
# trip_to1.detil()

# from random import *
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to1 = thailand.ThailandPackage()
# trip_to.detail()
# trip_to1.detail()

# random의 모듈이 어디위치에있는지 파일 정보를 알려준다.
import inspect
import random
from travel import *
trip_to1 = thailand.ThailandPackage()
trip_to1.detail()

print(inspect.getfile(random))
print(inspect.getfile(thailand))
# 해당경로 (현재 Mac기준 Python3.9)에 넣을경우 다른 프로젝트를 하더라도 똑같이 사용 가능하다.