'''
import sys
import time

start = time.time()
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for j in arr:
    sys.stdout.write(str(j)+'\n')
end = time.time()

print(f'{end-start:.5f}sec')
# 1.62130sec, memory: 169MB
'''

import sys
import time

start = time.time()
N = int(sys.stdin.readline())
arr = [0]*10001 # 10000보다 작거나 같은 자연수(0포함해서 +1)

for i in range(N):
    arr[(int(sys.stdin.readline()))]+=1 # 요소가 나온 횟수 누적

for j in range(10001):
    sys.stdout.write(str(j)+'\n')
end = time.time()

print(f'{end-start:.5f}sec')