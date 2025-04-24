'''
첫째 줄에 숫자 카드들이 놓인 행의 개수N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주여진다(1<=M<=100)
둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000이하의 자연수이다. 
첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
'''

#방법 1
N,M=map(int,input().split())

result=0    #작은 값들 중에서 큰 값을 넣어주기 위한 변수

for i in range(N):
    data=list(map(int,input().split()))
    min_value=100000

    for j in data:
        
        min_value=min(j,min_value)

    result=max(result,min_value)

print(result)


#방법 2
n,m=map(int,input().split())

result=0

for i in range(n):
    data=list(map(int,input().split()))

    min_value=min(data)

    result=max(min_value,result)

print(result)
