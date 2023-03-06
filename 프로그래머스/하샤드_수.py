def solution(x):
    # 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나눠져야 함.
    # e.g 18의 자릿수의 합 : 1 + 8 =9, 18은 9로 나눠 떨어짐. 18은 하샤드 수.
    answer = True
    hap = 0
    for i in str(x):
        hap += i
    if x % hap == 0:
        return answer
    else:
        return False
