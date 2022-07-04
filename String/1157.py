word = input().upper()
set_word = list(set(word))
cnt = []
for _ in set_word:
    count = word.count
    cnt.append(count(_))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(set_word[(cnt.index(max(cnt)))])
