def solution(citations):
    answer = 0
    # index가 인용 횟수인 리스트 생성
    res = [0] * (max(citations) + 1)
    # 인용 횟수가 c번인 논문의 개수 확인
    for c in range(max(citations) + 1):
        cnt = 0
        for i in citations:
            if i >= c:
                cnt += 1
        res[c] = cnt
    for idx, val in enumerate(res):
        if idx <= val:
            answer = idx
    return answer