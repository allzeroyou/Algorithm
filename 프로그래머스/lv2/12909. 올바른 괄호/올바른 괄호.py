def solution(s):
    answer = True

    lst = []

    for i in range(len(s)):
        if s[i] == "(":
            lst.append(s[i])
        else:
            if lst == []:
                return False
            else:
                lst.pop()

    if lst != []:
        return False
    return True
