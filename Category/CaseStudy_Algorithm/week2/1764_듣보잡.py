N, M = map(int, input().split())

a = set()

for i in range(N):
    a.add(input())

b = set()
for i in range(M):
    b.add(input())

result = sorted(list(a&b)) # 집합 교집합

print(len(result))

for i in result:
    print(i)