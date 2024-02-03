x, y, w, h = map(int, input().split())

# 거리구하는 공식
a = min(w - x, h - y)
b = min(x - 0, y - 0)
print(min(a, b))