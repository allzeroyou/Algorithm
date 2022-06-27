# 6
nterms = int(input("몇 번째 항까지 구할까요? "))
fibo = []
for i in range(nterms+1):
    if i == 0: # 0번째 항
        fibo.append(0)
    elif i == 1: # 1번째 항
        fibo.append(1)
    else: # 2번째 항 이상
        fibo.append(fibo[i-1]+fibo[i-2])
print(fibo)
