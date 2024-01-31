'''
분수찾기

1 -> 1/1
2 -> 1/2
3 -> 2/1
4 -> 3/1
5 -> 2/2
6 -> 1/3
7 -> 1/4
8 -> 2/3
9 -> 3/2

...
14 -> 2/4

'''

x = int(input())
line = 0 # 사선 라인
max_num = 0

while x > max_num:
    line += 1
    max_num += line
gap = max_num - x

if line % 2 ==0: # 사선 라인이 짝수 번째 일때
    top = line - gap    # 분자
    under = gap + 1     # 분모
else:           # 사선 라인이 홀수번째 일때
    top = gap + 1       # 분자
    under = line-gap    # 분모
print(f'{top}/{under}')

