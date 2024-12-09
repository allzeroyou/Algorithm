# 줄 세우기
# 오름차순 20명

tc = int(input())

for t in range(1, tc + 1):
    ipt = list(map(int, input().split()))
    student = ipt[1:]

    # 뒤로 간 학생들 카운트
    cnt = 0
    for i in range(19):
        for j in range(i + 1, 20):
            if student[i] > student[j]:  # 현재 있는 애가 더 크다면
                cnt += 1
                student[i], student[j] = student[j], student[i]

    print(f'{t} {cnt}')
