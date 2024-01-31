# 자릿수를 기준으로 점수를 N으로 나눠 왼쪽 부분의 각 자릿수 합 + 오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황

N = input()
n_len = len(N)
half = n_len / 2
left_sum = 0

# 아래코드를 [half:] 처럼 python slice를 이용해 풀어보기

for i in range(len(N)):
    if i == half:
        break
    left_sum += int(N[i])

right_sum = 0
for j in range(len(N)):
    if j >= half:
        right_sum += int(N[j])

if right_sum == left_sum:
    print("LUCKY")
else:
    print("READY")

'''
123402
7755
'''
