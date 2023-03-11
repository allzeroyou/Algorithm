# 정수 배열 arr
# 가장 작은 수 제거 -> 배열리턴
# 리턴하려는 배열이 빈 배열 -> 배열에 -1을 채워 리턴
# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    # 실패 코드
    # answer= sorted(arr, reverse=True)
    # del answer[len(arr)-1]
    # print(arr)

    if len(answer)>1:
        arr.remove(min(arr)) # 리스트에서 최솟값 구하기: min() 함수.
        # 리스트에서 원소 제거: .remove() 함수
        return arr

    return [-1]

# print(solution([1,3,2,1]))