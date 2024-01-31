array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1  # 피벗값 제외, 피벗값 옆의 오른쪽 방향으로 가장 왼쪽 요소를 left 설정
    right = end  # 가장 오른쪽을 right 으로 설정

    while (left <= right):
        # 왼쪽) 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 오른쪽) 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):  # left와 right의 값이 엇갈렸다면(left> right 이라면) 작은 데이터와 피벗값의 위치 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 작은 데이터와 피벗값 교체 이후, 피벗값 왼쪽 데이터는 모두 피벗보다 작고 오른쪽 데이터는 모두 피벗보다 큼
    # 이렇게 피벗을 기준으로 데이터묶음을 나누는 작업을 분할이라고 함
    # 따라서 분할 이후 왼쪽 부분과 오른쪽 부분에서 다시 각각 정렬 수행(재귀)
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
