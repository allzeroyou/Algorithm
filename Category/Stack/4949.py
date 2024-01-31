'''
- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
- 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
'''

'''
while True:
    word = input()
    stack = []
    no = 0
    for i in word:
        if i=='(' or i =='[':
            stack.append(i)
        elif i==')':
            if len(stack) == 0 or stack[-1] != '(':
                print('no')
                no += 1
                break
            else:
                stack.pop()
        elif i==']':
            if len(stack) == 0 or stack[-1] != '[':
                print('no')
                no += 1
                break
            else:
                stack.pop()
        elif i=='.':
            break
    if word=='.':
        break

    if len(stack)==0 and no ==0:
        print('yes')

위 코드의 반례: ([)] -> no가 출력되어야 하지만 yes가 출력됨
'''

while True:         # '.'가 입력되기 전까지 반복
    s = input()     # 사용자로부터 문자열 입력 받음
    if s == '.':    # 종료 조건
        break
    stack = []      # 괄호들을 저장할 스택(리스트)

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')


