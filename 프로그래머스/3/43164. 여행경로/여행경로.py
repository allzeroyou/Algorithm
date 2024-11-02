# 방문하는 공항 경로 배열에 담아 return
# ICN에서 출발
def solution(tickets):
    answer = []
    
    graph = {} # 딕셔너리로 저장
    
    for start, end in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start]=[end]
            
    # 알파벳 순서로 정렬
    for airport in graph:
        graph[airport].sort()
    # 경로 찾기
    route =[]
    
    def dfs(airport):
        # 현재 공항이 graph의 key로 존재, 다음 공항이 있다면
        while airport in graph and graph[airport]:
            next = graph[airport].pop(0) # 다음 경로 찾기
            dfs(next)
        route.append(airport)
        
    dfs("ICN")
    
    return route[::-1]