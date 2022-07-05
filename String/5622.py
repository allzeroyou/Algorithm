word = input()
'''
문제이해
1 = 2s
2 = 3s ABC
3 = 4s DEF
4 = 5s GHI
5 = 6s JKL
6 = 7s MNO
7 = 8s PQRS
8 = 9s TUV
9 = 10s WXYZ
0 = 11s 
한칸 옆 숫자를 걸려면 + 1s
예제 입력)
WA
10+3
UNUCIC
9 + 7+  9+ 3 +5 +3
'''

dia = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in word: # 입력받은 문자열의 문자 접근
    for j in dia: # 다이얼의 문자 접근
        if i in j: # 다이얼 문자에 입력받은 문자가 존재한다면
            time += dia.index(j)+2+1 # 다이얼 배열 위치(=번호)+ 초기 2초+ 한 칸 이동 1초
print(time)