# https://www.acmicpc.net/problem/9613

t = int(input())


def gcd(a, b):
    # a > b일때, a%b=n가 0이면 b가 최대공약수임.
    # 나머지가 0이 아니라면, a에 b를 대입하고 b에 n을 대입해서 0이 나올때까지 반복함.
    n = a % b
    if n == 0:
        return b
    else:
        return gcd(b, n)


for _ in range(t):
    tc = list(map(int, input().split()))
    ans = 0
    for i in range(1, tc[0] + 1):
        for j in range(i + 1, tc[0] + 1):
            ans += gcd(tc[i], tc[j])
    print(ans)
