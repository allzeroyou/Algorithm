import sys

input = sys.stdin.readline  # 빠른 입력
sys.setrecursionlimit(10 ** 8)  # 재귀 제한 늘려주기


def dfs(now):  # 현재 노드 번호
    # 다음 노드로 가기 위해
    # 열이 몇 번 일때의, 1 인 값? 을 찾아낸다.
    for nxt in range(n):  # 한줄 쭉 돌면서
        if adj[now][nxt] and not chk[nxt]:
            # 첫번째 조건: now 행에서 next 열의 1이 있다면==now에서 next로 가는 간선 존재(연결되어 있음)
            # 두번째 조건: 연결만 되었다고 가면 안됨! 방문체크 필수!
            chk[nxt] = True # 방문 완
            dfs(nxt)  # 다음 노드 (next는 예약어라 nxt로)


# 정점, 간선 입력받기
n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = 1
    adj[b][a] = 1 # 양방향 그래프

# for i, row in enumerate(adj):
#     print(f'{i}: {row}')

# 방문 체크
ans = 0
chk = [False] * n  # 방문(정점개수만큼)체크 처음에 False로 초기화 -> 방문 시 True로

for i in range(n):
    if not chk[i]:  # 방문 안한노드 발견시
        chk[i] = True  # 방문 체크함
        ans += 1  # dfs 한 횟수(count 변수)
        dfs(i)
print(ans)
