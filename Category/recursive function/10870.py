'''
피보나치 수
0과 1로 시작
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째부터는 바로 앞 두 피보나치 수의 합
n이 주어졌을 때 n번째 피보나치 수를 구하는 프로그램 작성
'''

n = int(input())


def fibo(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

print(fibo(n))

