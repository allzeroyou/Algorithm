def solution(arr):
    answer = []

    num = -1
    for i in arr:
        if num != i:
            num = i
            answer.append(i)

    return answer