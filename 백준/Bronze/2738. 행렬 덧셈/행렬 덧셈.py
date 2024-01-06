n, m = map(int, input().split())
# a
a = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(n):
#     a.append(list(map(int, input().split())))

# b
b = [list(map(int, input().split())) for _ in range(n)]

# ans
ans = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        ans[i][j] = a[i][j] + b[i][j]
        print(ans[i][j], end=' ')
    print()