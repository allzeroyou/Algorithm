import math

a,b,v = map(int, input().split())
day = math.ceil((v-a)/(a-b))+1 # 나무 정상에 도달하면 떨어지지 않음
print(day)