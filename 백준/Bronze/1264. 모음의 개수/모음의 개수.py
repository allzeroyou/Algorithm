while True:
    sen = input().lower()

    mo = ['a', 'e', 'i', 'o', 'u']

    if sen == '#':
        break
    cnt = 0

    for m in mo:
        cnt += sen.count(m)
    print(cnt)
