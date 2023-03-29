# 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 1. 숫자가 쓰인 카드들이 n x m 형태로 놓여 있음
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행 선택
# 3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드 뽑아야 함
# 4. 따라서 처음에 카드를 골라낼 행 선택 시 이후 해당 행에서 가장 숫자가 낮은 카드를 뽑을 걸 고려해 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함.

n, m = map(int, input().split())

answer = 0
for i in range(n):
    cards = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수
    min_card = min(cards)
    # 행 별로 가장 큰 수 추출
    answer = max(min_card, answer)

print(answer)

'''
3 3
3 1 2
4 1 4
2 2 2
'''

'''

'''
