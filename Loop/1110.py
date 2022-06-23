n = int(input())
count = 0
while True:
    a = n//10 #2
    b = n % 10 #6
    c = (a+b)%10 # 8
    n = (b*10)+c # 68

    count+= 1

print(count)