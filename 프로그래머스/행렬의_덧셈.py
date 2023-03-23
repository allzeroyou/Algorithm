def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])): # 각 행렬 안에 접근.
            arr1[i][j] += arr2[i][j]

    return arr1


print(solution([[1],[2]],[[3],[4]]))
