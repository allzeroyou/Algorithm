array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)): # 선형 탐색 수행, 가장 작은 원소 찾기
        if array[min_index] > array[j]: # 만약 j보다 가장 작은 원소의 인덱스가 크다면
            min_index = j               # 가장 작은 원소의 인덱스에 j를 대입
    array[i], array[min_index] = array[min_index], array[i] # 스와프, 파이썬에서는 별도의 라이브러리 필요없이 변수 스와핑 가능
print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]