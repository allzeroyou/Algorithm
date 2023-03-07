def solution(arr, divisor):
    answer = []
    cnt = 0
    # array의 각 요소중 divisor로 나눠 떨어지는 값 -> 오름차순으로 정렬한 배열 반환.
    # 각 요소 중 나눠떨어지는 값이 하나도 없으면 배열에 -1을 담아 리턴.
    for i in arr:
        if (i % divisor == 0):
            answer.append(i)
            cnt += 1
    if cnt == 0:
        answer.append(-1)
    return sorted(answer)

# 다른 사람의 풀이

# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
