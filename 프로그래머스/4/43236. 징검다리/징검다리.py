# 이분탐색
# left, right

def solution(distance, rocks, n):
    answer = 0
    left = 1
    right = distance
    
    # 정렬
    rocks.sort()
    rocks.append(distance)
    
    while left<=right:
        mid = (left+right)//2
        # 제거한 바위개수
        cnt = 0
        # 이전 바위 위치
        pre = 0
        for rock in rocks:
            dis = rock - pre
            # 거리가 커트라인보다 작다면, 바위 제거
            if dis < mid:
                cnt +=1
                if cnt > n:
                    break
            # 바위 제거 x -> 이전 바위 위치 갱신
            else:
                pre = rock
        # 초과 제거 -> 커트라인이 높은것
        if cnt > n:
            right = mid-1
        # 이하로 제거한경우 -> 커트라인이 적절 or 너무 낮음
        else:
            answer = mid
            left = mid+1
    
    return answer