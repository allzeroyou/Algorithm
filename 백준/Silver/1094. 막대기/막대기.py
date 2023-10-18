N = int(input())
ans = 0
while N > 0:
    if N % 2 == 1: # 이진수
        ans += 1
    N = N//2
print(ans)