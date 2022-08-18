N = int(input())

cnt = 0

for i in range(N):
    s = input().rstrip() # 오른쪽 공백 제거
    stack = []
    for i in range(len(s)):
        if stack:
            if s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if not stack:
        cnt += 1

print(cnt)


