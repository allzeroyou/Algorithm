# n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
# 수열에서 x가 등장하는 횟수 계산
# 시간복잡도는 O(logN)으로 알고리즘 설계할 것.

# n과 x가 정수형태로 공백으로 구분되어 입력
# n개의 원소가 정수 형태로 구분되어 입력
# 수열의 원소 중 값이 x인 원소의 개수 출력. 단 값이 x인 원소가 하나도 없다면 -1 출력

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
suyeol = list(map(int, input().split()))
# bisect_right: 정렬된 순서에서 x가 삽입되어야 하는 인덱스 : 6
# print(bisect_right(suyeol, x))
# bisect_left: 정렬된 순서에서 x가 처음 발생한 인덱스 : 2
# print(bisect_left(suyeol, x))
ans = bisect_right(suyeol, x) - bisect_left(suyeol, x)  # 발생 횟수 구하기
print(ans if ans else -1)

'''
7 2
1 1 2 2 2 2 3
'''

# 출력
'''
4
'''
