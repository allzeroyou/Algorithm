def make_table(p):
    global table

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j

def kmp(t, p):
    answer = []
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = table[j-1]

        if t[i] == p[j]:
            if j == len(p) - 1:
                answer.append(i - len(p) + 2)
                j = table[j]
            else:
                j += 1
    return answer

T = list(input())
P = list(input())

table = [0] * len(P)
make_table(P)
answer = kmp(T, P)
print(len(answer))
print(*answer)