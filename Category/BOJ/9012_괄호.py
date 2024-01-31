# 괄호문자열 ps
# 괄호의 모양이 올바르게 구성된 문자열을 올바른 괄호 문자열(valid ps, vps) 라고 함
# vps is true -> YES
# vps is false -> NO

num = int(input())


def check_vps(num):
    for i in range(num):
        bracket = input()
        vps_stack = []
        for j in bracket:
            if j == '(':
                vps_stack.append(j)
            elif j == ')' and '(' not in vps_stack:
                vps_stack.append(j)
            elif j == ')':
                vps_stack.pop()

        if len(vps_stack):
            print('NO')
        else:
            print('YES')

check_vps(num)