import sys

input = sys.stdin.readline

# 0,1 로만 이뤄진 문자열 S
# S의 모든 숫자를 전부 같게 만드려 함
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집음.
# 1 -> 0, 0 -> 1 로
# 다솜이가 해야하는 행동의 최소 횟수

# 풀이방법
# 연속된 하나의 덩어리를 바꿔야 하는횟수로 본다.

S = list(map(int, input()))

cnt = 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:  # 해당 문자의 직전, 직후가 다르면, 덩어리 수 증가
        cnt += 1

print(cnt//2)