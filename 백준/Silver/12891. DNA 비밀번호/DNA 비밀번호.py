
from collections import deque

# dna 문자열 길이, 부분문자열 길이
s, p = map(int, input().split())

# 임의로 만든 dna
dna = list(str(input()))

# ACGT 최소 횟수
A, C, G, T = map(int, input().split())
# 갯수 저장
acid = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# 3차 시도) 부분문자열 -> 범위(window)가 유지되므로 -> 슬라이딩 윈도우 기법 이용

# 슬라이딩 윈도우 이용(맨 왼쪽, 맨 오른쪽)
left, right = 0, p - 1
# 순회할 배열 만들기(덱 사용)
q = deque(dna[left:right])

# 개수 세기
for a in q:
    acid[a] += 1
# 답
ans = 0

while right < s:
    # 첫 윈도우 설정(다음부터는 구간 이동)
    acid[dna[right]] += 1
    if acid['A'] >= A and acid['C'] >= C and acid['G'] >= G and acid['T'] >= T:
        ans += 1
    # 구간이동
    acid[dna[left]] -= 1  # 왼쪽 요소 제거
    left += 1
    right += 1
print(ans)