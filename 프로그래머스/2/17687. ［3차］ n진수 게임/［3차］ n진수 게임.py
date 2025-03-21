# n진수 게임
# 10이상의 숫자는 한자리씩 끊어서 말함.
# 예제1
# n=2진법, 4개, 2명, 튜브는 1번
# 0, 1, 10, 11, 100, ...
# 참가인원이 2명이므로 -> 튜브, 상대방, 튜브, 상대방, .. 순서임
# 따라서 튜브 -> 0, 2, 4, 6 ..에 해당하는 숫자 가져옴
# 0+1+1+1-> 0111

# 예제2
# n=16진법, 16개, 2명, 1번째
# 0~9, A, B, C, D, E, F, 10, 11, ..
# 튜브는 0, 2, 4, 6..에 해당하는 숫자
# 0+2+4+6+8,..


def solution(n, t, m, p): # n: 진법, t: 미리 구할 숫자 개수, m: 게임 인원 수, p: 튜브 순서
    answer = ''
    # 게임에 필요한 숫자를 진법변환한 문자열
    total = ''
    # 0~n까지 수행
    number = 0
    
    # t*m 길이만큼 숫자 변환
    while len(total)< t*m:
        total += change(number, n)
        number+=1
    # 튜브의 순서에 맞는 숫자만 추출
    for i in range(t):
        # 튜브 순서-1: 인덱스화 + turn 횟수 구하기(4개 숫자 구할때 0, 2, 4, 6)
        answer += total[(p-1)+ i*m]
        
    
    return answer

# 진법 변환 함수-> 파이썬 진법 변환 함수 있지만, 3진수, 5진수로도 변환해야 하므로 함수 정의
def change(number, n): # 바꿀 숫자, 진법
    # 11진법부터는 숫자 + 문자 필요함
    chars = "0123456789ABCDEF" # (= 16진법에서, 10: a, 11: b, 12: c, 13:d, 14: e, 15:f)
    
    # 숫자가 0이라면, 모든 진법에서 '0'임
    if number == 0:
        return '0'
    
    res = "" 
    while number > 0:
        res = chars[number%n] + res # 진법 변환
        number //= n 
    return res
        
    