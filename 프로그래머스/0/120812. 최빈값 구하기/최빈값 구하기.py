# 1. 딕셔너리화
# 2. value 기준 내림차순 정렬
    # if [0]==[1]: -1출력
    # [0] 출력
from collections import defaultdict 

def solution(array):
    answer = 0
    dic = defaultdict(int)
    
    for a in array:
        dic[a]+=1
    # value 기준 내림차순 정렬
    sorted_dic =sorted(dic.items(), key=lambda x:x[1], reverse=True)

    if len(sorted_dic) > 1 and sorted_dic[0][1]==sorted_dic[1][1]:
        return -1
    
    return sorted_dic[0][0]