import sys

input = sys.stdin.readline

# A,B 두 사람이 "서로 다른 볼링공" 고르려고 함
# 볼링공 총 N개,
# 같은 무게의 공 다름 간주, 무게는 1-M까지의 자연수로 존재

# 볼링공 고르는 경우의 수


N, M = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0  # 경우의 수 저장
for i in range(len(balls) - 1):  # A 가 고르고
    for j in range(i + 1, len(balls)):  # B 가 고른다..
        if balls[i] != balls[j]:  # A와 B가 다르면
            cnt += 1  # 경우의 수 증가
print(cnt)
