num = int(input())  # 약수 개수
# 약수
lst = list(map(int, input().split()))
print(min(lst) * max(lst))