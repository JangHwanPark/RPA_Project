# 모듈
# 필요한 것들끼리 부품처럼 만들어진 파일
# ex : 자동차
# 타이어가 마모/펑크시 타이어만 교체
# 범퍼가 고장나면 범퍼만 교체
# 고장난 부품만 교체

# 확장자가 .py이다

# 모듈 불러오기
# 모듈 사용시 사용하려고하는 파일과 같은 경로에있거나
# 파이썬 라이브러리들이 모여있는 폴더에 있어야 사용이 가능하다.

# import theater_moduile
# theater_moduile.price(3) # 3명에서 영화보러 갔을때 가격
# theater_moduile.price_mornig(4) # 4명에서 조조할인 영화보러 갔을때
# theater_moduile.price_soldier(5) # 5명의 군인이 영화보러 갔을때

# 모듈에 별명 삽입
# import theater_moduile as mv # as 뒤에 적는내용은 그 내용으로 대체할수 있다.
# mv.price(3)
# mv.price_mornig(4)
# mv.price_soldier(5)

# from import 사용
# from theater_moduile import * # from random inport * ==
# price(3)
# price_mornig(4)
# price_soldier(5)

# from inport 변형
# from theater_moduile import price, price_mornig
# price(5)
# price_mornig(6)
# price_solier(7) price와 price_mornig만 사용하기로했기때문에 사용 불가

# 비슷한 변형 예제
from theater_moduile import price_soldier as price
#price_soldier를 price처럼 사용
price(3)