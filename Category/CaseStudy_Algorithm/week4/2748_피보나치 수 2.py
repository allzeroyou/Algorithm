# fibo = [0,1]
#
# for i in range(2, 91): # O(N): 반복문 1번 돔
#     fibo.append(fibo[-1]+fibo[-2]) # append는 맨 뒤에 추가 빠름 O(1) / 중간,.. 앞으로 갈수록 느려짐

# print(fibo[int(input())])

n = int(input())

cache = [[0] * 91 for _ in range(91)]
cache[0] = 0
cache[1] = 1

for i in range(2, n + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[n])
