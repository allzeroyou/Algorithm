def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x : x[1])
    final = 0
    job_len = len(jobs)
    
    while(jobs):
        for idx in range (0, len(jobs)):
            if jobs[idx][0] <= final:
                final += jobs[idx][1]
                answer += final-jobs[idx][0]
                jobs.pop(idx)
                break
            
            if idx == len(jobs)-1:
                final+=1
    
    return int(answer//job_len)