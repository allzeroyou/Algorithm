# 등차, 등비를 구분해야 함

def solution(common):
    answer = 0
    # 등비수열 -> 공비 구하기 위해 나눌 경우 -> 런타임 에러
    # 먼저, 등차 수열인지 부터 판별
    
    if common[1]-common[0]==common[2]-common[1]:
        # 등차수열
        d = common[1]-common[0]
        answer = common[-1]+d
        return answer
    
    # 등비수열
    if common[0] !=0: # 런타임 에러 방지용
        r = common[1]//common[0]
    else:
        r = common[2]//common[1]
    answer = common[-1] * r
    return answer