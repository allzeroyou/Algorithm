import collections

cnt, k = map(int, input().split())
yose = collections.deque()

for i in range(1, cnt+1):
    yose.append(i)
while yose:
    for i in range(cnt-1):
        yose.append(yose.popleft())
        yose.popleft()
    print(yose.popleft(), end='')
    if yose:
        print(',', end='')
print('>')
