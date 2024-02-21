# 오븐
# 요리 시작 시각, 요리하는 시간 --> 요리 끝나는 시각?

h, m, s = map(int, input().split())
cooking_time = int(input())

# 모두 초로 변경
cooking_times = h * 3600 + m * 60 + s + cooking_time

# 초, 분, 시로 변경
s = cooking_times % 60
cooking_times //= 60
m = cooking_times % 60
h = cooking_times // 60

# 시간은 0~23시까지
h %= 24

print(h, m, s)
