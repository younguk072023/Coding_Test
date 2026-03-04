'''
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!
'''

N = int(input())    #N개의 수업

list=[]

for i in range(N):
    S,T = map(int, input().split()) #시작과 끝 시간 입력
    list.append((S,T))
    
list.sort()
print(list)
# if N==1:
#     print(1)
# else:
#     count=1
#     end_time= list[0][1]
#     for i in range(1,N):
#         if end_time <=list[i][0]:
#             count+=1
#             end_time=list[i][1]

# print(count)
        

    
