def solution(n, lost, reserve):
    answer = 0
    # 여벌 체육복이 있는 학생 -> 체육복 빌려줄 수 있음
    # 학생들 번호: 체격순
    # 앞 번호, 뒷 번호 학생에게만 빌려줄 수 있음
    # 최대한 많은 학생이 체육 수업을 듣도록(여벌 + 도난당했지만 채육복 빌린 학생)
    
    # 학생 만들기
    st = []
    for i in range(1, n+1):
        st.append(i)
    # 체육복 빌릴 수 있는 후보 만들기
    # 여분 가져온 학생이 도난 당했을 경우 제외
    lost, reserve = list(set(lost)-set(reserve)), list(set(reserve)-set(lost))
    
    ca = []
    for l in lost:
        ca.append((l-1, l+1))
    
    for r in reserve:
        for c in ca:
            if r in c: # 체육복 빌릴 수 있는 경우
                answer+=1
                ca.remove(c) # 체육복 후보에서 제외
                break

    # 학생 - 도난 당한 학생 + 빌릴 수 있는 학생
    return n - len(lost) + answer
                
    
    return answer