n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def dfs(i, cnt, tot):
    global ans
    if i >= n:
        if cnt > 0 and tot == s:
            ans += 1
        return
    dfs(i + 1, cnt, tot)
    dfs(i + 1, cnt + 1, tot + arr[i])


dfs(0, 0, 0)

print(ans)
