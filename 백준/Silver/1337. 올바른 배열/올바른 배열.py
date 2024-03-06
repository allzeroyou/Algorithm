# 올바른 배열: 배열의 5개가 연속적인 것
# 연속: 5개의 수를 정렬했을 때, 인접한 수의 차이가 1인 것.
# 올바른 배열이 되도록 필요한 원소의 최소 개수

n = int(input())

arr = [int(input()) for _ in range(n)]

# 인접한 수의 차이가 1이 되게 해야 함. <- 이걸 어떤 자료구조로 쓰면 좋을까: 투포인터(for문 2개 사용)
# 1. 오름차순 정렬
arr.sort()

# 정답-최댓값으로 세팅(문제 조건: 백억)
ans = 10 * 11

# 해당 원소로 이뤄진 5개의 임시 수열
tmp = [0] * 5

for i in range(len(arr)):
    # 5개가 되는지 세기
    five = 0

    for j in range(5):  # 2. 5개로 이뤄진 연속 수열을 만든다.
        tmp[j] = arr[i] + j

    cur = i  # 해당 원소를 따로 변수로 빼준다.

    for k in range(5):  # 3. 현재 수열을 돌면서
        if cur < len(arr) and arr[cur] == tmp[k]:  # 몇개가 일치되는지 검사
            five += 1
            cur += 1

    ans = min(ans, 5 - five)  # 이미 연속된 수를 빼면 필요한 수를 알 수 있다.

print(ans)