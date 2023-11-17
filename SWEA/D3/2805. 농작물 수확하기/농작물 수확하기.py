t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    start = end = n // 2

    ans = 0
    for i in range(n):
        # start~end 까지
        for j in range(start, end + 1):
            ans += board[i][j]

        if i < n // 2:  # 중간값보다 작을 경우
            start -= 1  # start 1감소
            end += 1  # end 1증가
        else:
            start += 1
            end -= 1
    print(f'#{tc} {ans}')
