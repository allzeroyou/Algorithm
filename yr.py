import time

n = 10000
m = 10
time_sum = 0


def sum_of_n_2(n):
    start = time.time()  # 실행 시작

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()  # 실행 종료

    return the_sum, end - start  # 합과 실행시간


for i in range(m):
    time_sum += sum_of_n_2(n)[1]

print(f"1부터 {n}까지 더하는데 평균적으로 {time_sum / m:7.5f}초 걸림.")
