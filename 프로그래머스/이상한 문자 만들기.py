import sys

input = sys.stdin.readline


# 짝수번째 알파벳 -> 대문자
# 홀수번째 알파벳 -> 소문자로

def solution(s):
    answer = ''
    # 공백문자를 기준으로 자르기
    lst = list(s.split(" "))
    print(lst)
    # 자른 배열에서 짝수 인덱스 -> 대문자로, 홀수 인덱스 -> 소문자로
    cnt =0
    for i in lst:  # try
        c_lst = list(i)  # t,r,y
        for j in range(len(c_lst)):  # 3
            if j % 2 == 0:
                answer += c_lst[j].upper()
            else:
                answer += c_lst[j].lower()
        answer += " "

    print(answer[0:-1])
    return answer


solution(" try hello world ")
