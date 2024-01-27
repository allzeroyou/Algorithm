# 팰린드롬 수
# 뒤에서 읽어도 똑같은 수

while 1:
    num = input()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')