'''
상근 cd의 수 N
선영 cd의 수 M
상근의 CD번호 오름차순
다음줄에는 선영의 CD번호 오름차순
CD의 번호는 오름차순

집합or 맵으로 풀이 가능
'''
import sys
imput = sys.stdin.readline()

while True:
    N, M = map(int, input().split())
    if N==0 and M==0:
        break
    a = set()
    for _ in range(N):
        a.add(input())
    b = set()
    for _ in range(M):
        b.add(input())
    print(len(a&b))

