n = int(input())
d = [50001]*(n+1)
a=[3,5]

# di=i를 0으로 만들기 위한 최소 연산수
# k = 3, 5
# di=min(di, di-k+1)

d[0]=0

for i in range(2):
    for j in range(a[i], 1):
        if d[j-a[i]]!=50001:
            d[j]=min(d[j], d[j-a[i]]+1)

if d[n]==50001:
    print(-1)
else:
    print(d[n])

