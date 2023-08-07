def counting_star(a:list):
  ans = []
  for i in range(3 * len(a)):
    if (i//len(a)==1):
      ans.append(a[i%len(a)]+" "*len(a)+a[i%len(a)])
    else:
      ans.append(a[i%len(a)]*3)
  return ans
  
# 기본형 -> 3의 패턴
star = ["***", "* *", "***"]

n = int(input())
cnt = 0

while n!=3:
  n = n//3
  cnt += 1
# cnt 값을 통해 재귀함수의 횟수 결정
for i in range(cnt):
  star =  counting_star(star)
  
for s in star:
  print(s)