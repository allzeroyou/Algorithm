# 10
one = input("첫 번째 문자열: ")
two = input("두 번째 문자열: ")

one_sp = list(one)
print(one_sp)
two_sp = list(two)
print(two_sp)

list = []
if len(one) <= len(two):
    for k in two_sp:
        for l in one_sp:
            if k == l:
                list.append(k)
    new_list = set(list)
    print(new_list)

else:
    for i in one_sp:
        for j in two_sp:
            if i == j:
                list.append(i)
    new_list = set(list)
    print(new_list)