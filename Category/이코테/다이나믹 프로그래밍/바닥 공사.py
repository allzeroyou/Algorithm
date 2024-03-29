# 다이나믹 기초 예제 -> 타일링 문제 유형
# 바닥을 채우는 모든 경우의 수?
# 답: 796796으로 나눈 수 출력

# 문제 해결 아이디어
# 1. 도식화, 그림으로 그려 생각하기
# 2. 점화식 도출

n = int(input())

d = [0] * (n + 1)

d[1] = 1
d[2] = 3

for i in range(3, n+1): # n+1임에 주의
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])
