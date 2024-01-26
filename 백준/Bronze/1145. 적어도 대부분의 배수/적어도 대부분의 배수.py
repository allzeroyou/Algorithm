# 5개 자연수
# 적어도 대부분의 배수는 위의 수 중 적어도 3개로 나눠지는 가장 작은 자연수

nums = list(map(int, input().split()))

# 증가시킬 숫자
tmp = 1

while True:
    cnt = 0  # 각 반복마다 cnt 초기화
    tmp += 1

    for num in nums:
        if tmp % num == 0:
            cnt += 1

    if cnt >= 3:
        break

print(tmp)
