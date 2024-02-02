def solution(name):
    answer = 0
    min_move = float('inf')  # 무한대로 초기화하여 어떤 값보다 큰 값으로 설정
    next = 0

    for i, char in enumerate(name):
        # 두 가지 방향에서 최솟값 고려
        # 1. 상 하 관점 / 2. 좌 우 관점

        # 1. 상 하 관점
        # A부터 오름차순으로 char 찾는게 빠른지
        # Z부터 내림차순으로 char 찾는게 빠른지 비교
        # Z의 경우 A에서 커서 왼쪽으로 이동 시,
        # 횟수 1 늘어나기 때문에 +1 주의
        # ABCDEFGHIJKLMNOPQRSTUVWXYZ 참고
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 2. 좌 우 관점
        # 제일 긴 A구간을 찾기 위해 for문으로 반복하는 것!
        # 최종 next : '연속된' A구간의 마지막 A 인덱스를 나타냄
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # min(기존, 연속된 A기준 왼쪽 2번 탐색, 연속된 A기준 오른쪽 2번 탐색)
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    answer += min_move
    return answer
