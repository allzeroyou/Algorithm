n = int(input())

member = []

for i in range(n):
    age_name=input().split()
    member.append((int(age_name[0]), age_name[1])) # 튜플로 저장
# 정렬
member = sorted(member, key=lambda m: m[0] ) # key가 증가하는 순으로.
# 출력
for m in member:
    print(m[0], m[1])