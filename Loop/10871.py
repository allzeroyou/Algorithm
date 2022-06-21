n, x = map(int, input().split())
suyeol = []

suyeol = list(map(int, input().split()))

for i in range(len(suyeol)):
    if suyeol[i] < x:
        print(suyeol[i])


# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분해 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# n, m, k를 공백으로 구분해 입력
n, m, k = map(int, input().split())
print(n, m, k)