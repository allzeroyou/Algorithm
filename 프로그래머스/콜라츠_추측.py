def solution(num):
    answer = 0
    # 주어진 수가 1이 될 때까지 다음 작업 반복.. 모든 수를 1로 만들수 있다는 추측
    # 입력된 수가 짝수라면 2로 나누고, 홀수라면 3을 곱하고 1을 더함
    # 결과로 나온 수에 같은 작업을 1이 될때까지 반복
    if num==1:
        return 0
    while True:
        if num % 2 == 0:
            num = num // 2
            answer += 1

        else:
            num = num * 3 + 1
            answer += 1
        if num == 1:
            break
        if answer == 500:
            return -1

    return answer


print(solution(1))

