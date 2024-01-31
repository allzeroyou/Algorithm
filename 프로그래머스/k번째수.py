def solution(array, commands):
    # array의 i번째 숫자부터 j번재 숫자까지 자르고 정렬할 때 k번째 있는 수?
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        # i,j,k=command         #로 최적화 가능
        array_sliced = array[i - 1:j]
        array_sliced.sort()

        try:
            answer.append(array_sliced[k - 1])

        except:
            answer.append(array_sliced[0])
        # 위 두줄을
        # answer.append(sorted(array[i-1,j])[k-1]) #로 최적화 가능
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
