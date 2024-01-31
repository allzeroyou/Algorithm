n = int(input())
check = False
for i in range(1, n+1):
    temp = list(map(int, str(i)))
    if i + sum(temp) == n:
        print(i)
        check = True
        break
if check==False:
    print('0')




