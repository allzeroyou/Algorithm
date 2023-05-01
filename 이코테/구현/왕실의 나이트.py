# 8x8 좌표평면
# 행 위치 표현시 1~8
# 열 위치 표현시 a~h

# 요구사항 대로 충실히 구현
# 나이트의 8가지 방향 -> 방향벡터 정의

# ------------------------------------
# 현재 나이트 위치 받기
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, 2)]

# 8가지 이동 방향으로 이동 가능?
result = 0

for direction in directions:
    # 이동하고자 하는 위치
    next_row = row + direction[0]
    next_col = column + direction[1]
    # 해당 위치로 이동 가능하면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1
print(result)
