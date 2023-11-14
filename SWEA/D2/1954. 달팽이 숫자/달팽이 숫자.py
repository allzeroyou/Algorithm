t = int(input())

for tc in range(1, t + 1):
    # 달팽이 크기
    n = int(input())
    # 시계방향
    dist = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우 하 좌 상
    # n*n 행렬
    board = [[0] * n for _ in range(n)]
    num = 1  # 달팽이 채울 숫자
    d = 0  # 달팽이 이동방향
    x, y = 0, -1  # 시작 위치

    while num <= (n * n):
        nx, ny = x + dist[d][0], y + dist[d][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = num  # 숫자 넣어주기
            num += 1  # 숫자 증가
            x, y = nx, ny  # 현재 위치 갱신
        else:
            # 격자에서 벗어나거나, 해당 위치에 이미 숫자가 있는 경우
            # 방향을 변경한다.
            d = (d + 1) % 4  # 0, 1, 2, 3으로만 움직이게끔 나머지를 구한다

    print(f'#{tc}')

    for row in board:
        print(*row)
