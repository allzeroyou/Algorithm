a, b, c = list(map(int, input().split()))

if c-b <=0 :
    print('-1')
else:
    res = a/(c-b)
    res = res+1
    print(int(res))