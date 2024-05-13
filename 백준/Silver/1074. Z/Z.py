n, r, c = map(int, input().split())

# 정답
ans = 0

# 분할정복
while n != 0:
    # 재귀 탈출 조건
    n -= 1
    # 2사분면
    if r < 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 0
    # 1사분면
    elif r < 2 ** n and c >= 2 ** n:
        ans += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)
    # 3사분면
    elif r >= 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
    # 4사분면
    else:
        ans += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)
print(ans)