def solution(price, money, count):
    # price 이지만, 놀이기구 N번 이용시 이용료의 N배
    # 처음 이용료: 100->200->300
    # count번 탑승 시 현재 가지고 있는 금액에서 얼마 모자름?
    # 금액 부족하지 않다면 0 return
    ans = 0
    for i in range(1, count + 1):
        ans += price * i
    if money >= ans:
        answer = 0
        return answer
    else:
        return ans - money