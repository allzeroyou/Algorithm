def solution(numbers):
    # 0~9까지 숫자중 일부가 들어있는 배열.
    onetoten = []

    for i in range(10):
        onetoten.append(i)

    # 배열끼리 빼기
    # 순서가 상관없다면, 집합은 뺄셈 가능
    lst = (list(set(onetoten) - set(numbers)))

    # 다른 사람의 풀이
    # 45-sum(numbers) # 와우..

    return sum(lst)