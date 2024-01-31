n1, n2 = list(map(str, input().split()))

re_n1 = int(n1[::-1])
re_n2 = int(n2[::-1])

if re_n1 > re_n2:
    n1 = str(re_n1)
    print(n1)
else:
    n2 = str(re_n2)
    print(n2)
