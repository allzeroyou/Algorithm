# 비밀번호 발음하기
# 규칙
# 1.모음: a, e, i, o, u 중 하나 반드시 포함
# 2.모음 3개 or 자음 3개 연속으로 오면 안됨
# 3.같은 글자가 연속적으로 2번 오면 안되나, ee와 oo는 허용

mo = ['a', 'e', 'i', 'o', 'u']

while 1:
    password = input()
    if password == 'end':
        break
    # 1. aeiou 중 하나 반드시 포함
    cnt = 0
    for p in password:
        if p in mo:
            cnt += 1
    if cnt == 0:
        print(f'<{password}> is not acceptable.')
        continue
    flag = 0
    # 2.
    for i in range(len(password) - 2):
        if password[i] in mo and password[i + 1] in mo and password[i + 2] in mo:
            flag = 1
        elif not (password[i] in mo) and not (password[i + 1] in mo) and not (password[i + 2] in mo):
            flag = 1
    if flag == 1:
        print(f'<{password}> is not acceptable.')
        continue

    # 3.
    flag2 = 0
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] == 'e' or password[i] == 'o':
                continue
            else:
                flag2 = 1
    if flag2 == 1:
        print(f'<{password}> is not acceptable.')
        continue

    print(f'<{password}> is acceptable.')
