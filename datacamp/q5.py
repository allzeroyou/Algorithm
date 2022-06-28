# 5
print("정수를 입력하시오 :")
num = int(input())

# for i in range(1, 11):
#     for j in range(i):
#          print(f"{j} {i}")


# answer
for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()