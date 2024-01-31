'''
조건 1) 최대 토큰의 길이는 len(s)//2=4 이므로, 이 값을 기준으로 -1씩 하며 순차 탐색
조건 2) 주어진 문자열을 토큰의 길이만큼 파싱하여 연속된 문자열이 같은지 확인
  - 조건 2-1. 단, 연속된 문자열은 2개 이상이 될 수 있으므로("ccc"--> "3c") 같지 않은 문자열이 나올때 까지 확인하는 조건문 삽입

조건 3) 같은 문자열이라면 count +=1 후 결과 문자열 생성

조건 4) 가능한 토큰의 길이 별(4,3,2,1) 결과문자열 List를 모두 생성 후 이들의 Length를 구함
조건 5) Length에서 minimum value 를 추출
'''


def solution(s):
    result_list = []  # 결과 문자열 List

    if len(s) == 1: return 1  # 길이가 1인 경우 그냥 1로 출력

    for token_length in range(len(s) // 2, 0, -1):  # 조건 1
        # 1개씩 토큰, 2개씩 토큰.... 최대 len(s)//2 만큼 토큰길이 설정
        count = 1
        result = ""  # 결과 문자열
        copy_s = s  # 문자열 초기화

        for _ in range(len(s) // token_length + 1):
            while True:  # 조건 2-1, 같지 않은 문자열이 나올때까지 탐색
                temp_str = copy_s[:token_length]
                comp_str = copy_s[token_length:token_length * 2]
                copy_s = copy_s[token_length:]  # 문자열 sliding window 방식 탐색
                if len(comp_str) != token_length: break  # token_length가 len(s)의 약수가 아닌 경우
                if temp_str == comp_str:
                    count += 1  # 조건 3
                else:
                    break  # 같지 않은 문자열이 나온 경우 break
            result += (str(count) if count != 1 else "") + temp_str  # (숫자)(문자) 형태 결과문자열 생성
            count = 1  # count값 초기화
        result_list.append(result)  # 결과 문자열 List 생성
    length_list = [len(x) for x in result_list]  # 조건 4, 생성된 결과 문자열 List를 length로 반환
    return min(length_list)  # 조건 5
