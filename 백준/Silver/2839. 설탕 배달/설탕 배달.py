n = int(input())
k = [3, 5]

d = [5001] * (n + 1)
d[0] = 0
# dp- bottom-up
for i in range(len(k)):  # 설탕 단위 체크
    for j in range(k[i], n + 1):
        if d[j - k[i]] != 5001:
            d[j] = min(d[j], d[j - k[i]] + 1)
if d[n] == 5001:
    print(-1)
else:
    print(d[n])