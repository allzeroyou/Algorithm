from collections import Counter

def solution(k, tangerine):
   # 1. 귤 크기별 빈도 계산
    counter = Counter(tangerine)
    
    # 2. 빈도순 정렬 (내림차순)
    frequencies = sorted(counter.values(), reverse=True)
    
    # 3. 가장 많이 나오는 귤부터 골라서 k개 채우기
    count = 0
    selected = 0
    
    for freq in frequencies:
        count += freq
        selected += 1
        if count >= k:
            break
    
    return selected