n = int(input())
# 어떤 수의 약수개수는 제곱근을 기준으로 대칭적이다
# ex. 12의 약수개수는 1,2,3,4,6,12인데, 루트12(3.xx)보다 작은 수가 3개, 큰수가 3개임

i = 2
while n!=1:
    for i in range(2, n+1):
        # 2로 나눠지면 출력
        if(n%i==0):
            print(i)
            n = n//i # 다음 계산을 위해 n을 나눠줌(몫)
            break
