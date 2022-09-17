n = int(input())
requests = list(map(int, input().split())) # 예산 요청
budget = int(input()) # 총 예산

def calc_budget(upper_bound: int)->int:
    # 상한액이 boundary일때 필요한 예산을 계산하는 함수
    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)
    return needed_budget

# 이분 탐색 수행하는 메인 로직
low = 0
high = max(requests)
correct_upper_bound = -1 # False

while low <= high:
    mid = (low + high)//2
    if calc_budget(mid)<=budget:
        correct_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1
answer = -1
for request in requests:
    given = min(request, correct_upper_bound)
    answer = max(answer, given)
print(answer)
