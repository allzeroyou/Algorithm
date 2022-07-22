import collections

cnt, k = map(int, input().split())
yose = collections.deque()

for i in range(1, cnt+1):
    yose.append(i)

print('<',end='')
for i in range(cnt-1):
    for m in range(k-1):                # k 번째가 올때까지 앞 요소 dequeue
        yose.append(yose.popleft())     # dequeue한 값을 queue에 덧붙이기
    print(f'{yose.popleft()}', end=', ')  # k 번째의 값 dequeue
print(f'{yose.popleft()}>', end='')     # 마지막 요소 + >
