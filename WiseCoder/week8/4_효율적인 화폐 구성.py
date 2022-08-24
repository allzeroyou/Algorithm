# 정수 n, m 입력받기
n, m = map(int, input().split())
# n개의 화폐 단위 정보 입력받기
money = []
for i in range(n):
    money.append(int(input()))
# 한번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001]*(m+1) # m+1: 0부터 m원까지 각각의 금액에 대한 최소한의 화폐개수를 구함
# 보텀업-dp
d[0]=0
for i in range(n): # 각 화폐단위를 확인하면서
    for j in range(money[i], m+1): # 각각의 금액 확인 -> 최적의 해 찾기
        # 현재 금액-화폐단위 -> 금액을 만들 수 있다면! == (i-k)원을 만드는 방법이 존재할 경우
        if d[j-money[i]] != 10001:
            d[j]=min(d[j], d[j-money[i]]+1)
# 계산된 결과 출력
if d[m] == 10001:    # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])