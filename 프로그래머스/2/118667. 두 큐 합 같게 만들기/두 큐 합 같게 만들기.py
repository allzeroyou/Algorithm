# 자료구조: 큐 -> FIFO
# deque로 만들고-> popleft(), append()
# 근데 이제 두 큐 합을 동일하게 만드는 방법은,..?
# 일단 두 큐의 합을 구하고, 만들 값을 찾자!

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 1. 목표값 구하기
    # 1-1. q1, q2 어떤거에서 pop해올지 sum 값 구하기
    sum_q1, sum_q2 = sum(q1), sum(q2)
    
    # 2. 연산 횟수 제한값 (while 종료조건)
    limit = (len(q1))*4 # = (len(q1)+len(q2))*2
    # 연산 횟수 세기
    cnt = 0  

    # 3. 합 같아질때까지 반복
    # while(cnt <= limit): -> #11에서 시간초과
    for i in range(limit):
        # 목표값이라면 종료
        # 두 큐 합 같다면
        if sum_q1==sum_q2:
            return i
        # 3-1. 목표값 > q1: q1에 append해야함
        # 두 큐 합으로 비교하기
        if sum_q1 < sum_q2:
            val= q2.popleft()
            q1.append(val)
            sum_q1 += val
            sum_q2 -= val
        else: # 목표값 <= q1:
            val = q1.popleft()
            q2.append(val)
            sum_q1 -= val
            sum_q2 += val
   
    # print(cnt)
    answer = -1
    return answer
