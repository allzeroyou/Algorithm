sugar = int(input())

if sugar/3 > sugar/5:
    if sugar%3 == 0 :
        if sugar//5 < sugar//3:
            big = (sugar // 5)
            small = (3 // big)
            print(big + small)
    else:
        big = (sugar//5)
        try:
            small = (3//big)
            print(big+small)
        except:
            print(-1)
# 그리드로 푸는 방식인가..