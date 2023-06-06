money = int(input())
cnt = 0

while 1:
    if money % 5 == 0:  # 먼저 5로 나눈 후
        cnt += money // 5
        break
    else:
        money -= 2  # 2원씩 빼면서 5로 나눠떨어지는 게 나오도록
        cnt += 1
    if money < 0:  # 거스름돈 불가
        break
if money < 0:
    print(-1)
else:
    print(cnt)