while (1):
    name, age, weight = input().split()
    if str(name) == "#":
        break
    if int(age) > 17 or int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")