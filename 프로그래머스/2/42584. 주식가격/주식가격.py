from collections import deque


def solution(prices):
    answer = []

    # 인덱싱하지 않기 위해 큐 사용
    queue = deque(prices)

    while queue:
        # 가격이 떨어지지 않은 시간
        sec = 0
        price = queue.popleft()
        # 주식 가격 순회
        for q in queue:
            sec += 1
            if price > q:  # 현재 가격이 클 경우
                break
        answer.append(sec)

    return answer
