# 반복문
fibo = [0, 1]

for i in range(2, 91):  # n은 90보다 작거나 같은 자연수
    fibo.append(fibo[- 2] + fibo[- 1])  # 작은 수부터 큰수로 올라감

print(fibo[int(input())])
