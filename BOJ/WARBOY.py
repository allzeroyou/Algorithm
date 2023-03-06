# 가격 대비 성능 = 성능/ 가격
# 제품 가격 : a
# 제품 성능 :b
# WARBOY 가격 : c
# WARBOY의 성능?

a, b, c = map(int, input().split())

print(int(b/a*c*3))