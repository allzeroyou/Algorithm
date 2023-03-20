def solution(s):
    answer = ''
    # 문자열 s에는 공백 으로 구분된 숫자 저장.
    # 숫자 중 최솟값, 최댓값을 찾아
    # "min max"의 형태로 문자열을 반환
    lst = list(map(int, s.split()))

    # lst_sort=sorted(lst)
    # lst.sort()  # 드디어 sort() 쓰는 법을 깨우쳤다!
    # 굳이 정렬하지 않아도 min, max 메소드가 있다.

    return str(min(s)) + " " + str(max(s))
