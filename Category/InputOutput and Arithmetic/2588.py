n1 = input()
n2 = input()
n1 = int(n1)
n2 = int(n2)
third = n1*((n2%((n2//100)*100))%10)
fourth = n1*((n2%((n2//100)*100))//10)
fifth = n1*(n2//100)

print(third)
print(fourth)
print(fifth)
print(n1*n2)


