# n개의 정수, 정수 v가 몇개 인지 구하기

n = int(input())
lst = list(map(int, input().split()))
v = int(input())

ans = 0
for l in lst:
    if v==l:
        ans +=1
print(ans)
