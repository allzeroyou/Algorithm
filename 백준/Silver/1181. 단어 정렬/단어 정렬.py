n = int(input())
word = [input() for _ in range(n)]

set_word = list(set(word))
# 길이가 짧은 것부터, 같으면 사전순으로
set_word.sort(key=lambda x: (len(x), x))
for sw in set_word:
    print(sw)
