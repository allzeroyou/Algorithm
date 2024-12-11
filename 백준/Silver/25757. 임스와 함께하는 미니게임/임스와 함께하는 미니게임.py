import sys

# input = sys.stdin.readline
# n,game= input().split()

n, game = sys.stdin.readline().strip().split() # 시초 -> 빠른 입출력으로 변경
n = int(n)
type = {'Y': 1, 'F': 2, 'O': 3}  # 각 게임당 필요한 인원수 - 1(임스)

ids = set()
for _ in range(n):
    ids.add(str(sys.stdin.readline().strip()))

print(len(ids)//type[game])