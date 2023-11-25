def solution(nums):
    # n마리 중 n/2 마리 가져가는 것이 최대값
    max_ans = len(nums)//2
    
    # 폰켓몬 개수 저장
    d = {}
    
    for n in nums:
        if n not in d:
            d[n]=1
        else:
            d[n]+=1
    if len(d) >= max_ans:
        return max_ans
    else:
        return len(d)
        