one = input("첫 번째 문자열: ")
two = input("두 번째 문자열: ")

one_sp = one.split()
print(one_sp)
two_sp = two.split()
print(two_sp)

if len(one) > len(two):
    for i in one_sp:
        for j in two_sp:
            if i == j :
             print(i)
else:
    for k in two_sp:
        for l in one_sp:
            if k == l:
                print(k)
