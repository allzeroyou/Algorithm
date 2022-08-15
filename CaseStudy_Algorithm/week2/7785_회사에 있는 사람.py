n = int(input())

dic = {}

for i in range(n):
    name, in_out = input().split()
    if in_out == 'enter':
        dic[name] = 1
    else:
        del dic[name]

sorted_dic = sorted(dic, reverse=True)

for k in sorted_dic:
    print(k)

