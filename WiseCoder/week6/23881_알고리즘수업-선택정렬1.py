'''
선택 정렬 수업 조교 서준이

N개의 서로 다른 양의 정수가 저장된 배열 A
선택 정렬로 배열 A를 오름차순 정렬할 경우 k번째 교환되는 수를 구해서 서준이 도와주기

배열 A의 크기 N
교환횟수 K
서로 다른 배열 A의 원소(A1, A2..An)
'''
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
        # print(arr)
        if cnt == k:
            res = f'{arr[max_idx]} {arr[i]}'
    return res

print(selection_sort(arr, k))