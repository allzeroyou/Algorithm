# 전화번호 phone_number
# 뒷 4자리를 제외한 나머지 숫자 전부 "*"로 가리기.

def solution(phone_number):

    lst_phone_number = list(phone_number)
    for i in range(0, len(phone_number) - 4):
        lst_phone_number[i] = "*"

    # print(lst_phone_number)
    return ''.join(lst_phone_number)

print(solution("01033334444"))