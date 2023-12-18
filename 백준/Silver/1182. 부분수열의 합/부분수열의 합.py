# n: 정수 개수, 합: s
n, s = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
ans = []


# 백트래킹
def back(start):
    global cnt

    if sum(ans) == s and len(ans) > 0:  # s일때 개수 증가
        cnt += 1

    for i in range(start, n):  # start 부터 다음 탐색 진행
        ans.append(num[i])
        back(i + 1)
        ans.pop()


# 함수 실행
back(0)
print(cnt)  # 부분 수열 개수 출력
