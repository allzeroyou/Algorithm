#  2개의 마을로 분리하고, 유지 비용을 최소로 하기 위해서 마을의 길 중에 유지 비용이 가장 큰 길을 없앤다

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
# 유지 비용이 가장 큰 경로 없애서 마을 분리
last = 0

for edge in edges:
    C, A, B = edge
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C
        last = C

print(result - last)