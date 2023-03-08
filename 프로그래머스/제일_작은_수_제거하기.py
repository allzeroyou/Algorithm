# 정수 배열 arr
# 가장 작은 수 제거 -> 배열리턴
# 리턴하려는 배열이 빈 배열 -> 배열에 -1을 채워 리턴
# https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 테스트 불통ㅡ 다시 풀어야됨.

def solution(arr):
    answer = []

    arr= sorted(arr, reverse=True)
    del arr[len(arr)-1]

    print(arr)
    if len(arr)==0:
        arr=-1

    return arr
solution([4,3,2,1])