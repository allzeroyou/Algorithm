def solution(s):
    answer = ''

    if len(s) % 2 != 0:  # 홀수일경우
        return s[len(s) // 2]
    return s[len(s) // 2 - 1] + s[len(s) // 2]