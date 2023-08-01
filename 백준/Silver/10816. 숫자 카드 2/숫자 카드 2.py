# 상근이가 가진 숫자 카드 개수
n = int(input())
# 숫자 카드에 적힌 정수
sg_cards= list(map(int, input().split()))

# 상근이가 몇 개 가지고 있는 숫자카드인지 구해야 할 m개의 정수
m = int(input())
find_cards = list(map(int, input().split()))

card_count = {} # 카드 순서대로 개수 세야함

for sg_card in sg_cards:
  if sg_card in card_count:
    card_count[sg_card]+=1
  else:
    card_count[sg_card]=1

# 답
answer = []
for find_card in find_cards:
  if find_card in card_count:
    answer.append(card_count[find_card])
  else:
    answer.append(0)
    
for a in answer:
  print(a, end=' ')