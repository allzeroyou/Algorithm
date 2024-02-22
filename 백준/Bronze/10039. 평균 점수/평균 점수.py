# 점수 40점 이상: 그대로
# 점수 40점 미만: 40점.


score = [int(input()) for _ in range(5)]

for i in range(5):
  if score[i]<40:
    score[i]=40

print(sum(score)//5)