# 만들 수 있는 소수 개수 리턴
from itertools import permutations
from math import sqrt


def solution(numbers):
    answer = []

    # 1. 한자리수로 쪼개기
    nums = list(map(int, numbers))
    # 2. 소수 후보 숫자 만들기
    temp = []
    for i in range(1, len(numbers) + 1):  # numbers의 각 숫자들을 순열로 만들 경우
        temp += list(permutations(nums, i))

    per = []
    for t in temp:
        per.append("".join(map(str, t)))

    # 3. 소수 판별(소수: 1과 자기자신만 약수로 가짐)
    for p in per:
        p = int(p)

        # 0,1은 소수 아님
        if p < 2:
            continue

        # 소수이려면 제곱근 수까지 약수가 없어야.
        sqrt_num = int(sqrt(p))
        flag = True
        for i in range(2, sqrt_num + 1):
            if p % i == 0:  # 소수 아님
                flag = False
                break
        if flag:
            answer.append(p)
    print(answer)
    return len(set(answer))  # 중복 제거 후 개수 반환
