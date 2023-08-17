# nPm
from itertools import permutations

n, m = map(int, input().split())
nums = []
for i in range(1, n+1):
    nums.append(i)

perm = list(permutations(nums, m))

for i in perm:
    for j in i:
        print(j, end=' ')
    print()