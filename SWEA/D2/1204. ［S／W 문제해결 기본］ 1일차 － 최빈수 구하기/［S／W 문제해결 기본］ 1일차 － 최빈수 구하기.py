t = int(input())

for tc in range(1, t + 1):
    num = int(input())  # 테스트 케이스 번호
    scores = list(map(int, input().split()))
    dic = {}

    for score in scores:
        if score in dic:
            dic[score] += 1
        else:
            dic[score] = 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    print(f'#{tc} {dic[0][0]}')
