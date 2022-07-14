import collections

# 맨 위에 있는 카드는 버리고 그 다음 카드는 밑으로 옮긴다
card = collections.deque()
count = int(input())

for i in range(1, count+1): # 1~count 까지
    card.append(i) # 덱에 저장

for i in range(1, count):
    card.popleft() # 맨 위 카드 제거
    if len(card)>1:
        card.append(card.popleft()) # 그 다음 카드 아래로

print(card[0]) # 마지막 1장

# print(card.popleft())

'''
from collections import deque
T=int(input());
dq=deque([*range(1,T+1)]);

for i in range(T-1):
    dq.popleft();
    dq.append(dq.popleft());
    print(dq);
    
print(dq[0]);

#123456
#i=0 23456->34562
#i=1 4562->5624
#i=2 624->246
#i=3 46->64
#i=4 4
'''