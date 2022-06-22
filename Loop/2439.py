count = int(input())

for i in range(1, count+1):
    space = " "*(count-i)
    star = "*"*i
    print(space+star)

