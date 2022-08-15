N = int(input())

list = []
count = 0
for i in range(N):
    giho = int(input())
    list.append(giho)
dasom = list[0]
not_dasom = sorted(list[1:], reverse=True) # 후보군의 투표수 내림차순

if N==1:
    print(0)
else:
    for i in not_dasom:
        if dasom==i: # 후보군의 투표수와 동일할때는 1개만 얻어도 승리
            print(1)
            break

        while(not_dasom[0] >= dasom): # 다솜이의 투표수가 많을때까지
            count += 1
            not_dasom[0] -= 1
            dasom += 1

            not_dasom = sorted(not_dasom, reverse=True) # 최댓값 갱신

        print(count)
        break
