def solution(n):
    # 정수 n을 매개변수로 입력 -> n의 각 자릿수 큰 것 -> 작은 순으로 정렬한 새로운 정수 리턴.
    # n이 118372 -> 873211 리턴.

    n_list = list(str(n))
    # sort 이용
    n_list.sort(reverse=True)
    # sorted 이용
    # return int("".join(sorted(n_list, reverse=True)))
    return int("".join(n_list))

    #$return sorted(n_list, reverse=True).

print(solution(118372))