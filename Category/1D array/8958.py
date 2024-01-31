import sys
case = int(sys.stdin.readline().rstrip()) # 경우 입력받기

for i in range(case):   # 경우 만큼 반복문 돌기
    ox = sys.stdin.readline().rstrip()            # ox 입력
    list(ox)                # 입력받은 통째로의 ox를 비교를 위해 한 문자씩 쪼갠다
    sum = 0                 # 한번의 테스트 케이스를 돈 후에 합 초기화
    o_sum = 0               # 한번의 테스트 케이스를 돈 후에 o의 합 초기화
    for j in ox:            # 각각의 o와 x를 돈다
        if j == 'O':        # 만약 o일 경우
            o_sum += 1      # o의 누적합
            sum += o_sum    # 총 합
        else:               # 만약 x일 경우
            o_sum = 0       # o의 누적합 초기화
    print(sum)              # 총 합 출력
