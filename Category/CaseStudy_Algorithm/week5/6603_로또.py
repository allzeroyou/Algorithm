from itertools import combinations
tc = 0
while True:
    k, *s = map(int, input().split())
    #  첫번째 입력받는 숫자만 k에 할당, 나머지는 s에 할당됨
    if k == 0:
        break
    if tc: # tc가 1이상
        print()
    for combi in combinations(s, 6):
        print(*combi) # 테스트 케이스 사이에 빈 한줄 넣기

    tc+=1