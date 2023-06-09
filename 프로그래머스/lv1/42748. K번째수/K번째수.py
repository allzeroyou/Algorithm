def solution(array, commands):
    # array의 i번째 숫자부터 j번재 숫자까지 자르고 정렬할 때 k번째 있는 수?
    answer = []

    for command in commands:
        print(f'command : {command}')
        i = command[0]
        j = command[1]
        k = command[2]
        array_sliced = array[i - 1:j]
        array_sliced.sort()
        print(f'array {array_sliced}')

        try:
            answer.append(array_sliced[k - 1])

        except:
            answer.append(array_sliced[0])
    return answer