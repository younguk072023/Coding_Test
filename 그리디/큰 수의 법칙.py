'''
입력조건:
첫째 줄에N(2<=N<=1000),M(1<=M<=10000),K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다.
입력으로 주어지는 K는 항상M보다 작거나 같다.

출력 조건:
첫째 줄에 영욱이의 큰 수의 법칙에 따라 더해진 답을 출력한다. 


입력 예시
5 8 3
2 4 5 4 6

출력 예시
46
'''

#답 예시 1

N,M,K=map(int,input().split())
array=list(map(int,input().split()))

array.sort()
first=array[N-1]
second=array[N-2]

sum=0

while True:
    for i in range(K):
        if M==0:
            break
        sum+=first
        M-=1
    if M==0:
        break
    sum+=second
    M-=1

print(sum)

#답 예시 2
'''
위는 반복되는 값이 적어서 시간 초과가 일어나지 않음. 하지만 많아질 경우 시간 초과가 발생할 가능성이 큼
반복되는 수열에 대해서 먼저 파악하는 것이 중요함.
'''

n,m,k=map(int,input().split())
array1=list(map(int,input().split()))

array1.sort()

first1=array1[n-1]
second1=array[n-2]

#수학적 수열에 대한 생각을 해봄
count=0
count+=(m//(k+1))*k    #k의 가장큰 개수를 구하기 위한 알고리즘
count+=m%(k+1)      #나머지도 가장큰값이므로 더해주어 전체 개수를 구함

sum=0

first_result=count*first1   #가장 큰 값 모두 계산
second_result=(m-count)*second1 #두 번째 역시 마찬가지지

sum=first_result+second_result

print(sum)

