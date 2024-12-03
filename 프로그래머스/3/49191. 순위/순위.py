# A 선수가 B 선수를 이기고, B 선수가 C 선수를 이긴다면 -> A 선수는 B, C 선수를 이길 수 있다. 
# 자신의 순위를 알기 위해선 자신을 제외한 모든 선수와의 경기 기록을 가지고 있어야한다. 

from collections import defaultdict

def solution(n, results):
    answer = 0
    win = defaultdict(set) # key: 승자, val: 패자
    lose = defaultdict(set) # key: 패자, val: 승자
    
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
        
    for i in range(1, n+1):
        for winner in lose[i]: # 이긴 사람은 또 이김
            win[winner].update(win[i])
        for loser in win[i]: # 진 사람은 또 짐
            lose[loser].update(lose[i])
            
    for i in range(1, n+1):
        # 순위를 알려면 n-1개의 기록을 가지고 있어야 함
        if len(win[i]) + len(lose[i]) == n-1:
            answer +=1
        
    return answer