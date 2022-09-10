chess = [1, 1, 2, 2, 2, 8]

find_piece = list(map(int, input().split()))

perfect_piece = []


for i in range(6):
    if find_piece[i]==chess[i]:
        perfect_piece.append(0)
    elif find_piece[i] > chess[i]:
        perfect_piece.append(chess[i]-find_piece[i])
    elif find_piece[i] < chess[i]:
        perfect_piece.append(chess[i]-find_piece[i])
    else:
        perfect_piece.append(1)

for j in perfect_piece:
    print(j, end=' ')

