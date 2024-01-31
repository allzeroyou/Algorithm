x = int(input())

# x가 3으로 나눠떨어지면 3으로 나눔
# x가 2로 나눠떨어지면 2로 나눔
# 1을 뺀다.

# 세개 적절히 사용해 1로 만들려 함. 연산을 사용하는 횟수 최솟값.
cnt = 0

while (True):
    if (x % 3 == 0):
        if x % 3 == 1:
            break
        else:
            x = x / 3
            cnt += 1
            print(f'x%3 {cnt}')


    elif (x % 2 == 0):
        if x % 2 == 1:
            break
        else:
            x = x / 2
            cnt += 1
            print(f'x%2 {cnt}')
    else:
        if x == 1:
            break
        else:
            x -= 1
            cnt += 1
            print(f'x-1 {cnt}')


print(cnt)
