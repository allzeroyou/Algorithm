# 두개의 배열 A, B
# N개의 원소로 이뤄잠
# 최대 K번의 바꿔치기: 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라 두 원소를 서로 바꾼다.
# 배열 A의 모든 원소의 합이 최대가 될때까지.
# N, K 그리고 배열 A, B의 정보가 주어질때 만들 수 있는 배열 A의 원소의 합의 최댓값을 출력.

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 배열 A 정렬 후 작은 숫자를 배열 B의 큰 수와 바꿔야 함.
a = sorted(a)
b = sorted(b, reverse=True)

# 최대 k번의 연산
for i in range(k):
    # 작은 숫자를 배열 B의 큰수와 바꿔야 함.
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

