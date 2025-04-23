# #1


# system={}


# while True:
#     num=int(input("(1)추가(2)조회(3)삭제(4)수정(5)종료: "))

#     if num==1:
#         name,count=input("물품명과 개수를 입력하세요: ").split()
#         count=int(count)
#         system[name]=count
#         print(system)
    
#     elif num==2:
#         name=input("물품명을 입력하세요: ")
#         if name in system:
#             print(f"{name}의 재고: {system[name]}")

#     elif num==3:
#         name=input("물품명을 입력하세요: ")
#         if name in system:
#             del system[name]
#             print(system)
    
#     elif num==4:
#         name,count=input("물품명과 수정할 개수를 입력하세요: ").split()
#         count=int(count)

#         if name in system:
#             system[name]=count
#             print(system)
#         else:
#             print(f"{name}이/가 없습니다")

#     elif num==5:
#         print("출력없음, 프로그램 종료")
#         break

#     else:
#         print("1~5의 숫자를 입력하세요.")

    
# import numpy as np

# f=open('제주도_건강통계.csv',"r")
# text=f.read()
# f.close()

# health_list=text.strip().split("\n")
# data=[data_list.strip().split(",") for data_list in health_list[1:]]

# header=health_list[0].strip().split(",")
# header_index=header.index("비만율")

# fat_index=[]

# for row in data:
#     value=float(row[header_index])
#     fat_index.append(value)

# print(fat_index)

# fat_index_numpy=np.array(fat_index)

# print(np.mean(fat_index_numpy))   #1



# stress_index=[]

# header2_index=header.index("스트레스")

# for row2 in data:
#     value=float(row2[header2_index])
#     stress_index.append(value)

# stress_index_numpy=np.array(stress_index)

# stress28=stress_index_numpy>=28
# print(stress28)

# print(stress_index_numpy[stress28]) #2


# 고혈압=header.index("고혈압 진단")
# 당뇨병=header.index("당뇨병 진단")

# 고혈압리스트=[]
# 당뇨병리스트=[]

# for row3 in data:
#     value3=float(row3[고혈압])
#     고혈압리스트.append(value3)

# for ro4 in data:
#     value4=float(ro4[당뇨병])
#     당뇨병리스트.append(value4)


# 당뇨병리스트넘파이=np.array(고혈압리스트)
# 고혈압리스트넘파이=np.array(당뇨병리스트)

# 상관관계=np.corrcoef(고혈압리스트넘파이,당뇨병리스트넘파이)
# print(상관관계)








import numpy as np
import matplotlib.pyplot as plt

# 파일 읽기
f = open("나라별_GDP.csv", "r", encoding='UTF-8-sig')
text = f.read()
f.close()

list = text.strip().split("\n")
data = [i.strip().split(",") for i in list[1:]]
list_index = list[0].strip().split(",")

# 열 인덱스 추출
header = list_index.index('year')
header2 = list_index.index("korea_gdp")
header3 = list_index.index("japan_gdp")
header4 = list_index.index("china_gdp")

# 데이터 초기화
year_list = []
kor_list = []
jap_list = []
chi_list = []

# 기존 데이터 추출
for i in data:
    year_list.append(int(i[header]))
    kor_list.append(float(i[header2]))
    jap_list.append(float(i[header3]))
    chi_list.append(float(i[header4]))

# 1960~1999년 데이터 추가 (값은 0으로 초기화)
for year in range(1960, 2000):
    if year not in year_list:
        year_list.insert(0, year)
        kor_list.insert(0, 0)
        jap_list.insert(0, 0)
        chi_list.insert(0, 0)

# NumPy 배열로 변환
kor_list_numpy = np.array(kor_list)

# 한국 GDP 통계 출력
print("한국의 GDP 최대값:", np.max(kor_list))
print("한국의 GDP 평균값:", np.mean(kor_list))
print("한국의 GDP 중간값:", np.median(kor_list))
print("한국의 GDP 최소값:", np.min(kor_list))

# 한국 GDP가 15000 이상인 데이터 필터링
result = kor_list_numpy > 15000
print("15000 이상인 한국 GDP:", kor_list_numpy[result])

# 그래프 그리기
plt.plot(year_list, kor_list, color='r', linestyle='-', label="korea")
plt.plot(year_list, jap_list, color='g', linestyle='-', label="japan")
plt.plot(year_list, chi_list, color='b', linestyle='-', label="china")

# 그래프 설정
plt.legend()
plt.xlabel("year")
plt.ylabel("GDP")
plt.title("GDP Comparison by Country")
plt.grid(True)
plt.show()











    