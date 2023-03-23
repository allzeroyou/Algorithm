a, b = map(int, input().strip().split(' '))

sum_star = ''
for i in range(b):  # 3
    for j in range(1, a + 1):  # 5
        sum_star += '*'
    print(sum_star)
    sum_star = ''
# print(sum_star)
