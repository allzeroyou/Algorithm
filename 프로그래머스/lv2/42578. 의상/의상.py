def solution(clothes):
    # 각 행 [의상 이름, 의상 종류]로 이뤄짐
    d = {}
    cnt = 0
    res = 1
    for i in clothes:
        if i[1] not in d:
            d[i[1]] = 1
        else:
            d[i[1]]+=1
    # print(d)
    # for j in d:
    #     if len(d) == 1:
    #         return d[j]
    #     else:
    #         cnt += (d[j])
    # print(cnt)
    for k in d.values():
        res *= (k+1) # 계수들의 합
    return res-1 # x^3의 계수 빼기

    