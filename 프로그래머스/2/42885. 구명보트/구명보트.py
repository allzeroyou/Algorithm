def solution(people, limit):
    boat = 0  # 구명보트 수

    # 투포인터 이용
    people.sort()  # 정렬 필수
    # 시작
    first = 0
    # 끝
    last = len(people) - 1

    while first < last:
        if people[first] + people[last] <= limit:
            boat += 1  # 구명보트 탑승 가능
            first += 1
        last -= 1

    return len(people) - boat