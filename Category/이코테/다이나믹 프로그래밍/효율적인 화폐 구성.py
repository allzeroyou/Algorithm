# n 가지 종류의 화폐
# 화폐들의 개수를 최소한으로 이용해 가치의 합이 m원이 되도록
# 각 화폐는 몇 개라도 사용 가능
# 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 간주
# 2, 3원 화폐 -> 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수

# 불가능할때는 -1 출력

n, m = map(int, input().split())

# n개의 화폐 가치 정보 입력받기
money_value = []
for v in range(n):
    money_value.append(int(input()))

# dp 테이블
d = [10001] * (m + 1)
d[0] = 0 # 왜 붙는거지?? # 화폐단위 0원으로는 아무것도 만들 수 없기 때문에 개수가 0
for i in range(n):
    for j in range(money_value[i], m + 1):
        if d[j - money_value[i]] != 10001:  # i-k 원 만드는 법 존재
            d[j] = min(d[j], d[j - money_value[i]] + 1)
# 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
'''
2 15
2
3
'''

'''
3 4
3
5
7
'''
# https://hgk5722.tistory.com/12 참고 블로그