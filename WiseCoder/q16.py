t = ('a', 'b', 'c')
# 튜플 값 변경 불가
# 리스트로 바꾸고 값 변경 후 다시 튜플로 변환
h = list(t)
h[0]='A'
t = tuple(h)
print(t)