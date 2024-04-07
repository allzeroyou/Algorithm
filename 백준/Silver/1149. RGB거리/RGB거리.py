# rgb 거리: 집이 n개 있음
# 거리는 선분으로 나타낼 수 있고, 1번집부터 n번집이 순서대로
# 집: rgb 중 하나의 색으로 칠해야 함
# rgb로 칠하는 비용이 주어졌을때 모든 집을 칠하는 비용의 최솟값?

# 1번집의 색 != 2번집 색
# n번 집의 색은 n-1집의 색과 일치 x
# i번째 집의 색은 i-1, i+1 번의 집의 색과 같지 않아야 함.

# 집의 개수
n = int(input())

# r,g,b로 칠하는 비용
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # 현재 열을 제외한 i-1행의 열들 가운데 최솟값 + 현재 칸 비용
    # r
    dp[i][0] = dp[i][0] + min(dp[i - 1][1], dp[i - 1][2])

    # g
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])

    # b
    dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
