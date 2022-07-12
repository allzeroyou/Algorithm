class Singer:                   # 가수를 정의해볼게요.
    def sing(self):             # 노래하기 메서드
        return "Lalala~"
taeyeon = Singer()              # 태연을 만들어랏!
print(taeyeon.sing())           # 노래 한 곡 부탁해요~
'''
클래스 만들기
class 클래스이름:
    클래스의 성질, 행동 정의 => 클래스 내부에 정의된 함수: 메서드(method)
    
여기서 sing 메서드는 Singer라는 클래스가 하는 행동을 정의.
Singer 클래스를 만든 다음에는 taeyeon이라는 객체를 만듦.

인스턴스명 = 클래스() 와 같이 만듦.
그 다음 만들어진 인스턴스인 taeyeon에게 노래를 시켜봄.
Singer 클래스에 sing 메서드를 정의해줬기 때문에 Singer클래스에 속한 taeyeon 객체도 sing 메서드 사용 가능.

다시말해, 가수는 노래를 할 수 있으니까 태연이라는 가수도 역시 노래를 할 수 있는 것!
이와 같이 어떤 객체의 메서드를 사용할 때는 객체.메서드 형식으로 해주면 된다!
'''

'''
실제 세계에 존재하는 실체(instance)를 객체(object)라고 함.
객체들의 공통점을 간추려서 개념적으로 나타낸 것 => 클래스(class)

어떤 클래스를 만드려면 그 객체가 갖는 성질과 그 객체가 하는 행동을 정의해주면 된다!
디아블로2 게임의 아마존의 캐릭터를 클래스로 표현해보자.
'''
class Amazon:
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15

    def attack(self):
        return 'Jab!!!!!'
    def exercise(self):         # 훈련을 하면
        self.strength += 2      # 힘 +2
        self.dexterity += 3     # 기술 +3
        self.vitality += 1      # 체력 +1
# 아마존 클래스가 갖고 있는 힘, 기술, 체력, 에너지라는 네가지 성질은 변수로 나타냄
# '공격'하는 행동은 메서드로 표현
# self는 바로 그 클래스의 객체를 가리킴. jane, mary가 똑같은 attack 메서드를 가지기 때문에 서로 구별하기 위해 사용됨 => 메서드를 정의할 때는 항상 self라는 인자를 쓴다!

class Person:
    # 눈 두개, 코 하나, 입 하나..
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2
    # 먹고 자고 이야기하고..
    def eat(self):
        print('암냠..')
    def sleep(self):
        print('쿨쿨..zz')
    def talk(self):
        print('주절주절..')

class Student(Person):      # 학생도 사람이니까, Person의 클래스 상속받음
    def study(self):
        print('열공열공..')

yoo = Person()
print(yoo.mouth)
print(yoo.talk())
kim = Student()
print(kim.ears)
print(kim.study())