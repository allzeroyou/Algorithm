# 1부터 연속적으로 번호 붙은 스위치
# 스위치: on/off
# 1: on, 0: off
# 학생 몇 명을 뽑아서 1이상, 스위치 개수 이후 자연수 나눠줌
# 학생들은 성별, 받은 수에 따라 스위치 조작

# 남: 스위치 번호가 자기가 받은 수의 배수 -> 스위치 상태 바꿈(on->off, off->on)
# 여: 자기가 받은 수의 같은 번호가 붙은 스위치를 중심으로 좌우 대칭+가장 많은 스위치를 포함하는 구간 찾아서 그 구간에 속한 스위치 상태 모두 바꿈.
# 이때 구간에 속한 스위치 개수는 항상 홀수임.

# 스위치 개수
n = int(input())
# 스위치 상태
on_off = list(map(int, input().split()))
# 학생 수
s_cnt = int(input())


def change(x):
    if on_off[x] == 0:
        on_off[x] = 1
    else:
        on_off[x] = 0


# 성별, 학생이 받은 수
# s_num = [list(map(int, input().split())) for _ in range(s_cnt)]

for st in range(s_cnt):
    sex, num = map(int, input().split())

    if sex == 1:  # 남
        for j in range(1, n + 1):
            if j % num == 0:  # 배수라면
                change(j - 1)
        # print(on_off)

    else:  # 여
        idx = num - 1  # index는 0부터 시작
        # 받은 숫자 바꿈
        change(idx)

        # 번호를 중심으로 좌우대칭. (<- 어캐 판단?)
        i = 1

        while num - i >= 1 and num + i <= n:
            if on_off[idx + i] == on_off[idx - i]:
                change(idx + i)
                change(idx - i)
            else:
                break
            i += 1

# 스위치는 한 줄에 20개씩 출력. 21번째 스위치는 둘째 줄 맨 앞에 있어야 함.
for i in range(n):
    print(on_off[i], end=' ')

    if (i + 1) % 20 == 0:
        print()

# for o in on_off:
#     print(o)
