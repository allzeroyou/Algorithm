# 개미전사가 일직선으로 이어진 여러 식량창고를 선택적으로 약탈
# 최소 한 칸 이상 떨어진 식량 창고를 약탈해야할 때, 획득 식량의 최댓값을 구하라.

# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):   # 창고가 i개 있다고 할 때
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])