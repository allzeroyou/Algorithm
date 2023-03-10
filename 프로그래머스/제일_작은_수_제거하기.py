# 정수 배열 arr
# 가장 작은 수 제거 -> 배열리턴
# 리턴하려는 배열이 빈 배열 -> 배열에 -1을 채워 리턴
# https://school.programmers.co.kr/learn/courses/30/lessons/12935


def solution(arr):
    answer = []

    # answer= sorted(arr, reverse=True)
    # del answer[len(arr)-1]
    # print(arr)

    if len(answer)==0:
        answer=-1
        return answer

    answer = len(arr) - 1
    min = answer[0]

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    index = 0
    for i in range(len(arr)):
        if arr[i] == min:
            continue
        answer[i] = arr[i]
    return answer



solution([1,3,2,1])