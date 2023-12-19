# n개의 바구니
# 1~n번까지 번호 적혀있음

# m번 바구니의 순서를 역순으로 만들려 함

# 한번 순서를 역순으로 바꿀 때 순서를 역순으로 만들 범위를 정하고
# 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.

n, m = map(int, input().split())

num = [x for x in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = num[i - 1:j]
    tmp.reverse()
    num[i - 1:j] = tmp

for n in range(n):
    print(num[n], end=' ')
