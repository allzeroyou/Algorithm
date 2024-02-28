
a = input()
b = input()

# 부분 수열 중 가장 긴 것
cache = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:  # 현재 문자 같으면
            # 이전까지의 LCS 길이 +1
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:  # 같지 않을 경우에
            # 이전 행, 열에서 더 큰 값.
            cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
            
print(cache[-1][-1])  # 최장 공통 부분 수열 출력.
