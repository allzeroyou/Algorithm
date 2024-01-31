N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]

answer = [] # 제거된 사람들 담을 리스트

num = 0
for i in range(N):
    num += K-1
    if num >= len(arr):
        num = num%len(arr)
    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')
