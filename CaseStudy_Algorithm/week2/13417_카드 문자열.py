from collections import deque

for i in range(int(input())):
    i = input()
    dq = deque()
    for ch in input().split():
        if dq and ch <= dq[0]:
            dq.appendleft(ch)
        else:
            dq.append(ch)

    print(''.join(map(str, list(dq))))