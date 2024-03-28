def solution(ingredient):
    ig = ingredient
    answer = 0
    # 1,2,3,1이면 햄버거 완성
    h = [1,2,3,1]
    tmp = []
    
    for i in ig:
        tmp.append(i)
        if tmp[-4:]==h: # 끝에서부터 4개를 비교
            answer+=1
            del tmp[-4:]
            
        
    return answer