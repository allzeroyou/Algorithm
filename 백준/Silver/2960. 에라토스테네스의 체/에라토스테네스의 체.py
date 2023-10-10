import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0  # 순서 카운트

# 2부터 n 까지
lst = [i for i in range(2, n + 1)]

while lst:
    min_num = lst[0]
    baesu_lst = []

    for j in range(len(lst)):
        if lst[j] % lst[0] == 0: # p의 배수라면
            baesu_lst.append(lst[j])
            cnt += 1
            if cnt == k:
                print(lst[j])
                break # for문 탈출
    if cnt == k:
        break # while 탈출
    # lst - baesu lst
    lst = [x for x in lst if x not in baesu_lst]



