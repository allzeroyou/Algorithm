import re

word = input()
temp = re.sub("[^a-z0-9]","", word.lower())
print(temp == temp[::-1])

# A man, a plan, a canal: Panama