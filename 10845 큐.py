import collections
import sys

input = sys.stdin.readline

q = collections.deque()  # 큐 생성
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "push":  # push 명령
        q.append(command[1])
    elif command[0] == "front":
        if not q:  # 큐가 비었다면
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:  # 큐가 비었다면
            print(-1)
        else:
            print(q[-1])
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if not q:  # 큐가 비었다면
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        if not q:  # 큐가 비었다면
            print(-1)
        else:
            print(q.popleft())
