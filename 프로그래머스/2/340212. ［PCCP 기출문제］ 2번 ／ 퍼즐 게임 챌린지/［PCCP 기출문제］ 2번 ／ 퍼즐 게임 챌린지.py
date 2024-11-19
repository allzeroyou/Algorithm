# 게임 제한시간: limit 존재 -> 제한시간 내 모든 퍼즐 해결하기 위한 level 최솟값?
# 퍼즐 난이도 배열: diffs
# 퍼즐 소요시간 배열: times
# 전체 제한 시간: limit

# level를 찾을때 -> 1~max diff에서 하나씩 해보는 브루트포스는 시초남
# -> 이진탐색!
# 왼쪽: l, 오른쪽: r 설정하고, 중간값으로 limit 내 풀리는지 확인

def solution(diffs, times, limit):
    l = 1
    r = max(diffs)
    answer = r # diffs 최대값일경우로 초기화
    
    while l< r:
        level = (l+r)//2
        time = times[0]
        
        for i in range(1, len(diffs)):
            k = 0
            # 게임 규칙
            if level< diffs[i]:
                # diff-level번 틀림
                k = diffs[i]-level
            # 퍼즐 틀릴때마다 time_cur만큼 시간 사용
            # 추가로 time_prev만큼 시간 사용해 이전 퍼즐 다시 풀고 와야함
            time += (times[i] + times[i-1])*k + times[i]
        if time <= limit:
            r = level
            answer = level
        else:
            l = level + 1
    
    return answer