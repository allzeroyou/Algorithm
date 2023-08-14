import sys

# 빠른 입력
input = sys.stdin.readline

n = int(input())

board=[]
for _ in range(n):
	x, y = map(int, input().split())
	board.append([x,y])
 
sorted_board = sorted(board, key=lambda s: (s[1], s[0]))
                      
for s in sorted_board:
	print(s[0], s[1])