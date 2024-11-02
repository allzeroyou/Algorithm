def solution(begin, target, words):
    answer = 0
    
    q = [(begin, 0)]
    # 단어 중복 사용 x
    visited = [False]*len(words)
    
    while q:
        word, cnt = q.pop()
        
        for i in range(len(words)):
            # 알파벳 하나만 다른거 비교 후 큐에 삽입
            if not(visited[i]):
                # 문자열 순회 가능하므로, 인덱스로 비교
                flag = 0
                
                for j in range(len(word)): # 현재 단어
                    if word[j] != words[i][j]: # 같지 않을때 카운트 중가 -> 카운트가 1인 단어 사용
                        flag +=1
                if flag == 1:
                    q.append((words[i], cnt+1))
                    visited[i]=True
        # 탈출조건
        if target == word:
            answer = cnt
            break
                        
    return answer