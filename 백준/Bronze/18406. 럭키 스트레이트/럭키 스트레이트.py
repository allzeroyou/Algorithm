N = input()
n_len = len(N)
half = n_len / 2
left_sum = 0
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