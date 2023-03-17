def solution(left, right):
    # left~right까지 모든 수들 중에서, 약수의 개수가 짝수 -> +
    # 약수의 개수가 홀수 -> -

    # e.g. left: 13, right: 17 -> result: 43
    # 13 약수: 1, 13 => 짝수
    # 14 약수: 1,2,7,14 => 짝수
    # 15 약수: 1,3,5,15 => 짝수
    # 16 약수: 1,2,4,8,16 => 홀수
    # 17 약수: 1, 17 => 짝수

    # 13+14+15-16+17 = 43

    divisor_list = []
    answer = 0

    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if (i % j == 0):
                divisor_list.append(j)
        if len((divisor_list)) % 2 == 0:
            answer += i

        else:
            answer -= i
            divisor_list.clear()

    return answer
