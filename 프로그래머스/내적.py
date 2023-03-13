def solution(a, b):
    answer = 0
    # 배열 a와 b의 내적

    for i in range(len(a)):
        cnt = i
        for j in range(len(b)):
            if cnt == j:
                answer += (a[i] * b[j])
                break

    # 다른 사람의 풀이-zip 함수
    # sum([x*y for x, y in zip(a,b)])

    return answer
# print(solution([1,2,3,4], [-3,-1,0,2]))
# print(solution([-1,0,1], [1,0,-1]))
