from heapq import heappush, heappop

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
card = []
for _ in range(n):
    heappush(card, int(input()))
if n == 1:  # 카드가 하나라면 비교 x
    print(0)
else:
    two_set = 0
    while len(card) > 1:
        min_first = heappop(card)
        min_sec = heappop(card)
        two_set += min_first + min_sec
        heappush(card, min_first + min_sec)
    print(two_set)