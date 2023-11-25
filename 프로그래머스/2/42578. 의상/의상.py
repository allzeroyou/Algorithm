def solution(clothes):
    answer = 0
    
    d={} # 의상저장 해시
    
    for c in clothes:
        if c[1] not in d:
            d[c[1]]=2 # 입었을 때 + 안 입었을 때 -> 경우의 수: 2
        else:
            d[c[1]]+=1
    
    cnt = 1 # 의상 조합 개수
    for num in d.values():
        cnt *= num
        
    return cnt-1 # 의상을 하나도 안 입었을때 경우의 수 빼주기