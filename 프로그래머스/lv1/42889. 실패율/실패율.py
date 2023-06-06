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