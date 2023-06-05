n = int(input())
first = 666  # 1번째 영화제목

while n != 0:  # while 종료조건: n이 0일떄
    if '666' in str(first):  # first안에 666이 있을때
        n = n - 1  # 1 감소
        if n == 0:
            break
    first += 1
print(first)