# 10대 컴퓨터. 1~10까지 번호 부여
# 1번 데이터-1번 컴퓨터, .. 10번 데이터-10번 컴퓨터, 11번 데이터-1번 데이터, 12번 데이터-2번 데이터..
# 총 데이터수 : a^b
# 마지막 처리될 컴퓨터 번호는?

# 1차 시도 - 시간초과(1초)
# T = int(input())
#
# for i in range(T):
#     a, b = map(int, input().split())
#     data = pow(a, b)
#     print(data % 10)

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    first = a % 10

    if first == 0:  # 10일 경우
        print(10)
    elif first in [1, 5, 6]:  # 1,5,6일 경우
        print(first)
    elif first in [4, 9]:  # 4, 9일 경우
        second = b % 2  # 경우 2가지
        if second == 1:
            print(first)
        else:
            print(first ** 2 % 10)
    else:  # 2,3,7,8 일 경우
        third = b % 4  # 경우 4가지
        if third == 0:
            print(first ** 4 % 10)
        else:
            print(a ** third % 10)
