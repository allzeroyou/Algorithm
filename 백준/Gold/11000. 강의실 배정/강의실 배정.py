# Si~Ti에 끝나는 n개의 수업
# 최소 강의실을 사용해 모든 수업 가능해야 함
# 수업이 끝난 후에 다음 수업 가능(Ti<=Sj일 경우 i 수업과 j수업은 같이 들을 수 있음)
from heapq import heappush, heappop

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x: x[0])

# 항상 강의시간의 최솟값이 먼저 나와야 하므로 -> 우선순위 큐 사용
hq = []
heappush(hq, time[0][1])  # 첫번째 강의가 끝나는 시간를 heap에 넣는다

for i in range(1, n):
    if hq[0] <= time[i][0]:
        heappop(hq)
        heappush(hq, time[i][1])
    else:
        heappush(hq, time[i][1])
print(len(hq))
