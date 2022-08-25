# a[i]=a[i-2]+ a[i-1]인 전형적인 피보나치 수열 문제
k =int(input())


a = [1, 0]
b = [0, 1]

for i in range(2, k+1): # 3th부터 시작
    a_cnt = a[i-1]+a[i-2]
    a.append(a_cnt)
    b_cnt = b[i-1]+b[i-2]
    b.append(b_cnt)

print(a[k], b[k])