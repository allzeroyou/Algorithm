def solution(s):
    answer = ' '
    # s를 띄어쓰기 기준으로 슬라이스 한 후
    # split( ) 로 할 경우 -> 공백이 몇개건 하나로 퉁쳐서 처리.
    # 따라서 split(" ") 로 명시해서 사용
    s = s.split(" ")

    # 예제만 통과한 코드
    # for i in s:  # 3people
    #     for c in range(len(i)):  # 3
    #         if c == 0 and i[c].isdigit():
    #             answer += i[0]
    #             continue  # 첫문자가 알파벳이 아니라면, 나머지 글자는 소문자로.
    #         # if s의 첫문자가 알파벳이라면, 대문자로 변경후 나머지 글자는 소문자로.
    #         elif c == 0 and i[c].isalpha():
    #             answer += i[0].upper()
    #             continue
    #         answer += i[c].lower()
    #     answer += ' '
    #
    # answer.rstrip()
    #
    # return answer

    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return answer.join(s)
