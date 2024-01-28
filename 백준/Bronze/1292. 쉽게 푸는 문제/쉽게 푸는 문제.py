# 구간 합
a, b = map(int, input().split())
ans = 0
nums = []
# 수열 만들기
for i in range(1, b + 1):
    for j in range(i):
        nums.append(i)

print(sum(nums[a - 1:b]))