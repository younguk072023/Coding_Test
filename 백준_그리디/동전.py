'''
동전 0 
가치에 맞게 큰 금액부터 채운다는 느낌으로 코드 작성
'''

N,K= map(int,input().split())   #개수와 동전의 가치

a=[]
count=0 #개수 변수

for i in range(1,N+1):  #입력 값 예시 출력 코드
    a.append(int(input()))

for i in range(N-1,-1,-1):
    count+=K//a[i]
    K%=a[i]


    
print(count)



