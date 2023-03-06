class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            # 스택이 비었다면
            if S.isEmpty():
                return False
            else:
                # 아니라면 pop 하는데, 이때 괄호를 검사
                v = match[c]
                if v == S.pop():
                    return True
    return S.isEmpty()

