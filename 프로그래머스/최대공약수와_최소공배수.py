import math


def solution(n, m):
    answer = []
    # n, m의 최대공약수, 최소공배수 배열 반환.

    # 1. for문 이용
    # 최대공약수
    for i in range(min(n, m), 0, -1):  # 최소값~ 0까지.
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    # 최소공배수
    for i in range(max(n, m), n * m + 1):  # 최대값~ n*m까지.
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    # 2. import math
    # def lcm(n,m):
    #     return (n * m)
    # a = math.gcd(n, m)
    # b = lcm(n, m)
    # answer.append(a)
    # answer.append(b)

    return answer
