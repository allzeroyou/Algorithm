t = int(input())

d = [0]*11
d[1]=1
d[2]=2
d[3]=4

for i in range(4,11):
    d[i]=sum(d[i-3:i])


for j in range(t):
    n = int(input())
    print(d[n])
