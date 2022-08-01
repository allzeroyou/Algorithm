# 그래프 탐색 알고리즘
## DFS/ BFS

탐색(Search)란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
대표적인 그래프 탐색 알고리즘으로는 DFS/ BFS가 있음
DFS/ BFS는 코딩테스트에서 매우 자주 등장하는 유형으로 반드시 숙지해야!

### 스택
먼저 들어온 데이터가 나중에 나가는 형식(선입후출)
입구와 출구가 동일한 형탵로 스택을 시각화 가능
ex. 창고에 박스 쌓기

### 파이썬에서의 스택
```
stack = []
# 삽입(5)- 삽입(2)- 삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```

### 큐
먼저 들어온 데이터가 먼저 나가는 형식(선입후출)
큐는 입구와 출구가 모두 뚫려있는 터널가 같은 형태로 시각화
ex. 버스정류장에서 버스 기다리는 줄

### 파이썬에서의 큐
```
from collections import deque
# 큐 구현을 위한 deque 라이브러리 사용
queue = deque()
# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삭제(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)        # 먼저 들어온 순서대로 출력
queue.reverse()     # 역순으로 바꾸기
print(queue)        # 나중에 들어온 원소부터 출력
```
## 재귀 함수
재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수
단순한 형태의 재귀 함수 예제
- '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력
- 어느정도  출력하다가 최대 재귀 깊이 초과 메시지 출력
```
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()
recursive_function()
```
### 재귀 함수의 종료 조건
재귀 함수를 문제풀이에 사용할때는 반드시 재귀 함수의 종료 조건을 명시해야
종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
- 종료 조건을 포함한 재귀 함수 예제
```
def recursive_function(i):
    # 100번째 호출을 했을때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출')
    recursive_function(i+1)
   print(i, '번째 재귀함수 종료')
recursive_function(1)
```

### 팩토리얼 구현 예제
n! = 1x2x3x ... x(n-1)xn
수학적으로 0!과 1!의 값은 1임

```
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= 1
    return result
    
# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n*(n-1)!를 그대로 코드로 구현
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력
print('반복적으로 구현: ',factorial_iterative(5))
print('재귀적으로 구현: ',factorial_iterative(5))
```
### 최대공약수 계산(유클리드 호제법) 예제
두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있음
유클리드 호제법
- 두 자연수 A,B에 대해 (A>B) A를 B로 나눈 나머지를 R
- 이때 A, B의 최대공약수는 B와 R의 최대공약수와 같음
유클리드 호제법의 아이디어를 그대로 재귀함수로 작성 가능
### 유클리드 호제법
- 두 자연수 A,B에 대해 (A>B) A를 B로 나눈 나머지를 R
- 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같음
```
def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(192, 162))
```
### 재귀 함수 사용의 유의사항
재귀 함수를 잘 활용 -> 복잡한 알고리즘을 간결하게 작성 가능
모든 재귀 함수는 반복문을 이용해 동일한 기능 구현 가능

## DFS(Depth-First-Search)
깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
DFS는 스택 자료구조(혹은 재귀함수)를 이용
<구체적인 동작과정>
1. 탐색 시작 노드를 스택에 삽입, 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리.
방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄.
3. 더 이상 2번의 과정을 수행할 수 없을때까지 반복