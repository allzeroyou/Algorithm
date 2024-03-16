# 2xn 직사각형을 1x2, 2x1 타일로 채우는 방법의 수
# print(1+1%3, 2+2%3, 3+3%3, 4+4%3, 5+5%3)

# 점화식
# n+n%3(n>2)
# n=n(n<2)

n = int(input())

dp = [0] * 1001
dp[0] = 1

if n == 2:
    dp[1] = 2
else:
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1] % 10007)