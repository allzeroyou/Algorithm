cnt = int(input())
arr = []
for i in range(cnt):
    arr.append(int(input()))

arr.sort()
# print(arr)

for j in arr:
    print(j)
'''
빠른 입력과 출력    
import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
'''