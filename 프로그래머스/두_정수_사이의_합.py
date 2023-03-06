def solution(a, b):
    answer = 0
    # a와 b 사이에 속한 모든 정수의 합 리턴.
    # 3, 5 -> 3+4+5 = 12

    if a <= b:
        for i in range(a, b + 1):
            answer += i
    elif a > b:
        for i in range(b, a + 1):
            answer += i

    return answer
