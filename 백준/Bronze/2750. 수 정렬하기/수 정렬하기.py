n = int(input())
number = [int(input()) for _ in range(n)]
number.sort()
for num in number:
    print(num)
