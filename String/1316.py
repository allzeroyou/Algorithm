'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b,가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서
나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성
'''
n = int(input())
group_word = 0

for i in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]: # 연속되는 단어 판단
            new_word=word[index+1 : ] # 현재 글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:
                error += 1
    if error == 0:
        group_word += 1
print(group_word)

