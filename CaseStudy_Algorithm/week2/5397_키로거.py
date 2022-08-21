for _ in range(int(input())):
    stk1 = []  # 커서 왼쪽
    stk2 = []  # 커서 오른쪽
    for ch in input():
        if ch == '<':
            if stk1:
                stk2.append(stk1.pop())
        elif ch == '>':
            if stk2:
                stk1.append(stk2.pop())
        elif ch == '-':
            if stk1:
                stk1.pop()
        else:
            stk1.append(ch)

    print(''.join(stk1) + ''.join(reversed(stk2)))