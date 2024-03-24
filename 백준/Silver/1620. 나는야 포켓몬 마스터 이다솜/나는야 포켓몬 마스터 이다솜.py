# 포켓몬 개수 n, 문제 개수 m
n, m = map(int, input().split())
# 포켓몬 이름: 대소문자 mix
# 문자 -> 숫자로, 숫자 -> 문자로 : key-value 이용

# 도감 하나만 생성시 시간초과 -> 번호/ 이름으로 나누자.
book_number = {} # 번호를 키로 가지고 이름을 값으로 가지는 딕셔너리
book_name = {}

for i in range(1, n + 1):
    name = input()
    book_number[str(i)] = name
    # 소문자로 저장
    book_name[name.lower()] = str(i)

for j in range(m):
    inp = input()
    # 입력이 숫자라면 해당 번호 포켓몬 이름 출력
    if inp.isdigit():
        print(book_number[inp])
    # 입력이 문자열이라면 해당 이름의 포켓몬 번호 출력
    else:
        print(book_name[inp.lower()])
