def solution(phone_book):
    answer = True

    d = {}
    for pn in phone_book: # 전화번호를 하나씩 돌면서
        d[pn]=1
        
    for pn in phone_book:
        temp = ""
        for num in pn:
            temp += num
            if temp in d and temp!=pn:
                answer = False
    return answer