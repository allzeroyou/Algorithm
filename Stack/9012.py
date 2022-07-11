'''

한쌍의 괄호 기호로 된 "()" 문자열은 기본 vps(Valid Parenthesis String)
만약 x가 VPS라면 이걸 하나의 괄호로 넣은 새로운 문자열 "(x)"도 VPS
두 VPS x와 y를 접합(concatenation)한 새로운 문자열 xy 도 VPS

입력으로 주어진 괄호 문자열이 vps인지 아닌지 판단해서 그 결과를 yes/no로 나타내기
'''

n = int(input())

for i in range(n):
    word = input()
    stack = []
    for j in word:
        if j=="(":
            stack.append(j)
        elif j==")" and "(" not in stack:
            stack.append(i)
        elif j==")":
            stack.pop()
    if stack==[]:
        print("YES")
    else:
        print("NO")

