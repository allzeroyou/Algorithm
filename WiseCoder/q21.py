mylist = ['dog', 'cat', 'parrot']

for char in mylist:
    char = char.replace(char[0], char[0].upper())
    print(char)