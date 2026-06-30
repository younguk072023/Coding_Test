N = int(input())
M = list(map(int,input().split()))

count =0 #모험가 수
result = 0 #그룹 수
for i in M:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)
