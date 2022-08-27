n = int(input())

a_list = []
b_list = []
ans = [0] * (n + 1)

for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

for i in range(n - 1, -1, -1):  # 날짜를 뒤쪽에서부터 확인
    if a_list[i] + i > n:
        ans[i] = ans[i + 1]
    else:
        ans[i] = max(b_list[i] + ans[i + a_list[i]], ans[i + 1])
        # 현재의 일을 맡았을때의 보상, 현재 일을 끝낸 다음날 쌓여있는 보상 둘을 비교
print(ans[0])
