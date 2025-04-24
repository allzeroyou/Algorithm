def solution(arr):
    answer = []
    
    num = -1 # arr: 0~9 
    for a in arr:
        if a!=num:
            num = a
            answer.append(a)
            
    return answer