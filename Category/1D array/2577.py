a = int(input())
b = int(input())
c = int(input())

num = a*b*c
num_arr= list(map(int, str(num)))

for i in range(10):
    cnt= 0
    for j in num_arr:
        if i == int(j):
            cnt += 1
    print(cnt)
