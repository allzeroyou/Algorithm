# 팰린드롬인지 아닌지 확인
word = input()

if word == word[::-1]:
    print('1')
else:
    print('0')
