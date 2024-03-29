'''
문제 설명
한 마을에 모험가 N명이 있음.
모험가 길드에서는 N명의 모험가를 대상으로 '공포도' 측정
공포도가 높은 모험가는 위험 상황에서 대처 능력 저하
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 하도록 규정함

최대 몇개의 모험가 그룹(최댓값)을 만들 수 있을까?
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

res = 0                 # 총 그룹의 수
cnt = 0                 # 현재 그룹에 포함된 포함가의 수

for i in range(n):      # 공포도를 낮은 것부터 하나씩 확인
    cnt += 1            # 현재 그룹에 해당 모험가 포함시키기
    if cnt >= i:        # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면.. 그룹 결성
        res += 1        # 총 그룹의 수 증가시키기
        cnt = 0         # 현재 그룹에 포함된 모험가의 수 초기화
print(res)              # 총 그룹의 수 출력


'''
문제 해결 아이디어
오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인
앞에서부터 공포도를 하나씩 확인하며 
'현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도' 보다 크거나 같다면 이를 그룹으로 설정!

이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점 -> 항상 최소한의 모험가의 수만 포함해 그룹 결성
'''