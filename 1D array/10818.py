count = int(input())

data = list(map(int, input().split()))
i = 0
max = data[i]
min = data[i]
for i in range(len(data)):
    if data[i] > max:
        max=data[i]
    if data[i]<min:
        min=data[i]

print(min, max)