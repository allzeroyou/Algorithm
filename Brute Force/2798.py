'''
Brute Force 알고리즘
brute란 난폭한 이라는 뜻이고, force란 힘이라는 뜻으로 둘을 합치면 난폭한 힘으로 해석이 된다.
즉, 모든 경우의 수를 탐색하면서 요구 조건에 충족되는 결과만 가져옴

알고리즘에 가장 큰 특징은 모든 영역을 전체 탐색하는 방법임
따라서 브루트 포스의 가장 큰 단점은 시간복잡도가 커진다는 것이다
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k]>m:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)