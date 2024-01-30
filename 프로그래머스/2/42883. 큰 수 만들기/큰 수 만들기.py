def solution(number, k):
    answer = [] # stack 이용
    
    for num in number:
        # 제거할 수가 k 남았고
        # 스택에 값이 있고
        # 스택의 마지막 값이 num보다 작다면
        # 제거 후 제거할 수 k를 1씩 감소
        while k>0 and answer and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)
    # k가 남아있는 경우
    if k!=0:
        answer = answer[:-k]
    # 배열을 문자열로 변환
    return ''.join(answer)