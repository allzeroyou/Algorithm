# 자기 앞, 뒤 숫자 사용

def solution(n, lost, reserve):
    # 체육복 빌릴 수 있는 사람 개수
    answer = 0


    # 도난 당한 학생이 여분 가져온 경우를 제외 -> set 형식으로 변경헤준 뒤 차집합 구함.
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    # 순서 정렬 필요(체육복 최대한 빌려주는 경우만 고려)
    lost.sort()
    reserve.sort()

    # 자기 앞, 뒤 숫자
    around = []
    # 체육복 잃은 학생
    for l in lost:
        # 앞/뒤 번호 구하기
        around.append((l - 1, l + 1))
    # 여분 체육복
    for r in reserve:  # 1
        for num in around:  # [(1, 3), (3, 5)]
            if r in num:  # 튜플이므로 in 연산자 사용
                answer += 1
                around.remove(num)
                break

    lost_stu = len(lost)
    # print(n - lost_stu + answer)

    return n - lost_stu + answer