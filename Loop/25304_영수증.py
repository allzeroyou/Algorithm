x = int(input()) # 영수증 총 금액
n = int(input()) # 구매한 물건 종류

res = 0
for i in range(n):
    # 각 물건의 가격과 개수
    a, b = map(int, input().split())
    res += a*b

if res==x:
    print('Yes')
else:
    print('No')
