n = int(input())
stick=[64,32,16,8,4,2,1]
cnt=0
for i in range(len(stick)):
    if n >= stick[i]:
        cnt +=1
        n-= stick[i]
    if n==0:
        break
        
print(cnt)