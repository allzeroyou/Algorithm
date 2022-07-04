case = int(input())

for i in range(case):
    n, word = map(str, input().split())
    banbok = int(n)
    for _ in range(len(word)):
        print(word[_] * banbok, end='')

    print()
