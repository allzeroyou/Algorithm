from math import sqrt

def solution(n):
    answer = 0

    # n이 어떤 정수 x의 제곱?
    # n이 x의 제곱이라면, x+1 제곱 리턴
    # 아니라면 -1 리턴

    # 1차 시도
    # if n == pow(sqrt(n),2):
    #     answer = pow(sqrt(n) + 1, 2)
    #     return answer
    # else:
    #     return -1
    # 테스트 케이스 통과 x

    # 2차 시도
    root = n ** 0.5  # sqrt(스퀘어루트) 를 import(임포트) 하지 않아도 됨.

    # if int(root)==root:
    if root % 1 == 0:  # 제곱근이라면 나머지가 깔끔히 떨어짐.
        return (root + 1) ** 2
    else:
        return -1


print(solution(11))
print(solution(9))
