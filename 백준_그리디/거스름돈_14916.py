# coin=int(input())   #거스름돈

# change1,change2=5,2 #동전 5원짜리와 2원짜리로만 구성

# count=0
# while True:
#     if coin%change1==0:    #5원으로만 나누어지는 경우의 수
#         A=coin//change1
#         count+=A
#         print(count) 
#         break

#     elif coin%change1%change2==0: #5원과 2원으로 같이 나누어지는 경우
#         B=coin//change1
#         count+=B
#         C=coin%change1//change2
#         count+=C
#         print(count) 
#         break

#     elif coin%change1!=0 and coin%change1%change2!=0:
#         if (coin-change2)%change1==0:
#             D=(coin-change2)//change1
#             E=(((coin-change2)%change1)+change2)//change2
#             count+=E
#             count+=D
#             print(count) 
#             break
#         elif (coin-change1)%change2==0:
#             F=(coin-change1)//change1
#             count+=F
#             G=(((coin-change1)%change1)+change1)//change2
#             count+=G
#             print(count) 
#             break
#         elif (coin-change2)%change1!=0 and (coin-change1)%change2!=0:
            
#             if coin%change2==0:
#                 H=coin//change2
#                 count+=H
#                 print(count)
#                 break
#             elif coin%change2!=0:
#                 print('-1')
#                 break
'''
백준 14916번
위에 식으로 풀었을 경우 경우의 수가 너무 많아져 -1 출력이 안됨
밑에 처럼 간단하게 뺴는걸 먼저 한다고 생각해보면 편함 
'''
coin=int(input())

count=0

while coin>=0:
    if coin%5==0:
        count+=coin//5
        print(count)
        break
    coin-=2
    count+=1

else:
    print(-1)






   

   


