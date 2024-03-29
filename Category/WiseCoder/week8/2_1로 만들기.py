'''
x 연산 방식은 4가지
1. 5로 나누어 떨어지면 5로 나눈다.
2. 3으로 나누어 떨어지면 3으로 나눈다.
3. 2으로 나누어 떨어지면 2으로 나눈다.
4. x에서 1을 뺀다
연산 사용 횟수의 최솟값을 구하라.
'''

X = int(input())
dp = [0]*30001

for i in range(2, X+1): # 1: 연산 x
    # 현재의 수에서 1을 빼는 경우 + 연산횟수 1 추가
    dp[i]=dp[i-1]+1

    # 현재의 수가 2로 나누어 떨어지는 경우 + 연산횟수 1 추가
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)    # 둘 중 작은 값으로 갱신

    # 현재의 수가 3으로 나누어 떨어지는 경우 + 연산횟수 1 추가
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)    # 둘 중 작은 값으로 갱신

    # 현재의 수가 5로 나누어 떨어지는 경우 + 연산횟수 1 추가
    if i%5==0:
        dp[i]=min(dp[i], dp[i//5]+1)    # 둘 중 작은 값으로 갱신

print(dp[X])