# 세로 읽기-행 증가, 열 일정
# 다섯줄 입력
words = ['-1' * 15 for _ in range(5)]  # 2차원 배열 생성

for i in range(5):
    words[i] = input()

word_len = [len(word) for word in words]
leng = max(word_len)

ans = []
for i in range(leng):
    for j in range(5):
        try:
            ans.append(str(words[j][i]))
        except IndexError:
            continue

res = ''.join(ans)
print(res.replace(' ', ''))
