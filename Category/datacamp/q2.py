# 2
seats = []
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

list = []
print("=" * 40)
for i in range(11):
    list.append(i)
print(list)
print("=" * 40)


def displayBookings(seats):
    for row in seats:
        print(row)
    print(" ")
    print("원하시는 좌석의 행번호를 입력하세요(종료는 -1)")
    hang = int(input())
    print("원하시는 좌석의 열번호를 입력하세요(종료는 -1)")
    yeol = int(input())
    print("예약합니다.")

    seats[hang][yeol] = 1

    print(seats)


displayBookings(seats)
