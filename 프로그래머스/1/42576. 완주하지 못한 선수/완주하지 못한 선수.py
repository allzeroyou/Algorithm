# 마라톤 참여: participant
# 완주 선수: completion
# 완주하지 못한 선수?
def solution(participant, completion):
    answer = ''
    # 참여 선수를 딕셔너리로 저장 -> 딕셔너리는 키 중복 안됨에 주의
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p]=0
        else:
            dic[p]+=1
    
    # 완주 선수가 딕셔너리의 키로 있다면
    for c in completion:
        if dic[c]==0: # 값이 0이면 딕셔너리에서 삭제
            del dic[c]
        else: # 값이 1 이상이면
            dic[c]-=1
            
    # 값이 0인 요소 출력
    for d in dic:
        answer= d
 

    return answer
  



# 시간초과
# def solution(participant, completion):
#     # p-c 해서 남은 선수가 완주 x
#     participant.sort()
#     completion.sort()
#     for p in participant:
#         for c in completion:
#             if p==c:
#                 participant.remove(c)
    
#     answer = p
#     return answer