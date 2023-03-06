def solution(n):
    # 자연수 n이 매개변수, n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x return
    # 나의 풀이
    for i in range(1, n + 1):
        if n % i == 1:
            return i

    # 다른 사람의 풀이
    # return [x for x in range(1, n+1) if n%x==1][0]

print(solution(12))
