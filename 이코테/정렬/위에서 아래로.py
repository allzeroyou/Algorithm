# 수열-크기 상관없이 나열
# 큰수부터 작은수 순서로 나열
# 내림차순 정렬

n = int(input())

# n개의 정수를 입력받아 배열에 저장
suyeol = []
for i in range(n):
    suyeol.append(int(input()))

suyeol = sorted(suyeol, reverse=True)

# print(suyeol)
for i in suyeol:
    print(i, end=' ')

'''
3
15
27
12
'''