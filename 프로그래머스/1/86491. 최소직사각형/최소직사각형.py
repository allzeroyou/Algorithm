# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 
# 회전 가능 하므로 가로/세로 중 가장 큰 값을 뽑은 후, 세로에서 가장 큰 값이 아닌 두번째로 큰 값을 곱해주면 된다.

def solution(sizes):
    answer = 0 
    w = []
    h = []

    for size in sizes:
        if size[0]<size[1]:
            size[0], size[1]=size[1], size[0]
        w.append(size[0])
        h.append(size[1])
  
            
    return max(w)*max(h)