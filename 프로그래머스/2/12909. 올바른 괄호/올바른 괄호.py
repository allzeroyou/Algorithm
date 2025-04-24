def solution(s):
    answer = True
    
    # 스택 구조
    stack = []    
    for i in range(len(s)):
        if len(stack)>0:
            last = stack[-1]

            if last == '(' and s[i]==')':
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
            
    answer = True if len(stack)==0 else False

    return answer