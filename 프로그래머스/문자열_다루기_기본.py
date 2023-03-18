def solution(s):
    # 문자열 s의 길이가 4혹은 6
    # 숫자로만 구성돼있는지 확인해주는 함수

    # e.g. s가 "a234" -> False
    # "1234" -> True
    if len(s) == 4 or len(s) == 6: # len(s) in [4,6] 도 가능.
        return s.isdigit()
    else:
        return False
