word= input()

alpha = list(range(97, 123)) # 아스키코드 숫자 범위

for _ in alpha:
    print((word.find(chr(_))), end=' ')
