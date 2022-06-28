import sys
c = int(sys.stdin.readline())           # 케이스 입력

for i in range(c):                      # 케이스 만큼 돌면서
    grade = list(map(int, input().split())) # 학생의 수, 점수 입력해서 grade에 저장
    num=grade[0] # 이때 점수의 평균을 구하기 위해, 학생의 수는 제거하기 전 num에 저장
    del grade[0] # 학생의 수 제거
    sum = 0 # sum 값 초기화
    for j in grade: # grade를 돌면서 평균을 구하기 위한 점수의 총 합을 구한다.
        sum += j # 각 요소를 sum에 누적합
    aver = sum/num # 평균은 총 합/ 학생의 수

    aver_up = 0 # 평균을 넘는 학생의 수 초기화
    for m in grade: # grade를 돌면서
        if m > aver: # 평균을 넘는 점수는
            aver_up+=1 # 비율을 구하기 위해, 수를 누적합
    per = aver_up / num* 100 # 비율 계산
    print(f"{per:.3f}"+"%") # 소수점 셋째자리까지 출력

