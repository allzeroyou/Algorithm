'''
n개의 문자열로 이뤄진 집합 S

입력: m개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇개인지?

시간제한: t가 S에 있는지 확인할 때, in을 사용 -> 자료구조에 따라 시간 복잡도가 다름
set/dict은 hash table 구조(key에 데이터를 저장하는 구조, key를 통해 데이터를 받아오기 때문에 빠름)
hash는 hashing function(key에 대한 산술연산을 통해 데이터의 위치를 찾는 함수) -> O(1에서 최악의 경우 O(n)의 시간복잡더
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()

for i in range(N):
    S.add(input())

ans = 0
for _ in range(M):
    t = input()
    if t in S:
        ans += 1
print(ans)