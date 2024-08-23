# nxn 크기 2차원 배열 -> 잘라서 1차원 배열로 전환
# 전체 2차원 배열 만들기 보다는 특정 위치에서 계산해 1차원 배열에 넣는게 효율적임

def solution(n, left, right):
    answer = []
    # 2차원 배열에서 몇번째 행, 몇번째 열
    for i in range(left, right+1):
        row = i//n # 1차원 -> 2차원 행
        col = i%n # 1차원 -> 2차원 열
        answer.append(max(row, col)+1)
    
    
    return answer