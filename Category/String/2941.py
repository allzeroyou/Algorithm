'''
c=
c-
dz=
d-
lj
nj
s=
z=

ljes=njak은 크로아티아 알파벳 5개로 이뤄짐.

'''

word= input()
alphabet=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=', 'z=']

for i in alphabet:
    word = word.replace(i, '*')
print(len(word))

