# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는
word = input()
new_word = ''
for i in range(len(word)):
    if word[i].islower():
        new_word += word[i].upper()
    else:
        new_word += word[i].lower()
print(new_word)