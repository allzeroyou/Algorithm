def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_val = 0
        for j in range(i, n+1): # 더하려는 연속하는 자연수 증가
            sum_val += j
            # 연속한 자연수의 합이 n인지 검사
            if sum_val == n:
                answer += 1
            elif sum_val > n:
                break
    return answer