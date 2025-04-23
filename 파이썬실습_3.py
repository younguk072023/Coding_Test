

#1,2,3 csv와 numpy사용과 연산,boolean

import matplotlib.pyplot as plt
import numpy as np

f=open("제주도_건강통계.csv","r")
text=f.read()
f.close()

table_list=text.strip().split("\n")
data=[list.strip().split(",") for list in table_list[1:]]

all_list=[]

header=table_list[0].strip().split(",")
fat_index=header.index("비만율")


for row in data:
    value=float(row[fat_index])
    all_list.append(value)

all_list_numpy=np.array(all_list)

result=all_list_numpy>=25

print(result)
print(all_list_numpy[result])




