n = int(input())

pos = list(map(int, input().split()))

pos = sorted(pos)


print(pos[(n-1)//2]) # 중간값 구하기