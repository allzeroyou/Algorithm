def solution(s):
    lst = []

    for i in range(len(s)):
        if s[i] == "(":
            lst.append(s[i])
        else:
            if not lst:
                return False
            else:
                lst.pop()

    # if '(' in lst:
    if lst:
        return False
    return True

print(solution(")(()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
