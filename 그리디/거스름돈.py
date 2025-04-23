'''
당신은 음식점의 계산을 도와주는 점원이다. 키운터에는 거스름돈으로 사용할 500원, 100원,50원,10원짜리
동전이 무수히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일때 거슬러줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

'''
#내 첫번째 답
coin1,coin2,coin3,coin4=500,100,50,10

print("거스름 금액을 입력하세요")
N=int(input())

sum=0 #동전의 총 합계

change1=N//coin1
change2=(N%coin1)//coin2
change3=(N%coin1%coin2)//coin3
change4=(N%coin1%coin2%coin3)//coin4

sum=change1+change2+change3+change4

print(sum)

# 해설 답, 코드 간결

n=1260
count=0

coin_types=[500,100,50,10]

for i in coin_types:
    count+=n//i
    n%=i

print(count)



