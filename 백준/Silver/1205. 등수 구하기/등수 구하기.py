# 등수 구하기
import copy

# 게임 랭킹 리스트
# 매번 게임할 때 마다 얻는 점수가 비오름차순 저장됨

# 랭킹 리스트 등수는 위에서 몇번째 있는 점수인지?로 결정
# but 같은 점수 있을땐 그러한 점수 등수 중에 가장 작은 등수가 됨

# 100, 90, 90, 80일땐 각각의 등수는 1,2,2,4임

# 태수의 새로운 점수가 랭킹 리스트에서 몇등 하는지?

# 점수가 랭킹에 못 올라간다면 -1 출력
# 랭킹 리스트가 꽉 차있을때(len=length), 새 점수가 이전 점수보다 좋을때만 점수 바뀜
# sol
# sort(key=lambda(x[0]: x[1]), reverse=True) 로 내림차순 정렬하고, 같은 점수일때 동수 처리

n, new_score, p = map(int, input().split())

if n == 0:
    print(1)  # 랭킹리스트가 없을 경우 무조건 1등
else:
    scores = list(map(int, input().split()))
    original = copy.deepcopy(scores)
    scores.append(new_score)
    scores.sort(reverse=True)

    idx = scores.index(new_score)
    ori_idx = 0

    if scores.count(new_score) + scores.index(new_score) > p:
        print(-1)
        #ori_idx = original.index(new_score)  # 기존 순위 보다 커야 함.
    else:
        rank = [sorted(scores, reverse=True).index(score) + 1 for score in scores]
        print(rank[idx])