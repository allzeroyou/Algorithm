# 알파벳 소문자로 이뤄진 단어
# 먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갬
# 주어진 단어를 3개의 더 작은 단어로 나눔.
# 각각은 적어도 길이가 1이상인 단어여야 함.
# 나눈 3개의 단어들을 앞뒤로 뒤집고 이를 다시 원래의 순서대로 합침.
# 만든 단어 중 사전순으로 가장 앞서는 단어

word = list(input())
# 임시 저장할 단어
tmp = []

# 단어에서 3부분으로 자른다.
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        left = word[:i]
        mid = word[i:j]
        right = word[j:]
        # 뒤집기
        left.reverse()
        mid.reverse()
        right.reverse()
        tmp.append(left + mid + right)

# 정답
ans = []
for t in tmp:
    ans.append("".join(t))

# 사전순으로 가장 앞서는 단어.
print(sorted(ans)[0])
