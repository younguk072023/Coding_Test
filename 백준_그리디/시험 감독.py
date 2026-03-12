N = int(input()) #시험장의 개수

A = [] #시험자의 응시자 수
for i in range(N):
    A.append(int(input()))

B,C = map(int,input().split())


count = 0
for i in range(N):
    if A[i] > B:
        count+=1
        A[i] -= B
        if A[i] <= C:
            count+=1
        else:
            count+=A[i]//C
            if A[i]%C != 0:
                count+=1
    else:
        count+=1

print(count)            