def solution(nums):
    # 최대한 많은 종류의 폰켓몬을 포함해 n/2 마리 선택
    n = len(nums)//2
    # 해시 이용
    poketmon = dict()
    
    for i in nums:
        if i not in poketmon:
            poketmon[i] = 1    
        else:
            poketmon[i] += 1
     # n/2 마리의 폰켓몬을 선택하는 방법중
    if len(poketmon)>= n : # n/2 보다 포켓몬 종류가 많다면
            return n    #가장 많은 종류의 폰켓몬을 선택하는 방법 찾아 폰켓몬 종류 개수 return
    else:
        return len(poketmon)
