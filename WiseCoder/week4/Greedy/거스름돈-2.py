money = int(input())

coins = [500, 100, 50, 10]
change_cnt = 0
for coin in coins:
    change_cnt += money // coin
    money %= coin

print(change_cnt)

# 화폐의 종류만큼 반복 수행
# 따라서 화폐의 종류가 K개라고 할때, 시간복잡도는 O(K).
# 그리드 문제는 이보다 어렵지만, 문제 접근 방법은 유사함.
# 따라서 거스름돈 문제는 그리드 알고리즘을 설명할때 자주 소개되는 문제임
