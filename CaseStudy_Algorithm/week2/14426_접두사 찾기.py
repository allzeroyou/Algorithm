prefixes = set()
N, M = map(int, input().split())

for _ in range(N):
    word = input()

    for i in range(1, len(word) + 1):
        prefixes.add(word[:i])

print(sum(1 for _ in range(M) if input() in prefixes))