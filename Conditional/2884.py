si, bun = input().split()
si = int(si)
bun = int(bun)

if bun < 45 and si >= 1:
    print(si-1, 60-abs(bun-45))
elif bun < 45 and si < 1:
    print(23, 60-abs(bun-45))
else:
    print(si, bun-45)