# 절단기에 높이(h)를 지정하면 줄지어진 떡을 한번에 절단
# 높이가 h보다 긴 떡은 h 위의 부분이 잘리고
# 낮은 떡은 잘리지 않음

# 높이가 19, 14, 10, 17cm인 떡
# 절단기 높이르 15cm로 지정하면 자른 뒤
# 떡의 높이는 4, 0, 0, 2 cm임.
# 즉 손님은 6cm 만큼의 길이를 가져감.

# 손님이 왔을때 요청한 총 길이가 m일때 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값?

# 떡의 개수 n, 떡의 길이 m
# 떡의 개별 높이가 주어짐.
# 떡 높이의 총합은 항상 m 이상, 필요한 양만큼 떡을 사갈 수 있음

n, m = map(int, input().split())
dduk_height_list = list(map(int, input().split()))

ans = 0


# 재귀 함수로 풀었음.
def binary_search(dduk_height_list, start, end):
    global ans
    slice_sum = 0
    if start > end:
        return None
    mid = (start + end) // 2  # 중간값
    for h in dduk_height_list:
        if h - mid >= 0:  # 높이가 더 길다면
            slice_sum += (h - mid)
    if slice_sum >= m:  # 자른 떡의 합이 요청한 떡의 길이보다 길다면
        ans = mid
        return binary_search(dduk_height_list, mid + 1, end)  # 중간값 이후부터 탐색
    else:
        return binary_search(dduk_height_list, start, mid - 1)  # 중간값 이전까지 탐색.


binary_search(dduk_height_list, 0, max(dduk_height_list))
print(ans)

# 입력
'''
4 6
19 15 10 17
'''

# 출력
'''
15
'''
