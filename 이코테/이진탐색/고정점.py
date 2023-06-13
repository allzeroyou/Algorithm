# 고정점: 수열의 원소 중 그 값이 인덱스와 동일한 원소
# 수열 a = [-15, -4, 2, 8, 13]이 있을때
# a[2]= 2이므로, 고정점은 2가 된다.

# n개의 서로 다른 원소 포함.
# 모든 원소가 오름차순 정렬
# 이 수열에서 고정점이 있다면 고정점을 출력하는 프로그램 작성
# 고정점은 최대 1개 존재
# 고정점이 없다면 -1 출력

# 시간복잡도 O(logN)으로 알고리즘 설계할 것.

# 찾는 고정점이 mid 중간값과 동일하다
# 중간값이 가리키는 위치의 값보다 중간값이 작은 경우, 왼쪽 부분 탐색
# 중간값이 가리키는 위치의 값보다 중간값이 큰 경우, 오른쪽 부분 탐색 반복

n = int(input())
suyeol = list(map(int, input().split()))


def binary_search(suyeol, start, end):
    if start > end:
        return None
    mid = (start + end) // 2  # 중간값
    if suyeol[mid] == mid:  # 고정점이라면
        return mid
    # 중간값이 가리키는 위치의 값보다 중간값이 작은 경우
    if mid < suyeol[mid]:
        return binary_search(suyeol, start, mid - 1)
    else:
        return binary_search(suyeol, mid + 1, end)


# 이진탐색 수행
index = binary_search(suyeol, 0, n - 1)
if index == None:
    print(-1)
else:
    print(index)

'''
5
-15 -6 1 3 7
--
7
-15 -4 2 8 9 13 15
--
7
-15 -4 3 8 9 13 15
'''

'''
3
2
-1
'''
