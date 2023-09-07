# 문자열 x, y 입력
x = list(input())
y = list(input())

# 길이만큼 반복할 것이기 때문에
x_len = len(x)
y_len = len(y)

# 2차원 배열 dp 테이블 생성
dp = [[0] * (y_len + 1) for _ in range(x_len + 1)]  # 1-based

for i in range(1, x_len + 1):
    for j in range(1, y_len + 1):
        # 1. 문자열 X의 i번째 문자와 문자열 Y의 j번째 문자가 서로 같은 경우
        if x[i - 1] == y[j - 1]:  # LCS가 맞음
            dp[i][j] = dp[i - 1][j - 1] + 1  # X[i], Y[j]를 포함하기 전의 LCS에 1을 더한 값과 같음
        else:  # 문자열 X의 i번째 문자와 문자열 Y의 j번째 문자가 서로 다른 경우
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # LCS가 아님
print(dp[x_len][y_len])
