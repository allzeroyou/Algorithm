# deque를 import해서 사용
from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()

# Contain 1, 2, 3, 4, 5 in deq
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)
# deque([5, 1, 2, 3, 4])

deq.rotate(-1)
print(deq)
# deque([1, 2, 3, 4, 5])