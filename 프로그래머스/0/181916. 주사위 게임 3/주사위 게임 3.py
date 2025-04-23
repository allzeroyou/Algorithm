from collections import defaultdict

def solution(a, b, c, d):
    lst = [a,b,c,d]
    
    # 1) 4개 숫자 모두 같음
    if a==b==c==d:
        return 1111*a

    # 2) 개수 세기
    dic = defaultdict(int)
    for l in lst:
        dic[l]+=1
        
    # (값, 빈도) 리스트를 빈도 내림차순으로 정렬
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    # 3) 3개 숫자 같고, 1개 숫자 달라야
    if dic[0][1]==3:
        x = dic[0][0] # 3개
        y = dic[1][0] # 1개
        return (x*10 + y)**2
    # 4) 두 쌍씩 있는 경우
    if dic[0][1]==2 and dic[1][1]==2:
        x = dic[0][0]
        y = dic[1][0]
        return (x + y) * abs(x-y)
    # 5) 한 쌍만 있고, 나머지 2개가 다른 경우
    if dic[0][1]==2:
        x = dic[1][0]
        y = dic[2][0]
        return x * y
    # 6) 모두 다를 경우
    min_dic= min(dic)
    return min_dic[0]