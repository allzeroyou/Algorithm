n = int(input())
stu_list= []

for i in range(n):
    x,y = list(map(int, input().split()))
    stu_list.append((x,y))


for i in stu_list:
    rank = 1
    for j in stu_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')