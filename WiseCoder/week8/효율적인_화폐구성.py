# n가지 종류의 화폐들의 개수를 최소한으로 이용해 그 가치의 합이 m원이 되도록 한다.
# 각 화폐는 개수 제한이 없으며, 사용 화폐 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

# 정수 n, m 입력 받기
n, m = map(int, input().split())

# n 개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:    # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:    # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])