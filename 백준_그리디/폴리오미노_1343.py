'''
백준 폴리오미노 1343번 문제
'''

a=str(input())

part=a.split('.')

result=[]

for i in part:

    temp=''

    if len(i)%2!=0:
        print(-1)
        exit()
    
    while len(i)>=4:
        temp+="AAAA"
        i=i[4:]
    while len(i)>=2:
        temp+="BB"
        i=i[2:]
    result.append(temp)

print('.'.join(result))


# join함수 문법
'''
리스트에 있는 문자열들을 .을 사이에 넣어 이어붙이는 역할을 함 
ex) reuslt=["BB","AAAA","AAAABB"]
-> BB.AAAA.AAAABB
이 문법을 모르면 이문제는 풀기 힘들다.
'''