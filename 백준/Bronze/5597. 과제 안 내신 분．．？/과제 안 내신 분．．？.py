# 30명 중 28명만 제출
# 제출 안한 2명의 출석번호 구하기

s = [x for x in range(1, 31)]

for _ in range(28):
    n = int(input())
    if n in s:
        s.remove(n)
for i in s:
    print(i)
