'''
한수
어떤 양의 정수 x가 각 자리가 등차수열을 이룸
n이 주어졌을때, 1보다 크거나 같고, n보다 작거나 같은 한수의 개수를 출력하는 프로그램
'''

n = int(input())
hansu = 0

for i in range(1, n+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1 # 100보다 작으면 모두 한수임
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]: # 등차수열(공차가 같다면)
        hansu += 1
print(hansu)
