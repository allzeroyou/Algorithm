'''
N개의 선물 상자
선물 상자에는 현재 담겨있는 선물의 개수
선물 받을 아이들 M명(1~M까지 서로 다른 번호

0(M * logN)

우선순위 큐: max-heap
'''
from heapq import heappush, heappop

N, M = map(int, input().split())
max_heap = []

for c in map(int, input().split()):
    heappush(max_heap, -c)
ans = 1
for w in map(int, input().split()):
    gift = -heappop(max_heap)
    if w > gift:
        ans = 0
        break
    else:
        heappush(max_heap, -(gift - w))
print(ans)



