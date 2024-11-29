# 공집합 s
# 아래 연산 수행
# (1<=x<=20)
# add: x 추가, x가 이미 있는 경우 연산 무시
# remove: x 제거, x가 이미 없는 경우 연산 무시
# check: x가 있으면 1, 없으면 0 출력
# toggle: x가 있으면 x 제거, 없으면 x 추가
# all: s를 {1,2,..,20}으로 바꿈
# empty: 공집합으로 바꿈.
import sys
input = sys.stdin.readline

m = int(input())
# 공집합
s = set()

for i in range(m):
    op = list(input().split())
    x = 0
    if len(op) >= 2:
        x = int(op[1])
    op = op[0]

    if op == 'add':
        s.add(x)
    elif op == 'remove':
        s.discard(x)
    elif op == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif op == 'all':
        s = {n for n in range(1, 21)}
    else:
        s = set()
