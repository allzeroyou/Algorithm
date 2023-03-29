# 어떠한 수 n이 1이 될 때까지 두 과정 중 하나를 반복 수행해야.
# 두번째 연산은 n이 k로 나눠떨어질 때만 선택 가능

# 1. n에서 1을 뺀다
# 2. n을 k로 나눈다.(if n%k==0)

n, k = map(int, input().split())
cnt = 0

while (n != 1):
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)
