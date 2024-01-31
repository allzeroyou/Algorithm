board = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 6
ans = 25


def is_possible(y, x, sz):
    if paper[sz] == 5:
        return False

    if y + sz > 10 or x + sz > 10: # 범위체크(10 넘어갈 경우 false)
        return False
    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False

    return True


def mark(y, x, sz, k):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = k
    if k == 1:
        paper[sz] -= 1
    else:
        paper[sz] += 1


def backtracking(y, x):
    global ans

    if y == 10:
        ans = min(ans, sum(paper))
        return
    if x == 10:
        backtracking(y + 1, 0)
        return

    if board[y][x] == 0:
        backtracking(y, x + 1)
        return
    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x + 1)
            mark(y, x, sz, 1)


backtracking(0, 0)
print(-1 if ans == 25 else ans)
