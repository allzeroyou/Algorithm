t = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    # 최대이익
    ans = 0

    # 개수
    n = int(input())
    nums = list(map(int, input().split()))

    # 범위 탐색용
    start = -1
    end = -1

    # 탐색
    while start < n - 1:
        # 최대 매매가
        max_val = 0
        # 가장 높은 매매가의 인덱스 구하기
        for j in range(end + 1, n):
            if nums[j] > max_val:
                max_val = nums[j]
                end = j

        for i in range(start + 1, end):
            ans += (max_val - nums[i])
        start = end

    print(f'#{test_case} {ans}')
