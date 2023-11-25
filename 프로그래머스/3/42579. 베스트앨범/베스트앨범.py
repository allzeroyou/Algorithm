def solution(genres, plays):
    answer = []
    # 1. 속한 노래가 많이 재생된 장르를 먼저 수록
    dic = {}
    
    for i in range(len(genres)):
        if genres[i] not in dic: # 초기화
            dic[genres[i]]=[[plays[i], i]] # 재생횟수, 번호 저장
            
        else: # 이미 초기화를 했다면 추가한다
            dic[genres[i]].append([plays[i], i])
    
    # 2. 장르내 많이 재생된 노래를 먼저 수록
    dic2 = {}
    for genre in dic.keys():
        songs = dic[genre] # 재생수 list
        ps = 0 # 재생수 합
        for song in songs:
            ps += song[0] # 재생 수 원소
        dic2[genre]=ps    
    
    dic2=sorted(dic2.items(), key=lambda x: x[1], reverse=True) # 내림차순

    # 3. 장르내에서 재생횟수가 같은 노래 중에서는 번호가 낮은 노래를 먼저
    for i in dic2: # 장르
        song_rank = sorted(dic[i[0]], key=lambda x: (-x[0], x[1])) # 횟수-내림차순, 번호-오름차순        
        best_two = 0 # 가장 많이 재생된 노래 2개
        # 장르 별 2개씩
        for song in song_rank:
            answer.append(song[1])
            best_two +=1
            if best_two == 2:
                break        
    
    return answer