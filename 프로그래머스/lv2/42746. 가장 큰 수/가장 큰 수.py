def solution(numbers):
    answer = ''
    numbers= list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) # 세자리수까지 비교
    # 앞의 0을 제거하기 위해 int형 변환 후 str 변환
    answer= str(int(''.join(numbers)))
    
    return answer