def solution(A, B):
    answer = 0
    # 길이가 같은 배열 A,B 두개.
    # 각 배열은 자연수로 이뤄져 있음.
    # 배열 A,B에서 각각 한개의 숫자를 뽑아 두 수를 곱함.
    # 배열의 길이만큼 반복. 두 수를 곱한 값을 누적해서 더함
    # 최종적으로 누적된 값이 최소가 되도록.


    lst = []

    A = sorted(A)  # [1,2,4]

    B = sorted(B, reverse=True)  # [5,4,4]

    for i in range(len(A)):
        lst = A[i] * B[i]
        answer += lst

    return answer


print(solution([1, 4, 2], [5, 4, 4]))

# 와 1차 통과!
# 순수하게 짠 코드로 정확도랑 효율성 모두 통과라니 ><