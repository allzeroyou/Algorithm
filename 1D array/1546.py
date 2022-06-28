n = int(input())
grade=[]
grade = list(map(int, input().split()))
sum = 0
for j in grade:
    m = max(grade)
    j = (j/m)*100
    sum += j

print(f"{sum/n:.2f}")
# how to 리스트와 연결?

# 최댓값은 max 함수 쓰면 될 것 같고, replace ?