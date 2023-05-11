def solution(participant, completion):
    # 마라톤 참여 선수들 이름(string) 배열 : participant
    # 마라톤 완주 선수들 이름(string) 배열 : completion
    # 완주못한 선수의 이름 return
    # string으로 키 관리 -> hash 사용
    d = dict()
    
    # 참가자 중 동명이인 있을 수 있음
    for p in participant:
        # 효율성 33
        if p not in d:
            d[p] = 1
        else:
            d[p] += 1
        # 개선
        # d[x] = d.get(x, 0) + 1
    for c in completion:
        # if d[c] == 1: # 완주한 선수라면
        #     d.pop(c) # 제거
        d[c] -= 1
            
    for k,v in d.items():
        if v >0:
            return k
        
