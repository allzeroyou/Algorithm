# 배열 arr의 원소는 0~9 숫자
# 이때 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거.
# 제거된 후 남은 수 반환시 배열 arr의 원소 순서들은 유지해야 함

def solution(arr):
    answer = []

    num = -1
    for i in arr:
        if num != i: # 같지 않다면 answer 에 추가한다는 생각이 대단.
            num = i
            answer.append(i)

    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
# arr = [4, 4, 4, 3, 3]
print(solution(arr))
