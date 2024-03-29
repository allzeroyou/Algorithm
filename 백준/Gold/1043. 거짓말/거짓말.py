# 파이썬 집합 연산
# 합집합: union,|
# 교집합: intersection, &
# 차집합: difference, -
# https://ctkim.tistory.com/entry/Python-%EC%9E%85%EB%AC%B8-%EA%B0%95%EC%A2%8C-12-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%91%ED%95%A9Set-%EC%A0%95%EB%A6%AC-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95


# 사람 수, 파티 수
n, m = map(int, input().split())
# 진실 아는 사람 수, 번호 -> 개수는 상관없으니까 번호만 저장
knows = set(input().split()[1:])
# 파티 수, 번호
parties = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        # 파티원 중 진실아는 사람이 있다면
        if party.intersection(knows):
            knows = knows.union(party)
cnt = 0
for party in parties:
    if party & knows:
        continue
    cnt += 1
print(cnt)
