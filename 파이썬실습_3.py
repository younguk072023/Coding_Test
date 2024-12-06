

#1,2,3 csv와 numpy사용과 연산,boolean

import matplotlib.pyplot as plt
import numpy as np

f=open("제주도_건강통계.csv","r")
text=f.read()
f.close()

table_list=text.strip().split("\n")
data=[table_data.strip().split(",") for table_data in table_list[1:]]

header=table_list[0].strip().split(",")
fat_index=header.index("비만율")

fat_list=[]

for row in data:
    row_value=float(row[fat_index])
    fat_list.append(row_value)

fat_list_numpy=np.array(fat_list)


result=fat_list_numpy>=25   #numpy 조건문은 if 생략 가능


fat_list_numpy_result=fat_list_numpy[result]


print(fat_list_numpy)
print(type(fat_list_numpy))
print(result)
print(fat_list_numpy_result)


