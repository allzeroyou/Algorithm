count = int(input())
# stack = []

for i in range(count):
    stack = []
    string = input()
    for i in string:
       if i=="(":
           stack.append(i)
       elif i==")" and "(" not in stack:
           stack.append(i)
       elif i==")":
           stack.pop()
    if len(stack):
        print(f"짝이 맞지 않은 괄호의 개수: {len(stack)}")
        print("NO")
    else:
        print("YES")
'''
k=int(input());
result=[]
for i in range(k):
    stk=[]
    isVPS=True
    for char in input():
        if char == '(':
            stk.append(char);
        elif char ==')':
            if stk:
                stk.pop();
            else: #여는 괄호가 없는 경우
                isVPS=False;
                break;
    if stk: #여는 괄호가 남는경우
        isVPS=False;
    result.append('YES' if isVPS else 'No');

    # print('YES' if isVPS else 'No')                
print(result);
'''