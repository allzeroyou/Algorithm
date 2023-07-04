# 0~n번까지의 번호 부여
# 모든 학생이 서로 다른 팀으로 구분, 총 n+1
# 이때 "팀 합치기" or "같은 팀 여부 확인" 연산 사용 가능

# 팀 합치기: 두 팀을 합치는 연산
# 같은 팀 여부 확인: 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산
# M개의 연산 수행, 수행 연산 결과 출력

n, m = map(int, input().split())
parent = [0]*(n+1) # 부모 테이블 초기화

# 두 원소가 속한 집합 합치기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루드 노드를 찾을때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 특정 원소가 속한 집합 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 부모테이블에서, 부모를 자기자신으로 초기화
for i in range(0, n+1):
    parent[i]= i

# 각 연산을 하나씩 확인 # 서로소 집합 알고리즘 사용
for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
print(parent)

