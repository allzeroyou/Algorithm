from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_cnt = Counter(cards)

for num in nums:
    print(card_cnt.get(num, 0), end=" ")