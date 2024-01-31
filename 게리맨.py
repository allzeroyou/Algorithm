n = int(input())
population = []
for _ in range(n):
    population.append(list(map(int, input().split())))


def solution():
    min_ans = 20 * 20 * 100  # 최댓값으로 초기화
    for x in range(n):
        for y in range(n):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    # 나머지 세 모서리가 범위 내에 있어야 함
                    if (0 <= x + d1 < n and 0 <= y - d1 < n) and (0 <= x + d2 < n and 0 <= y + d2 < n) and (
                            0 <= x + d1 + d2 < n and 0 <= y - d1 + d2 < n):
                        # 구역 설정하기 위한 배열
                        section = [[5 for _ in range(n)] for _ in range(n)]
                        # 1번 구역
                        for i in range(d1 + 1):
                            r1, c1 = x + i, y - i
                            for tr in range(r1):
                                section[tr][c1] = 1
                        r2, c2 = x + d1, y - d1
                        for tc in range(c2):  # c2에 해당하는 열 인덱스에 대해 루프를 돈다. 왼쪽 아래 모서리부터 c2 열까지의 열을 1번 구역으로 설정
                            for tr in range(r2):  # r2에 해당하는 행 인덱스에 대해 루프를 돈다. 왼쪽 아래 모서리부터 r2 행까지의 행을 1번 구역으로 설정
                                section[tr][tc] = 1
                        # 2번 구역
                        for i in range(d2 + 1):
                            r1, c1 = x + i, y + i
                            for tc in range(c1 + 1, n):  # 오른쪽으로
                                section[tr][tc] = 2
                        r2, c2 = x, y
                        for tr in range(r2):  # 아래로
                            for tc in range(c2 + 1, n):  # 왼쪽으로
                                section[tr][tc] = 2
                        # 3번 구역
                        for i in range(d2 + 1):
                            r1, c1 = x + i, y - i
                            for tc in range(c1, n):
                                section[tr][tc] = 3
                        r2, c2 = x + d1 + d2, y - d1 + d2
                        for tr in range(r2 + 1, n):
                            for tc in range(c2):
                                section[tr][tc] = 3
                        # 4번 구역
                        for i in range(d1 + 1):
                            r1, c1 = x + d2 + i, y - i + d2
                            for tr in range(r1 + 1, n):
                                section[tr][c1] = 4
                        r2, c2 = x + d2, y + d2
                        for tc in range(c2 + 1, n):
                            for tr in range(r1 + 1, n):
                                section[tr][tc] = 4
                        # 계산
                        cal = [0 for _ in range(6)]  # 5번 구역까지

                        for r in range(n):
                            for c in range(n):
                                sec = section[r][c]
                                cal[sec] += population[r][c]

                        ans = max(cal[1:]) - min(cal[1:])

                        if min_ans > ans:
                            min_ans = ans
    print(min_ans)


solution()
