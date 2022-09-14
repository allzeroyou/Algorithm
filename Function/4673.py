numbers= list(range(1, 10_001))
remove_lst = []
for num in numbers:
    for n in str(num): # 2
        num += int(n)  # 생성자
    if num<=10_000:
        remove_lst.append(num)

for remove_num in set(remove_lst):
    numbers.remove(remove_num) # 리스트에서 리스트 빼기
for self_num in numbers:
    print(self_num)