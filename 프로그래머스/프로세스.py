
from collections import deque


def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]  # index와 인덱스 쌍으로 이뤄진 튜플로 변환해 queue에 저장.
    answer = 0
    while True:
        cur = queue.pop(0)  # queue의 첫번째 요소 추출

        if any(cur[1] < q[1] for q in queue):  # 현재 우선순위 보다 더 높은 우선순위가 있다면
            queue.append(cur)  # queue의 뒤쪽에 넣는다.
        else:  # 현재 우선순위가 가장 높은 경우
            answer += 1
            if cur[0] == location:  # 현재 요소의 인덱스와 location가 일치할 경우
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))