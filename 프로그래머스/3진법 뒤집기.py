import sys

input = sys.stdin.readline
# 자연수 n -> 매개변수
# n을 3진법 상에서 앞뒤로 뒤집은 후 다시 10진법으로 바꾼 수 return

def solution(n):
    answer = 0
    rev_str = ''
    while n > 0:
        n, mod = divmod(n, 3)  # 3진법 변환
        rev_str += str(mod)
    rev_str = (rev_str[::-1])[::-1]
    answer = int(rev_str)

    return answer