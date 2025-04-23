# import numpy as np
# import matplotlib.pyplot as plt


# f=open("나라별_GDP.csv","r",encoding='utf-8-sig')
# text=f.read()
# f.close()

# print(text)

# gdp_list=text.strip().split("\n")
# data=[i.strip().split(',')for i in gdp_list[1:]]

# header_list=gdp_list[0].strip().split(',')
# header=header_list.index('year')

# year_list=[]

# for j in data:
#     value=int(j[header])
#     year_list.append(value)


# header1=header_list.index('korea_gdp')
# kor_list=[]

# for k in data:
#     value1=float(k[header1])
#     kor_list.append(value1)


# header2=header_list.index('japan_gdp')
# jap_list=[]

# for l in data:
#     value2=float(l[header2])
#     jap_list.append(value2)

# header3=header_list.index('china_gdp')
# chi_list=[]

# for q in data:
#     value3=float(q[header3])
#     chi_list.append(value3)

# kor_numpy_list=np.array(kor_list)
# print("한국의 GDP 최댓값:",np.max(kor_numpy_list))
# print("한국의 GDP 평균값:",np.mean(kor_numpy_list))
# print("한국의 GDP 중간값:",np.median(kor_numpy_list))
# print("한국의 GDP 최솟값:",np.min(kor_numpy_list))


# kor15000=kor_numpy_list>15000

# print(kor_numpy_list[kor15000])




# plt.plot(year_list,kor_list,color='r',linestyle='-',label='korea')
# plt.plot(year_list,jap_list,color='b',linestyle='-',label='japen')
# plt.plot(year_list,chi_list,color='g',linestyle='-',label='china')

# plt.xlabel('year')
# plt.legend()

# plt.show()

# a='##sdwodmwodowdo##'
# b=a.strip('#').capitalize()
# print(b)

import numpy as np
import math

a=[1,2,3,4,5]
b=np.array(range(5))
c=np.arange(5)
print(c)

np.random.seed(5)
d=np.random.rand(5,3)
print(d)