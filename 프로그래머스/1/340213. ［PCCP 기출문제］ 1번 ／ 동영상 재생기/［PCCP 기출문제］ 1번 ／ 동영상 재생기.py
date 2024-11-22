# 동영상 재생기
# 알고리즘: 구현(문제 조건 맞추기)
# 3가지 기능 구현: +10초, -10초, 오프닝 건너뛰기

def solution(video_len, pos, op_start, op_end, commands):
    
    # : 기준 split하기
    # 기준이 sec 이므로, 전체 sec로 맞추고 계산
    def get_sec(t1, t2, t3, t4):
        tmp = [t1, t2, t3, t4]
        lst = []
        for i in range(4):
            m, s = tmp[i].split(':')
            total = int(m)*60 + int(s)
            lst.append(total)

        return lst

    lst =get_sec(video_len, pos, op_start, op_end)
    
    # 비디오 길이, 현재위치, 오프닝시작, 오프닝끝
    video, cur, start, end = lst
    
    # 공통 로직이므로 -> 아예 반복문 밖으로 빼기!
    if start<=cur<=end:
        cur = end
        
    for com in commands:
        if com == 'prev':
            cur = max(0, cur-10) # cur-10가 0미만일경우, 0으로 만드는 코드 기법!

        elif com == 'next': # next
            cur = min(video, cur+10) 
        if start<=cur<=end:
            cur = end
            
    #print(cur)
    # 결과출력
    # 초 -> 분으로 나누기
    m = str(cur//60)
    s = str(cur % 60)
    
    if len(m)<2:
        m='0'+m
    if len(s)<2:
        s='0'+s
    answer = ''
    answer = m+':'+s
    
    return answer