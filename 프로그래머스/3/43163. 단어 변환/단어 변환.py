# begin, target, 단어의 집합: words
# begin -> target으로 변환하는 가장 짧은 과정! => bfs

# 한번에 한개의 알파벳만 바꿀수 o -> 단어들 순회하면서 하나씩 바꾸면서 일치하는지 체크

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    q = deque()
    q.append((begin, 0)) # 시작노드, 단어깊이 삽입
    # 방문 단어 체크
    visited = [0]*len(words)
    
    while(q):
        word, dep = q.popleft()
        
        for i in range(len(words)):
            
            if not(visited[i]): # 사용 안한 단어라면
                # 그 단어가 알파벳 하나만 다른지 검사
                cnt = 0
                for j in range(len(word)):
                    if word[j]!=words[i][j]:
                        cnt+=1
                if cnt == 1: # 하나만 다른 단어라면
                    q.append((words[i], dep+1))
                    visited[i]=1
        if word == target:
            answer = dep
            break # while 탈출
    
    return answer