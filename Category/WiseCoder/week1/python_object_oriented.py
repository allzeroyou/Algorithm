class FourCal:
    def __init__(self, first, second):
        # 생성자(Constructor): 객체가 생성될 때 자동으로 호출되는 메서드
        self.first = first
        self.second = second
    def setdata(self, first, second): # 클래스 안에 구현된 함수: 메서드(Method)
        self.first = first      # 메서드의 수행문1
        self.second = second    # 메서드의 수행문2
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
    def div(self):
        result = self.first/self.second
        return result

# 클래스 상속: 기존 클래스를 변경하지 않고 기능을 추가, 기존 기능을 변경하려고 할때 사용
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second

