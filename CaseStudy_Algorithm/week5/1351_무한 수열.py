dp = dict()  # 해당 n에 대한 An만 저장
dp[0] = 1


def A(i):
    if i not in dp:  # key값이 있는지 없는지 확인
        dp[i] = A(i // p) + A(i // q)
    return dp[i]


n, p, q = map(int, input().split())
print(A(n))
# print(len(dp))