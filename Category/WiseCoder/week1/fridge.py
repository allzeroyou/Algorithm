class Fridge:
    def __init__(self):
        self.isOpened = False  # 문이 열렸는지 나타내는 isOpened 변수
        self.foods = []  # 냉장고 안에 들어있는 음식들의 리스트

    def open(self):  # 냉장고 문 열기
        self.isOpened = True
        print('냉장고 문을 열었어요..')

    def put(self, thing):  # 냉장고에 음식 집어넣기
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어갔네..')
        else:
            print('냉장고 문이 닫혀있어서 못 넣었네요..')

    def close(self):  # 냉장고 문 닫기
        self.isOpened = False
        print('냉장고 문을 닫았어요..')


class Food:
    pass



