a, b, c = map(int, input().split())


def power(n):
    if n == 0:
        return 1  # n이 0이면 1을 반환한다.
    if n % 2 == 0:
        return (power(n // 2) ** 2) % c  # n이 짝수면 power(n//2)의 제곱을 반환한다.
    # n이 홀수면 power(n//2)의 제곱에 a를 곱한 값을 반환한다.
    return ((power(n // 2) ** 2) * a) % c


print(power(b))