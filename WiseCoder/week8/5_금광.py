# test case 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())  # n: 행, m: 열
    arr = list(map(int, input().split()))
    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index: index + m]) # 한줄에 입력받기 때문에 m의 크기로 슬라이싱해서 dp에 담음
        index += m
    # dp-보텀업
    for j in range(1, m): # 각각의 열을 하나하나 확인하면서
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: # 인덱스 범위 check -> 벗어난다면 해당 범위 값을 0으로
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == 0:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left) # 얻을 수 있는 금의 최댓값 갱신
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
