import sys

n, k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

def selection_sort(arr, k):
    cnt = 0
    res = -1
    for i in range(n-1, 0, -1): # 4, 3, 2, 1
        max_idx = i
        for j in range(i-1, -1, -1): # 3, 2, 1, 0
            if arr[j] > arr[max_idx]:
                max_idx=j
        if arr[max_idx] != arr[i]:
            arr[max_idx], arr[i] = arr[i], arr[max_idx]
            cnt +=1

        if cnt == k:
            res = ' '.join(str(_) for _ in arr)
            break
    return res

print(selection_sort(arr, k))