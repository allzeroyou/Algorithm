from heapq import heapify, heappush, heappop

def solution(operations):
    # heapq: 최소 힙
    # D-1: heappop()->최솟값
    # D 1: pop()->마지막 원소가 최댓값임
    
    answer =[]
    hq = []
    
    for op in operations:
        alp, num = op.split()
        num = int(num)
        # 삽입
        if alp=="I":
            heappush(hq, num)
        # 삭제
        else: 
            if hq: # 큐에 값이 있을 때
                if num == -1:
                    heappop(hq) # 최솟값
                else:
                    hq.sort()
                    hq.pop() # 최댓값
    
                    
    # 모든 연산 처리 후 정렬
    hq.sort()
    if hq:
        answer = [hq[-1], hq[0]]
    else:
        answer =[0,0]

    return answer
