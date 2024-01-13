a, b = map(int, input().split())


# 최대공약수
# 유클리드 호제법
# a를 b로 나눈 나머지를 r이라고 할때, gcd(a,b) = gcd(b,r)와 같다. 이때 r이 0이면 b가 최대공약수.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(a, b))

# 최소공배수
lcm = a * b // gcd(a, b)  # 파이썬: 정수형/정수형 -> 실수형이므로 정수형 출력을 위해 //로 바꿔줌.
print(lcm)
