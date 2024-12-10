# 올림픽
# 규칙
# 1.금메달 수가 더 많은 나라
# 2.금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3.금,은 메달 수가 같으면, 동메달 수가 더 많은 나라

# 국가: 1~n 사이 정수
# 한 국가의 등수 : 자신보다 더 잘한 나라 수 +1 <- 등수 로직 계산의 핵심

# sort() 함수 사용 후 key 로 정렬 ?

# 국가 수, 등수 구할 국가
n, k = map(int, input().split())
total = {}

for i in range(n):
    tmp = list(map(int, input().split()))
    total[tmp[0]] = tmp[1:]

# 등수 계산
cnt = 0
for i in range(1, n + 1):
    # 1.금메달
    if total[k][0] < total[i][0]:
        cnt += 1
    # 2.금메달 같을 때
    elif total[k][0] == total[i][0]:
        # 은메달로 비교
        if total[k][1] < total[i][1]:
            cnt += 1
        # 3. 금,은 메달 같을때
        elif total[k][1] == total[i][1]:
            # 동메달로 비교
            if total[k][2] < total[i][2]:
                cnt += 1
print(cnt + 1)
