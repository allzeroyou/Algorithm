# 투 포인터 + 구간합

n, m = map(int, input().split())

nums = list(map(int, input().split()))

# left, right
left = 0
right = 1
# m이 되는 경우의 수 카운트
cnt = 0

while left <= right <= n:
    # 구간합 계산
    s = sum(nums[left:right])

    if s < m:
        right += 1  # 오른쪽으로 한칸
    elif s > m:
        left += 1  # 왼쪽으로 한칸
    else:  # 같을 경우
        cnt += 1
        right += 1  # 오른쪽으로 한칸

print(cnt)
