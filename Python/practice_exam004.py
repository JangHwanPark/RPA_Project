#pickle
#프로그램상에서 사용중인데이터를 file형태로 저장하는것

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# profile에 있는 정보를 file에 저장
# pickle.dump(profile, profile_file) 
# profile_file.close()

#데이터 가져오기
import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()