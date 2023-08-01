s = input()
switch_cnt = 0

for i in range(len(s)-1):
  if s[i] != s[i+1]: # 뒤집기
    switch_cnt+=1
#print(switch_cnt//2)
# 홀수일때는 +1 해줘야 함
if switch_cnt %2 == 1:
  print(switch_cnt//2 + 1)
else:
  print(switch_cnt//2)