ans = 0
stk = []
last_open = False

for ch in input():
    if ch == '(':
        stk.append(ch)
        last_open = True
    else:
        stk.pop()
        ans += len(stk) if last_open else 1
        last_open = False

print(ans)