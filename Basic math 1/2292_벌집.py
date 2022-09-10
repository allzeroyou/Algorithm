n = int(input())
limit=1_000_000_000

cnt = 1
six_list = 0

if n==1:
    print(1)
else:
    for i in range(1, limit):
        six_list=six_list+(i*6) # 0+6, # 12+6=18
        cnt = cnt+1 # 2, 3
        if n <= six_list+1: # 7, 19
            print(cnt)
            break

'''
1, 6, 12, 18, 24, ... -> 6의 배수로 증가
1: 1
6: [2,3,4,5,6,7]
12: [8,9,10,11,12,13,14,15,16,17,18,19]
# n이 어디에 속하는지(6의 몇번째 배수?) 구해 -> 인덱스 출력
'''