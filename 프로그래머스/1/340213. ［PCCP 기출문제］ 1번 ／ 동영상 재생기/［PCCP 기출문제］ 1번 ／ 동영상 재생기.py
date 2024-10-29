# 동영상 재생기
# 3가지 기능: 10초 전으로  이동, 10초 후로 이동, 오프닝 건너뛰기 
# 10초 전: "prev" 명령 -> 재생 위치: 현재 위치 - 10초(만약, 10초 미만일 경우 -> 처음 위치로 이동: 0분 0초)
# 10초 후: "next" 명령 -> 재생 위치: 현재 위치 + 10초(만약, 10초 미만일 경우 -> 마지막 위치로 이동: 동영상 길이)
# 오프닝 건너뛰기: 재생 위치가 오프닝 구간일 경우 자동으로 오프닝 끝나는 위치로 이동

# 문자열 -> 숫자로 (대소 비교하기 위해)
# : 기준으로 앞은 *60, 뒤는 그대로
def str_to_time(temp):
    tmp = temp.split(":")
    mi= int(tmp[0])*60
    sec = int(tmp[1])
    str_to_time = mi + sec 
    return str_to_time

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    cur_time = str_to_time(pos)
    ops_time = str_to_time(op_start)
    ope_time = str_to_time(op_end)
    video_time = str_to_time(video_len)
    
    for c in commands:
        if ops_time<=cur_time <ope_time:
            cur_time = ope_time
                
        if c == "next":
            cur_time+=10
            if ops_time<=cur_time <ope_time:
                cur_time = ope_time
            if video_time-cur_time < 10:
                cur_time = video_time
        elif c == "prev":
            cur_time -=10
            
            if ops_time<=cur_time <ope_time:
                cur_time = ope_time
            if cur_time < 10:
                cur_time = 0
                continue
    print(cur_time)
    
    res_min=cur_time//60
    res_sec = cur_time - (res_min)*60

    if len(str(res_min))<2:
        res_min = "0"+str(res_min)
    if len(str(res_sec))<2:
        res_sec = "0"+str(res_sec)    
    print(str(res_min)+":"+str(res_sec))

    
    return str(res_min)+":"+str(res_sec)