import sys

input = sys.stdin.readline


# 0과 1로 이뤄진 어떤 문자열 x
# x의 모든 0 제거
# x의 길이를 c라고 하면 x를 c를 2진법으로 표현한 문자열로 바꿈.

# x="0111010" -> 이진 변환 -> x="1111"(0 제거) -> 길이:4이므로 이진법으로->"100"이됨.
# s가 1이 될때까지 계속해서 이진변환
# 이진 변환 횟수, 제거된 0의 개수를 각각 배열에 담아서 return

# 문자열 돌면서 0 제거

# 남은 문자열 길이재기

# 길이를 bin()함수 써서 이진수로 변경
def solution(s):
    answer = []
    binary_cnt = 0
    zero_cnt = 0

    while True:
        if s == "1":
            break
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        binary_cnt+=1
    answer=[binary_cnt, zero_cnt]
    return answer


print(solution("01110"))
