def solution(s):
    answer = 0

    # 문자열 s를 숫자로 변환하는 함수.
    # 맨앞에 부호 +, - 올 수 있음.
    if s[0]== '-':
        return int(s[0]+(s[1:]))
    else:
        return int(s)

print(solution('-123'))
