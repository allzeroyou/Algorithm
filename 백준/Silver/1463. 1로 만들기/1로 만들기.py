n = int(input())
# dp 테이블
d = [0] * (n+1) # 1000001  # 10^6

for i in range(2, n + 1):
    # 1을 뺀다.
    d[i] = d[i - 1] + 1
    # 3으로 나눈다.
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])