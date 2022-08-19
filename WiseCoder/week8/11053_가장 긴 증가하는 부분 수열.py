'''
어떤 임의의 수열이 주어질 때, 이 수열에서 몇 개의 수들을 제거해서 부분수열을 만들 수 있다.
이때 만들어진 부분수열 중 오름차순으로 정렬된 가장 긴 수열을 최장 증가 부분 수열이라 한다.
'''

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp=[1]*n

for i in range(1, n):
    for j in range(i):
        if a[j]<a[i]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))

