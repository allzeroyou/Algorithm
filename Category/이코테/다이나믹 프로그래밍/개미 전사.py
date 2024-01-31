n = int(input())
eat_thing = list(map(int, input().split()))

# dp 테이블
d = [0] * (n + 1)

d[0] = eat_thing[0]
d[1] = max(eat_thing[0], eat_thing[1])

for i in range(2, n):  # range가 n-1까지의 범위
    d[i] = max(d[i - 1], d[i - 2] + eat_thing[i])
    # 개미전사가 위치한 칸과 i-2 칸을 더한게 더 많은 식량인지, 이번 칸은 스킵하고 i-1칸을 선택하는게 더 많은 식량?
print(d[n-1])
# 왜 d[n-1]이지?
# 끝 index는 n-1의 값임.

'''
4
1 3 1 5
'''
