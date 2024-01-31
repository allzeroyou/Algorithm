'''
첫째줄에 떡의 개수 N, 떡의 길이 M
둘째줄에 떡의 개별 높이 주어짐
이때, 떡 높이의 총합은 항상 M 이상

적어도 M 만큼의 떡을 집에 가져가기위해 절단기에 설정할 수 있는 높이의 최댓값을 출력
'''

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

# 이진탐색
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid=(start+end)//2
    for x in array:
        # 잘랐을때의 떡의 양 계산
        if x>mid:
            total += x-mid
    if total < m:
        end =mid-1
    else:
        result = mid
        start = mid+1
# 정답 출력
print(result)