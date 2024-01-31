# 피보나치를 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:  # f(2)와 f(1)은 항상 1이기 때문에 호출 정지
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(4))
# 문제점: n이 커지면 커질수록 수행 시간이 기하급수적으로 늘어난다.

