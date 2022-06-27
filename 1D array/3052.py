num = [] # 입력받은 숫자를 저장
for _ in range(10): # 10개 숫자 입력
    num.append(int(input())) # 입력받은걸 num 리스트에 추가

reminder=[] # 42로 나눈 나머지를 저장
for i in num: # 입력받은 숫자를 돌아서
    reminder.append(i%42) # 42로 나눈 나머지를 reminder 리스트에 추가

new_reminder=set(reminder) # 이때 서로 다른 나머지를 구하기 위해 집합 사용
print(len(new_reminder)) # 집합의 개수를 세기