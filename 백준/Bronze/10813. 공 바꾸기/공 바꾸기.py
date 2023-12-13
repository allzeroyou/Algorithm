n, m = map(int, input().split())

ball = [x for x in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    ball[i - 1], ball[j - 1] = ball[j - 1], ball[i - 1]

for b in ball:
    print(b, end=' ')