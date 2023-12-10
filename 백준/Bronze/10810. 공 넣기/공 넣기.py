import sys
from collections import defaultdict

input = sys.stdin.readline

# n개의 바구니, m번 공 넣을 수 있음
n, m = map(int, input().split())

# 0으로 만든 배열
lst = [0 for _ in range(n)]

for _ in range(m):
    # i~j번 바구니, k번 공 넣겠음
    i, j, k = map(int, input().split())
    # 바구니에 공이 있는 경우, 들어있는 공 빼고 new 공 넣음.
    for q in range(i - 1, j):
        lst[q] = k

for p in lst:
    print(p, end=' ')
