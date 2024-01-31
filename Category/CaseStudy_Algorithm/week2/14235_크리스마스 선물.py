import heapq as hq
import sys

input = sys.stdin.readline
max_heap = []
for _ in range(int(input())):
    a, *gifts = map(int, input().split())
    if a:
        for i in gifts:
            hq.heappush(max_heap, -i)
    else:
        print(-hq.heappop(max_heap) if max_heap else -1)