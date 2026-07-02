N= int(input())
M=list(map(int,input().split()))

M.sort()
result=1

for i in M:
    if result<i:
        break
    result+=i

print(result)
