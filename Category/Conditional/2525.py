hour, min = map(int, input().split())
cooking = int(input())
# hour = int(hour)
# min = int(min)

min = min+cooking
add_hour = 0

if min > 59:
    add_hour = min // 60
    min = min%60
hour += add_hour
hour = hour % 24
print(hour, min)