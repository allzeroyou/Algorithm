n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
first = lst[n - 1]
second = lst[n - 2]

# 가장 큰수가 더해지는 횟수 계산.
fir_cnt = int(m / (k + 1)) * k + m % (k + 1)
# 두번째로 큰 수가 더해지는 횟수
sec_cnt = m - fir_cnt

# 결과 도출.
answer = int(first * fir_cnt + second * sec_cnt)

print(answer)
