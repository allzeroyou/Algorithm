
def solution(L, x):
    left = 0
    right = len(L)-1

    while (left <= right):
        mid = (left + right) // 2

        # 중간값과 타겟이 같은 경우 종료
        if L[mid] == x:
            return mid

        # 중간값이 타겟보다 큰 경우
        elif L[mid] > x:
            right = mid - 1
        # 중간값이 타겟보다 작은 경우
        else:
            left = mid + 1
    return -1



# def solution(L, x):
#     #left = L.index(L[0]) # 찾지 못하면 인덱스에러 발생.
#     #right = L.index(L[-1])
#
#     left=0 # 따라서 대입필요.
#     right=len(L)-1
#
#     while (left <= right):
#         mid = (left + right) // 2
#
#         # 중간값과 타겟이 같은 경우 종료
#         if L[mid] == x:
#             return mid
#         # 중간값이 타겟보다 작은 경우
#         elif L[mid] < x:
#             left = mid + 1
#         # 중간값이 타겟보다 작은 경우
#         else:
#             right = mid - 1
#     return -1

res=solution([2, 5, 7, 9, 11], 4)
res2=solution(	[], 3)
print(res,res2)
