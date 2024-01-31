dp = [-1] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1


def is_sk_win(n):
    if dp[n] == -1:
        dp[n] = 0 if is_sk_win(n - 1) and is_sk_win(n - 3) and is_sk_win(n - 4) else 1
        # 참이면 dp[n]=0, 거짓이면 1 대입
    return dp[n]


print('SK' if is_sk_win(int(input())) else 'CY')
