# 알파벳 대문자, 숫자 0~9로만 구성된 문자열이 입력으로
# 모든 알파벳을 오름차순으로 정렬해 이어서 출력
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력.
string = ''
S = input()
num_lst = []
str_lst = []

for i in S:
    if i.isdigit():  # 숫자일 경우
        num_lst.append(i)
    else:
        str_lst.append(i)

str_lst.sort()

print(''.join(str_lst) + str(sum(list(map(int, num_lst)))))

'''
K1KA5CB7
AJKDLSI412K4JSJ9D
'''
