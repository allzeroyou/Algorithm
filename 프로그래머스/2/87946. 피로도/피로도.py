from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0 # 탐험할 수 있는 최대 던전수
    answer = -1
    
    # 모든 던전 탐험 순서에 대해 시도
    for perm in permutations(dungeons):
        current_tired = k # 현재 남은 피로도를 초기 피로도 설정
        dungeons_explored = 0 # 탐험한 던전 수를 세기 위한 변수 초기화
        
        # 현재 순서의 던전들에 대해 탐험 시도
        for min_required, tired_cost in perm:
            # 현재 피로도가 던전의 최소 필요 피로도 이상일때만 탐헌 가능
            if current_tired >= min_required:
                current_tired -= tired_cost # 던전 탐험 -> 피로도 소모
                dungeons_explored += 1 # 던전 탐험 수 증가
            else:
                break
        # 최대 던전 수 업데이트
        max_dungeons = max(max_dungeons, dungeons_explored)
    return max_dungeons