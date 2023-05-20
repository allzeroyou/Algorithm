def solution(genres, plays):
    answer = []
    # 속한 노래가 많이 재생된 장르를 먼저 수록
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i], i])
        else:
            dic[genres[i]]=[[plays[i], i]]
    # 장르내에서 많이 재생된 노래를 먼저 수록
    dic2={}
    for genre in dic.keys():
        songs=dic[genre]
        plays_sum =0
        for song in songs:
            plays_sum += song[0]
        dic2[genre]=plays_sum
    # 장르내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
    dic2=sorted(dic2.items(), key=lambda x: x[1],reverse=True)
    
    for i in dic2:
        song_rank=sorted(dic[i[0]], key=lambda x:(-x[0], x[1]))
        best_two = 0
        # 한 장르의 곡이 두 곡 저장되면 반복 중지
        for song in song_rank:
            answer.append(song[1])
            best_two+=1
            if best_two == 2:
                break
    return answer