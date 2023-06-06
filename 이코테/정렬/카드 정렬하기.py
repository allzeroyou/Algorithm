# 정렬된 두 묶음의 숫자 카드
# 각 묶음의 카드의 수를 a, b라고 하면, 보통 두 묶음을 합쳐 하나로 만드는 데에는 A+B번의 비교 필요
# 매우 많은 숫자 카드 묶음 중 두 묶음씩 골라 서로 합쳐나감
# 고르는 순서에 따라 비교 횟수 달라짐
# ex. 10장, 20장, 40장 묶음이 있다면,
# 10장 + 20장 합친 뒤, 합친 30장 묶음과 40장을 합친다면 10+20 + 30+40 = 100번의 비교 필요
# 그러나 10장+40장을 합친 뒤, 50장과 20장을 합친다면 10+40 + 50+20 = 120번의 비교 필요.
# n개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇번의 비교가 필요한지 구하는 프로그램 작성


# 1. 메모리 초과
'''
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort() # 카드를 오름차순으로 정렬

two_set = 0
if n == 1: # 카드가 1장일때는 비교 불가 -> 0 출력
    print(0)
for a in range(n-1):
    two_set += arr[a] + arr[a + 1]  # 2묶음
    arr[a+1]=two_set

print(arr[a + 1])
'''

# 2. 우선순위 큐 이용
# 우선순위 큐는 자료구조로 '힙'을 가지고, 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나옴.
# 배열, 연결리스트 : 삽입 시 시간복잡도 O(n)으로 너무 크므로 힙을 사용.

from heapq import heappush, heappop

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
card = []
for _ in range(n):
    heappush(card, int(input()))
if n == 1:  # 카드가 하나라면 비교 x
    print(0)
else:
    two_set = 0
    while len(card) > 1:
        min_first = heappop(card)
        min_sec = heappop(card)
        two_set += min_first + min_sec
        heappush(card, min_first + min_sec)
    print(two_set)