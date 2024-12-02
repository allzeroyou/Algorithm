# 삼각형 세변 길이
# Equilateral: 세 변 길이 같음
# Isosceles: 두 변 길이 같음
# Scalene: 세 변 길이 모두 다름
# Invalid: 가장 긴 변 > 나머지 두 변 합

# 입력 양의 정수 3개
# 마지막 줄은 0 0 0

while 1:
    a, b, c = map(int, input().split())
    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break

    max_n = max(a, b, c)
    li = [a, b, c]
    li.remove(max_n)
    if max_n >= sum(li):
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    elif a != b and b != c and a != c:
        print('Scalene')
