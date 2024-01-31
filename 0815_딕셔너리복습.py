import sys

input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    x, y = map(int, input().split())

    if y in dic:
        dic[y].append(x)
    else:
        dic[y]=[x]
# print(dic)
# y좌표 오름차순 정렬
key_list = list(dic.keys())
key_list.sort()

# y좌표가 같다면 x좌표 오름차순 정렬
for k in key_list:
    ans = dic[k]
    ans.sort()

    for a in ans:
        print(f"{a} {k}")






