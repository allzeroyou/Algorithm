def solution(array, commands):
    answer = []
    
    for c in commands:
        i = c[0]-1
        j= c[1]+1
        k = c[2]-1
        # 1 & 2
        tmp = array[i:j-1]
        tmp=sorted(tmp)
        
        answer.append(tmp[k])
        
        
        
        
        
        
    return answer