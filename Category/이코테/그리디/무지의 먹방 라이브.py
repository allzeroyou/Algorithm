import sys

input = sys.stdin.readline

# N개의 음식
# 1부터 N까지 번호
# 음식섭취시 일정 시간 소요
# 1번 음식부터 섭취 -> 번호가 증가하는 순서대로
# 1초동안 섭취 후 음식이 남는 경우 그대로 두고, 다음 음식 섭취.
# K초 후 중단.
# 네트워크 정상화 후 몇번 음식부터 섭취?

# food_times 각 음식을 먹는데 걸리는 시간이 리스트로
# 만약, 더 섭취해야할 음식이 없다면 -1을 반환하라.

def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i + 1))

    foods.sort()

    pretime = 0  # 이전 음식을 다 먹는 시간
    for i, food in enumerate(foods):
        diff = food[0] - pretime  # 이전 음식과 현재 음식 먹는 시간 차이
        if diff != 0:  # 차이가 없으면 스킵
            spend = diff * n
            if spend <= k:  # 남은 시간내에 음식이 먹어지면
                k -= spend
                pretime = food[0]  # 이전 음식 재설정

            else:  # 남은 시간내에 음식이 먹어지지 않으면
                k %= n  # 남은시간을 음식수로 나눈 나머지를 인덱스로
                sublist = sorted(foods[i:], key=lambda x: x[1])
                # 음식순서대로 재정렬
                return sublist[k][1]

        n -= 1

    return -1