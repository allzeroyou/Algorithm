# dr: 북, 동, 남, 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# solution
def robotic_vacuum(ci, cj, dr):
  cnt = 0 # 청소한 칸
  
  while 1: # 벽이라면 종료
    # [1] 현재 위치를 청소
    arr[ci][cj]=2
    cnt +=1
    
    # [2] 왼쪽 방향부터 탐색
    flag = 1
    while flag==1:
      for i in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
        ni = ci + di[i]
        nj = cj + dj[i]
        if arr[ni][nj]==0: # 미청소 영역
          ci, cj, dr = ni, nj, i
          flag = 0
          break
      else: # 4방향 모두 미청소 영역 없음 -> 후진
        bi = ci - di[dr]
        bj = cj - dj[dr]
        if arr[bi][bj] ==1: # 벽
          return cnt
        else:
          ci, cj = bi, bj
  # -1 이라면 내부 로직이 이상하다는 의미
  return -1 
        
        
      
  

# 입력
n, m = map(int, input().split())
si, sj, dr = map(int, input().split()) # start i, start j, dr(direction) 설정
# 방
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = 0
print(robotic_vacuum(si, sj, dr))
