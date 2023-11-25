def solution(phone_book):
    answer = True
    
    d = {} # 문자열이 key -> 해시 이용
    
    for p in phone_book:
        if p not in d:
            d[p]=1
            
    
    for p in phone_book:
        tmp = '' # 문자열 비교용
        for n in p: # 전화번호를 순회하면서
            tmp += n
            if tmp in d and tmp!=p:
                answer=False
            
        
    return answer