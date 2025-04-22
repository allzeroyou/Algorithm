# 공차가 1인 등차수열
# 첫번째 항을 start라고 할 때 n항까지의 합은
# start + (start+1) + (start+2) + ... + (start+num-1)
# total = start * num + sum(1~n-1)
# start를 기준으로 식 다시 세우기
# start = num-total+ sum(1~n-1)/start

def solution(num, total):
    answer = []
    # 첫째항
    start = 1
    
    # sum
    su = 0
    for i in range(1, num-1):
        su += i
    
    start = (total-su)//num
    
    print(start)
    
    answer= [x for x in range(start, start+num)] # start 부터 시작하니까 start+num을 범위값으로 설정
    
    
    return answer