# 전공평점 3.3 이상이어야 함
# 전공평점: (학점 x 과목평점)의 합을 학점의 총합으로 나눈 값.
grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
res = 0.0  # 전공평점
total = 0.0  # 학점총합

# 과목명, 학점, 등급
for _ in range(20):
    a, b, c = input().split()
    if c == 'P':
        continue

    res += float(b) * grade[c]
    total += float(b)

try:
    print('{:.6f}'.format(float(res / total)))
except:
    print('{:.6f}'.format(0.0))
