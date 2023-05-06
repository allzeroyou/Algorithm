import sys

input = sys.stdin.readline

# 짝수번째 알파벳 -> 대문자
# 홀수번째 알파벳 -> 소문자로

# def solution(s):
#     answer = ''
#     lst = list(s.split())
#     print(lst)
#     for i in range(len(lst)):
#         for i in range(len())
#
#
#     return answer

def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]
solution("try hello world"	)