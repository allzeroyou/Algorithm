class Stack:
    # 파이썬은 내장 자료형인 리스트를 통해 스택 생성 가능
    def __init__(self):
        self.data = []
        # 초기화(intialize) 메서드: 어떤 클래스의 객체가 만들어질때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일
        # data 변수 안에는 파이썬에 내장되어 있는 리스트를 이용해 스택을 초기화

    class Stack:
        # 파이썬은 내장 자료형인 리스트를 통해 스택 생성 가능
        def __init__(self):
            self.data = []
            # 초기화(intialize) 메서드: 어떤 클래스의 객체가 만들어질때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일
            # data 변수 안에는 파이썬에 내장되어 있는 리스트를 이용해 스택을 초기화

        # 스택의 크기(길이)를 출력
        def size(self):
            return len(self.data)

        # 스택에 원소 삽입
        def push(self, item):
            self.top.append(item)

        # 스택의 원소 삭제 == 가장 위에 있는 원소 삭제하고 반환
        def pop(self, item):
            if not self.isEmpty():  # 스택이 공백이 아닐때
                return self.top.pop(-1)  # 후입선출==선입후출
            else:
                print('Stack underflow')  # 스택이 공백이라면
                exit()  # 실행 후 탈출

        # 스택 가장 위에 있는 원소 반환
        def peek(self):
            if not self.isEmpty():
                return self.top[-1]
            else:
                print('Stack underflow')
                exit()

        # 스택이 비어있는지를 반환
        def isEmpty(self):
            return self.size() == 0

    # 스택의 크기(길이)를 출력
    def size(self):
        return len(self.data)

    # 스택에 원소 삽입
    def push(self, item):
        self.top.append(item)
    # 스택의 원소 삭제 == 가장 위에 있는 원소 삭제하고 반환
    def pop(self, item):
        if not self.isEmpty(): # 스택이 공백이 아닐때
            return self.top.pop(-1) # 후입선출==선입후출
        else:
            print('Stack underflow') # 스택이 공백이라면
            exit() # 실행 후 탈출
    # 스택 가장 위에 있는 원소 반환
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print('Stack underflow')
            exit()

    # 스택이 비어있는지를 반환
    def isEmpty(self):
        return self.size() == 0
