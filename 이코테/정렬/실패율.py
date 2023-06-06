# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수/스테이지에 도달한 플레이어 수
# 전체 스테이지 개수: n
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 return

# 단,
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.


def solution(N, stages):
    answer = []
    player = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)# 스테이지에서 머물러 있는 플레이어 수

        # for s in stages:
        #     if i == s:  # 현재 스테이지에서 실패했다면
        #         cnt += 1  # 실패한 사용자 수
        if player == 0:
            fail = 0
        else:
            fail = (cnt / player)  # 실패율 계산

        answer.append((i, fail))  # 스테이지 번호, 실패율 원소 삽입.
        player -= cnt

    # 실패율을 기준으로 각 스테이지 내림차순으로 정렬
    answer = sorted(answer, key=lambda f: f[1], reverse=True)

    #print(answer)
    # 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]	))
