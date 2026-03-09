'''
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!
'''

import sys
import heapq


input = sys.stdin.readline 

n = int(input())

lectures = []
for _ in range(n):
    start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()

rooms = []

if not lectures:
    print(0)
    exit()

heapq.heappush(rooms, lectures[0][1])

for i in range(1, n):
    current_start, current_end = lectures[i]
    
    # 가장 빨리 끝나는 강의실을 재사용할 수 있는 경우
    if current_start >= rooms[0]:
        # heappop과 heappush를 heapreplace로 최적화
        # 기존 원소를 pop하고 새로운 원소를 push하는 작업을 한 번에 수행
        heapq.heapreplace(rooms, current_end)
    else:
        # 재사용 불가, 새로운 강의실 필요
        heapq.heappush(rooms, current_end)

print(len(rooms))