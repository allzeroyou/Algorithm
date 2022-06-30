def print_max():
    num = list(map(int, input().split()))
    max=0
    for i in num:
        if max < i:
            max=i
    print(max)

print_max()