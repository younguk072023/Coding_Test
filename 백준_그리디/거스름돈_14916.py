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






   

   


