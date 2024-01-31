def solution(L, x):
    for i in range(len(L)):
        if x <= L[i]:
            L.insert(i, x)  # index, value
            break
        elif x > L[i] and i != len(L) - 1: # 제일 마지막 원소가 아닐때
            continue
        elif i == len(L) - 1: # 제일 마지막 원소까지 왔다면, 리스트의 원소들 보다 더 큰 수임.
            L.insert(i + 1, x)
            break
    answer = L

    return answer


res = solution([20, 37, 58, 72, 91], 100)
print(res)
