# 입력
# 양의 정수가 담긴 numbers

# 출력
# 가장 큰 수를 문자열로 return

def solution(numbers):
    answer = ''
    dic = {}

    for n in numbers:
        n = str(n)

        if len(n) >= 2:  # 제일 큰 자릿수를 기준으로 해야 함
            if n[0:1] in dic:
                dic[n[0:1]].append(n[1:])
            else:
                dic[n[0:1]] = [n[1:]]

        else:
            dic[n] = [n]

    key_list = list(dic.keys())
    key_list.sort(reverse=True)  # key 내림차순 정렬

    for k in key_list:
        ans_list = dic[k]
        ans_list.sort(reverse=True, key=lambda x: int(x))

        for a in ans_list:  # 4 3 0
            if k != a:  # 두자릿수 이상인 수일때는 key와 value를 합쳐서 join
                answer += k
                answer += a
            else:
                answer += a

    return answer

# test case pass
#print(solution([6, 10, 2]))
#print(solution([3, 30, 34, 5, 9]))
#print(solution([0,0,0]))
print(solution([99,0,90]))
