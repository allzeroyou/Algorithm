import sys

input = sys.stdin.readline

# 모험가 N명
# 모험가 길드 : N명의 모험가를 대상으로 공포도 측정
# 공포도가 X인 모험가 -> 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야

# 모험가 그룹 최댓수 출력

N = int(input())
fear = list(map(int, input().split()))
fear.sort()  # 오름차순 정렬

cnt = 0  # 팀 수
member = 0  # 팀원 수
for i in fear:
    member += 1
    if i <= member: # 앞에서부터 확인해 현재 공포도 <= 팀원 수이면 팀 결성.
        cnt += 1
        member = 0  # 팀원수 초기화
print(cnt)

'''
5
2 3 1 2 2
'''
