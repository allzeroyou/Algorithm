# 붕대감기
# bandage: [붕대감기 기술 시전 시간(t), 1초당 회복량(x), 추가 회복량(y)]
# health: 최대 체력
# attacks: [몬스터 공격 시간, 피해량] -> 공격시간 기준 오름차순 정렬

# 모든 공격 후 현재 체력 return
# 체력<=0 -> -1 return

def solution(bandage, health, attacks):
    t,x,y = bandage # 파이썬 언패킹: 리스트의 요소를 꺼내 각 변수에 할당
    total_time = attacks[-1][0] # 전체시간
    att_dic = { a[0] : a[1] for a in attacks} # 시간복잡도 줄이기 위해 -> 딕셔너리로 조회하기
    
    k = 0 # 연속 시간
    cur_health = health # 현재 체력
    
    
    for i in range(total_time+1):
        if i in att_dic: # 몬스터 공격 시간일때
            cur_health -= att_dic[i] # 딕셔너리 값에 접근
            k = 0 # 연속시간 초기화
            
            if cur_health<=0:
                return -1
            continue
            
        cur_health += x # 1초 회복량
        k += 1 # 연속 시간 증가
            
        if k == t: # 연속 시간과 일치한다면
            k = 0 # 연속 시간 초기화
            cur_health += y # 추가회복량 더하기
            
        cur_health = min(health, cur_health) # 최대 체력 넘지 않는 코드 기술!
   
    return cur_health