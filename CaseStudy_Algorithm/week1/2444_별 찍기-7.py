N = int(input())

for i in range(1, N + 1):
    if i == N:
        break
    else:
        print(" " * (N - i) + "*" * (2 * i - 1))

for i in range(1, N + 1):
    print(" " * (i - 1) +"*" * (2 * N - i * 2 + 1))