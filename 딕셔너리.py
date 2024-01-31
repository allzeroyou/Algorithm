import sys

input = sys.stdin.readline
n = int(input())

dic = {}

for _ in range(n):
    x, y = map(int, input().split())

    if y in dic:
        dic[y].append(x)  # 1, 2
    else:
        dic[y] = [x]

key_list = list(dic.keys())

key_list.sort()

for key in key_list:
    ans = dic[key]
    ans.sort()
    for a in ans:
        print(f"{a} {key}")
