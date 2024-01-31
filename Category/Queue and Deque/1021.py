'''
회전하는 큐
n개의 원소를 포함하고 있는 양방향 순환 큐
3가지 연산 가능
1. 첫번째 원소 뽑아내기. 원래 큐의 원소가 a1, ..., ak 이었던 것이 a2, ... ak 처럼 된다
=> popleft()
2. 왼쪽으로 한 칸 이동. a1, ..., ak 이었던 것이 a2, ..., ak, a1이 된다
=> append(popleft())
3. 오른쪽으로 한 칸 이동. a1, ..., ak 이었던 것이 ak, a1, ..., ak-1
=> appendleft(pop())
'''
from collections import deque

n, m = map(int, input().split())
lst = deque(range(1, n+1))
q = deque(map(int,input().split()))

count = 0
while q:
    mid = len(lst)//2          # mid 변수를 생성 lst의 중간 index로 설정
    if lst.index(q[0])>mid:    # 만약 lst.index(q[0])가 mid보다 크다면 3번 조건 반복
                                # 반대일 경우는 2번 조건 반복
        while q[0]!=lst[0]:
            lst.appendleft(lst.pop())
            count += 1
        lst.popleft()
        q.popleft()
    else:
        while q[0]!=lst[0]:
            lst.append(lst.popleft())
            count += 1
        lst.popleft()
        q.popleft()
print(count)
