# 디펜스 게임
# 병사 n명으로 연속되는 적의 공격 순서대로 막기
# 디펜스 게임은 다음과 같은 규칙
# n명의 병사, 매 라운드마다 enemy[i]마리의 적 등장
# 남은 병사 중 enemy[i]명 만큼 소모해, enemy[i]마리의 적 막을 수 있음
# 만약, 남은 병사 수 < 현재 라운드 적의 수 => 게임 종료
# 무적권: 병사의 소모 없이 한 라운드의 공격 방어 가능
# 무적권은 최대 k번 사용 가능 -> 적절한 시기에 사용해 최대한 많은 라운드 진행          
# 무적권을 어떻게 써야 최대한 많은 라운드까지 진행할까?
# -> 남은 병사들 중 힘이 쎈 애에 무적권 사용해야 함! -> 현재 라운드의 적의 힘을 저장해놓고, 가장 힘이 쎈 애에 사용하기
# -> 우선순위 큐 heapq 사용하기 (근데 이제 파이썬은 최소힙이 기본이라, -값 으로 저장해줘야 최대힙임)

import heapq
def solution(n, k, enemy):    
    # 병사 수
    soliders = n
    # 무적권
    strong = k
    # 최대힙
    max_heap = []
    # 라운드 수
    round = 0
    
    for i in range(len(enemy)):
        if soliders >= enemy[i]:
            soliders -= enemy[i]
            heapq.heappush(max_heap, -enemy[i])
        else: # 만약 병사를 다 썼다면
            # 무적권이 남아있을경우 사용!
            if strong >0:
                strong -= 1
                # 만약, 적이 더 많았던 라운드가 있었다면 무적권은 이때 사용하기로
                if max_heap and enemy[i] < -max_heap[0]:
                    soliders += -heapq.heappop(max_heap) # 병사 수 채우기
                    # 현재 적은 처지해야함
                    soliders -= enemy[i]
                    heapq.heappush(max_heap, -enemy[i])
            else: # 무적권도 없고, 병사수도 부족하다면 종료
                break   
        round += 1
        
    return round