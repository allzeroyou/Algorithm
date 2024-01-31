n = int(input())
num = n # 무한 루프에서 빠져나오기 위함
count = 0
while True:
    a = n//10 #2
    b = n % 10 #6
    c = (a+b)%10 # 8
    n = (b*10)+c # 68

    count+= 1
    if num == n: # 원래의 수로 돌아오면 반복문 빠져나감
        break
print(count)