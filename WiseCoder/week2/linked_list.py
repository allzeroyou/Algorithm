class FourCal:

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

a = FourCal()
print(type(a)) # <class '__main__.FourCal'>


