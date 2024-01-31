'''
특별한 메서드들

메서드는 클래스를 만들면서 그 안에 만들어 넣는 함수!
만들어진 메서드를 사용하려면 객체.메서드() 와 같은 형식으로 호출함!
일반적인 메서드들과는 조금 다른 특별한 메서드에 대해 알아보자
'''

# __init__ 메서드(초기화)
class Book:
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목: ',self.title)
        print('가격: ',self.price)
        print('저자: ',self.author)

    def __init__(self, title, price, author):
        # 파이썬에서 특별하게 약속된 메서드 가운데 하나로, 초기화(intialize)메서드=생성자(constructor)
        # 어떤 클래스의 객체가 만들어질때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일

        # 객체를 생성시킬때 제목, 가격, 저자를 인자로 받아서 setData 메서드에게 넘겨주도록 함!
        # 직접 변수를 다뤄도 괜찮지만 setData 메서드를 미리 만들어뒀으니 이용한 것!
        # 책 객체를 만들때는 다음과 같이 세 개의 인자를 넘겨주면 됨!
        self.setData(title, price, author)
        print('책 객체를 새로 만들었어요~')

