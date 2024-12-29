# 팀: 6명의 선수, 팀 점수: 상위 4명의 점수 합
# 점수: 6명 주자가 모두 참가
# 우승: 점수를 더해 가장 낮은 점수를 얻는 팀
# 동점: 5번째 주자가 빨리 들어온 팀 우승(==점수가 낮음)
from collections import defaultdict

# sol
# 딕셔너리로 각 팀당 인원수 세기
# if dic.values() < 6이라면 카운트 포함 x
# for 문으로 순차적으로 점수 합
# 동점이라면 그 다음 주자의 점수가 낮은 팀 -> 우승

tc = int(input())

for t in range(tc):
    num = int(input())
    scores = list(map(int, input().split()))
    dic = {}
    for i in scores:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    # 점수 저장
    grades = defaultdict(list) # 모든 key에 대해 기본값으로 list 지정
    grade = 0
    for s in scores:
        # 6명 보다 적다면 pass
        if dic[s] < 6:
            continue
        grade += 1
        grades[s].append(grade)
    # 우승팀 가리기
    # 4번째까지 점수 합, 5번째 요소 저장
    ans = {}

    for key, val in grades.items():
        # 4번째 요소까지 누적합 계산
        n_sum = sum(val[:4])

        # 누적합과 5번째 요소 저장
        ans[key] = (n_sum, val[4])

    # 동점일때, 5번째 점수 비교
    res = sorted(ans.keys(), key=lambda x: (ans[x][0], ans[x][1]))

    print(res[0])