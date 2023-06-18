import heapq


def solution(scoville, K):
    # 섞은 스코빌 지수 = 가장 맵지 않은 스코빌 지수 + (두번째로 맵지 않은 음식의 스코빌 지수 * 2)
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    while heapq[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer += 1

    return answer
solution([1, 2, 3, 9, 10, 12],7)