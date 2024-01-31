# n = int(input())
# testcase = [] # 입력받은 층 수, 호 수를 바탕으로 생성할 배열
# answer = [] # 답 저장할 배열
#
# for i in range(n):
#     a = int(input())
#     b = int(input())
#     testcase.append([a, b])
#
# for test in testcase:
#     floor=test[0] # a
#     room = test[1] # b
#     apt = [[i for i in range(1, 15)]] # 각 층은 14호까지까지 있으며, 입력된 층까지만 배열 만들기
#     for i in range(floor+1): # apt의 각 층의 1호는 전부 1명이 거주
#         apt[i][0] = 1
#     for i in range(1, floor+1):
#         for j in range(1, room):
#             apt[i][j] = apt[i-1][j] + apt[i][j-1]
#     answer.append(apt[floor][room-1])
#
# for a in answer:
#     print(a)
################################
'''
case = int(input())

for i in range(case):
    f = int(input()) # floor
    r = int(input()) # room

    valueset = [x for x in range(1, r+1)] # 0층

    for k in range(f): # 층 수 만큼 반복
        for j in range(1, r): # 1~r-1까지, 인덱스로 사용
            valueset[j] += valueset[j-1] # 층별 각 호실의 사람수를 변경
        print(valueset)
    print(valueset[-1]) # 가장 마지막 수 출력
'''
#################################

lst = [[0 for j in range(14)] for i in range(15)]
# 리스트 컴프리헨션으로 다중 for문 만들기
for i in range(15):
    lst[i][0] = 1
for h in range(14):
    lst[0][h] = h+1
for i in range(1, 15):
    for j in range(1, 14):
        lst[i][j] = lst[i][j-1] + lst[i-1][j]
test_case = int(input())

for i in range(test_case):
    k = int(input())
    n = int(input())
    print(lst[k][n-1])


