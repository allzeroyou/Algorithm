# 각 자리가 숫자(0-9)로만 이뤄진 문자열 S
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자 확인 -> 숫자 사이에 x or + 연산자를 넣어 가장 큰 수를 만들자.


S = list(map(int, input()))

res = S[0]


for i in range(len(S)-1): # i+1 사용 -> 마지막 앞까지 탐색
    if S[i] <= 1: # 1 이하라면 더하는 것이 이득
        res += S[i+1]
    else:
        res *= S[i+1]
print(res)

'''
02984
567
'''