class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# __name__을 사용해서 직접 모듈내에서 실행하는건지
# 외부에서 모듈을 가져다 쓰는건지 확인할 수 있다.
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    trip_to1 = ThailandPackage()
    trip_to1.detail()
else:
    print("Thailand 외부에서 모듈 호출")