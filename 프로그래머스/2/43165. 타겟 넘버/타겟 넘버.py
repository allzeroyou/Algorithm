def solution(numbers, target):
    answer = 0
    
    p_node = [0] # 부모노드
    for number in numbers:
        s_node = [] # 자식노드-방법의 수
        for p in p_node:
            s_node.append(p+number)
            s_node.append(p-number)
        p_node = s_node

    
    return p_node.count(target)