import sys

input = sys.stdin.readline


# 0과 1로 이뤄진 어떤 문자열 "x"
# x의 모든 0 제거
# x의 길이를 c라고 하면 x를 "c를 2진법으로 표현한 문자열"로 바꿈.

# 예를 들어, x="0111010" -> 이진 변환 -> x="1111"(0 제거)
# 길이:4 이므로 이진 변환으로 ->"100"
# s가 1이 될 때까지 계속해서 이진변환
# 1. 이진 변환 횟수, 2. 제거된 0의 개수 -> 각각 배열에 담아서 return

# 남은 문자열 길이재기

# 길이를 bin()함수 써서 이진수로 변경
def solution(s):
    answer = []
    bin_cnt = 0
    zero_cnt = 0
    while 1:
        if s == '1':
            break
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        bin_cnt += 1
    answer = [zero_cnt, bin_cnt]
    return answer


print(solution("01110"))
