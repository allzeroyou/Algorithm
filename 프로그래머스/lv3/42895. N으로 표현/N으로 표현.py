from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)
    # N 사용 횟수
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # NNN..N

        for j in range(1, i):
            # j 개
            for num1 in dp[j]:
                # i-j 개
                for num2 in dp[i - j]:  # 현재 연산 횟수 i에서 사용할 숫자 개수 j를 뺀다
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                        # number가 연산한 결과에 있으면 답으로 반환
        if number in dp[i]:
            return i
    return -1