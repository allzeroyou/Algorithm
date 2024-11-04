def solution(phone_book):
    answer = True
    
    # 전화번호가 다른 전화번호의 접두어인지 판단
    # 접두어인지 어캐 판단하지
    # in ?
    # 시간복잡도 고려해야함. 그냥 for문 돌면 시초날수도
    
    phone_book.sort() # 정렬
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer= False


    return answer