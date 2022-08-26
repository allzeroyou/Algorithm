n = int(input().rstrip())
arr = [0]
for _ in range(n):
    arr.append(int(input().rstrip())) # 런타임에러 나서 rstrip추가

if n == 1:
    print(arr[1])
else:

    dp = [0] * (301)

    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n + 1):
        dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], dp[i - 2] + arr[i])
    print(dp[n])
