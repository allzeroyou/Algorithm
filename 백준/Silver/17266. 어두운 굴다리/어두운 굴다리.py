# 굴다리: 0~n
# 가로등 설치 개수: m, 가로등 위치: x
# 가로등: 높이만큼 주위 비출 수 있음
# 최소한의 높이로 굴다리 모든 길 비추고자 함

# sol
# 0으로 채워진 배열을 만든 후 높이를 맞춰가면서(for문) 비춘 곳은 1로 변경
# 배열이 모두 1인 높이 출력

n = int(input())
m = int(input())
light = list(map(int, input().split()))

# 높이 조절
ans = 0
# 가로등이 1개면 0, n 끝까지 비춰야 함
if len(light) == 1:
    ans = max(light[0] - 0, n - light[0])
else:
    for i in range(len(light)):
        # 첫번째라면
        if i == 0:
            hei = light[i]
        # 끝점이라면
        elif i == len(light) - 1:
            hei = n - light[i]
        else:  # 중간이라면
            mid = light[i] - light[i - 1]  # 현재 - 이 전 가로등
            # 둘이 반반 씩 부담하면 됨
            if mid % 2 == 0:
                hei = mid //2
            else:  # 홀수라면 +1 해준다
                hei = mid // 2 + 1
        ans = max(ans, hei)

print(ans)
