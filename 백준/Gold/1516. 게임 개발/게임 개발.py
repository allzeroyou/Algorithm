import sys

n = int(input())
buildings = []
for i in range(n):
    buildings.append(list(map(int, sys.stdin.readline().split()))[:-1])  # -1 외의 숫자들을 리스트로 저장
times = [0] * n  # 각 빌딩을 짓는데 걸리는 최소 시간


def minTime(i, time, blist):  # 최소 시간 구하는 함수
    if len(blist) == 0:  # 이전에 지어야 하는 건물이 없을 경우
        times[i] = time
        return time
    else:  # 이전에 지어야 하는 건물이 있을 경우
        max_time, prev_time = 0, 0  # 짓는 시간 최댓값, 그전에 지어져야하는 건물 짓는 시간
        for b in blist:
            if times[b - 1] != 0:  # b번째 건물을 짓는데 걸리는 시간을 이미 구한 경우\
                prev_time = times[b - 1]
            else:  # b번째 건물을 짓는데 걸리는 시간을 새로 구해야 하는 경우
                prev_time = minTime(b - 1, buildings[b - 1][0], buildings[b - 1][1:])
            if max_time < prev_time:  # 짓는 시간 최댓값과 그전에 지어져야하는 건물 짓는 시간 비교해
                max_time = prev_time  # 최댓값 갱신
        times[i] = time + max_time  # 현재 건물 짓는 시간 + 그전에 지어져야 하는 건물 짓는 시간
        return time + max_time  # 해당 건물 짓는데 걸리는 최종 시간


for i in range(n):
    if times[i] == 0:
        minTime(i, buildings[i][0], buildings[i][1:])
    # if 0 not in times: # 모든 빌딩들을 짓는데 걸리는 시간을 구했을 경우 종료
    #     break

for time in times:
    print(time)
