import sys

input = sys.stdin.readline

# N개의 동전
# 만들수 없는 양의 정수 금액 중 최솟값.
# N = 5이고 3, 2, 1, 9원짜리 동전 이라면 8원임.
# N = 3이고 3, 5, 7원짜리 동전 이라면 1원임

# 입력
N = int(input())
moneys = list(map(int, input().split()))

moneys.sort()  # 화폐를 오름차순으로 정렬

# target 초기화 (현재까지 더한 값의 다음 수)
# 이 수 앞까지는 만들 수 있고,
# 이 수에 해당하는 수가 들어온다면, 만들 수 있는 수를 연장 할 수 있다.
target = 1
for money in moneys:
    if money > target:  # 만들 수 있는 수의 바로 다음 수까지는 들어오면, 만들 수 있는 수를 이어갈 수 있다.
        break  # 그러나 그 수보다 더 큰 수가 들어오면, 이어나갈 수 없으니까, 못 만드는 수이다.
    target += money

