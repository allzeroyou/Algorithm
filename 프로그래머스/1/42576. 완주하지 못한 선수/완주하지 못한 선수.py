def solution(participant, completion):
    # 문자열로 key 관리 -> hash 사용
    
    d = {}
    
    for p in participant:
        if p not in d: # hash에 없을 경우
            d[p]=1 # 초기화
        else: # hash에 있을 경우(동명이인)
            d[p]+=1
    
    for c in completion:
        d[c]-=1
    
    for k, v in d.items():
        if v>0:
            return k