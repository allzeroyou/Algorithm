n = int(input())

num = map(int, input().split())  # 공백으로 구분한 하나의 문자열을 리스트로

sosu = 0  # 소수: 1과 자기 자신으로 나눌때만 나눠 떨어지는 수

for i in num:
    cnt = 0
    if i > 1:  # 1은 소수 아님
        for j in range(2, i):  # 2부터 n-1까지
            if (i % j == 0):
                cnt += 1  # 2부터 n까지 나눈 값이 0이면 cnt 중가
        if cnt == 0:
            sosu += 1  # cnt가 없으면 소수임!
print(sosu)
