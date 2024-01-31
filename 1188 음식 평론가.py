# https://www.acmicpc.net/problem/1188

sausage, person = map(int, input().split())


def gcd(a, b):
    n = a % b
    if n == 0:
        return b
    else:
        return gcd(b, n)


if sausage % person == 0:
    print(0)
else:
    print(person-gcd(sausage, person))
