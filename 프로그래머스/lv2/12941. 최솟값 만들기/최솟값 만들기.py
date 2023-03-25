def solution(A,B):
    answer = 0

    lst = []

    A = sorted(A)  # [1,2,4]

    B = sorted(B, reverse=True)  # [5,4,4]

    for i in range(len(A)):
        lst = A[i] * B[i]
        answer += lst

    return answer