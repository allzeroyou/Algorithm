t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 뒤에서부터 탐색한다. (가격을 미리 알고있기에)
    price = list(map(int, input().split()))[::-1]
    # 이익
    profit = 0
    # 현재 가격
    now_price = price[0]

    for i in range(1, n):
        # 현재 금액이 더 높다면
        if now_price > price[i]:
            profit += now_price - price[i]
        else:
            now_price = price[i]
    print(f'#{tc} {profit}')
