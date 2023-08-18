import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    ans = 0
    leng = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for j in range(2, leng):
        ans = max(ans, arr[j] - arr[j - 2])
    print(ans)