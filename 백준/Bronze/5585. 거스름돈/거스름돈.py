# 지불할 돈
pay = int(input())
# 잔돈
coins = [500, 100, 50, 10, 5, 1]
# 1000-지불할 돈 -> 최대한 거스름돈 개수가 적어야 함
change = 1000 - pay

# 동전 개수
coin_cnt = 0

# 동전 종류에 따라 잔돈 나누기
for coin in coins:
    if change == 0:
        break
    coin_cnt += change//coin
    change %= coin # 동전으로 나눈 잔돈

print(coin_cnt)
