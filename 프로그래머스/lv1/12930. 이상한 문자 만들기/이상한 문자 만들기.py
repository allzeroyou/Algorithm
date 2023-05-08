def solution(s):
    answer = ''
    lst = list(s.split())
    cnt = 0
    for i in lst:  # try
        c_lst = list(i)  # t,r,y
        for j in range(len(c_lst)):  # 3
            if j % 2 == 0:
                c_lst[j] = c_lst[j].replace(c_lst[j], c_lst[j].capitalize())  # T
        answer += ''.join(c_lst)
        cnt += 1
        if cnt < len(lst):
            answer+=' '

    return answer