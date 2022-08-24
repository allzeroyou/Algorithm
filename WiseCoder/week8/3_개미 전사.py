# 개미전사가 일직선으로 이어진 여러 식량창고를 선택적으로 약탈
# 최소 한 칸 이상 떨어진 식량 창고를 약탈해야할 때, 획득 식량의 최댓값을 구하라.

# 정수 N 입력받기
n = int(input())

# 모든 식량 정보 입력받기
arr = list(map(int, input().split()))

# dp 테이블 초기화
d = [0] * 100

# dp-보텀업
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):  # 3번째~n-1번째 항까지
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[n - 1])
