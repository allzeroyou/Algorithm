# https://www.acmicpc.net/problem/2839

# 그리디 알고리즘: 탐욕적으로 선택한다.

n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0: # n==0일때 걸림
        cnt += (n // 5)
        print(cnt)
        break
    else:
        n -= 3
        cnt += 1
else:
    print(-1)


