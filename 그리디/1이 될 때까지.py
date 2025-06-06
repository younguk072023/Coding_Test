'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단 두 번째 연산은 N이 k로 나누어떨어질 때만 선택할 수 있다.

첫째 줄에 N(2<=N<=100,000)과 K(2<=k<=100,000)가 공백으로 구분되며 각자 자연수로 주어진다. 
이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행하는 횟수의 최솟값을 출력한다.
'''

N,K=map(int,input().split())

count=0

while N>=K:
    while N%K!=0:
        N-=1
        count+=1
    N//=K
    count+=1

while N>1:
    N-=1
    count+=1

print(count)

#방법 2

n,k= map(int,input().split())
result =0

while True:
    target = (n//k)*k
    result+=(n-target)
    n=target
    
    if n<k:
        break
    result+=1
    n//=K

result+=(n-1)   #마지막으로 남은 수에 대하여 1씩 빼기 위한 n-1을 더해줘야함함
print(result)
    



    

