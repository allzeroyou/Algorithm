import sys

while True:
    # 마지막에 stack에 있는 값들을 다 꺼내기 위해 마지막 h 값은 0
    h = list(map(int, sys.stdin.readline().split()))+[0]
    if h[0] == 0:
        break
    n = h[0]
    stack = [(1, h[1])]
    res = 0
    for i in range(2, n+2):
        w = i
        # stack에 있는 h 값이 더 크다면 꺼내서 (높이 * 너비) 계산
        while stack and stack[-1][1] > h[i]:
            w, hi = stack.pop()
            res = max(res, (i-w)*hi)
        stack.append((w, h[i]))
    print(res)