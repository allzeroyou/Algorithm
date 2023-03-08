def solution(absolutes, signs):
    answer = 0
    # 절댓값을 차례대로 담은 정수 배열-absolutes
    # 정수들의 부호를 차례대로 담은 불리언 배열-signs
    # 실제 정수들의 합을 구해 return
    for j in range(len(signs)):
        if signs[j] == False:  # 거짓이라면 = 음수라면
            absolutes[j] *= -1
    # 다른 사람의 풀이
    # sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
    # zip을 사용한 for문.
    # [(3, true), (1, false), (5, true)] 처럼 될것.
    # 두 리스트의 요소의 개수가 같으므로 zip으로 풀 수 있음.

    return sum(absolutes)
