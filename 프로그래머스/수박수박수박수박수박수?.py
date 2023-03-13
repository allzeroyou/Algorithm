def solution(n):
    str = '수박'

    if n%2 == 0:
        return str*(n//2)
    else:  # 홀수
        return str*(n//2)+str[:1]
    # 다른 사람의 풀이
    # str = '수박'*n
    # return str[:n]
    
print(solution(3))
print(solution(4))
print(solution(5))

