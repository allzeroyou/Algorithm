'''
문제 설명
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
이때 모든 알파벳은 오름차순으로 정렬해 이어 출력. 그뒤에 모든 숫자를 더한 값을 이어 출력

예를 들어 K1KA5CB7 -> ABCKK13 출력
'''
data = input()
res = []
val = 0

# 문자를 하나씩 확인하자
for x in data:
    # 만약 알파벳이라면 결과 리스트에 삽입
    if x.isalpha():
        res.append(x)
    # 숫자는 따로 더하기
    else:
        val += int(x)
# 알파벳을 오름차순으로 정렬
res.sort()

# 숫자가 하나라도 존재 하면 가장 뒤에 삽입
if val != 0:
    res.append(str(val))

# 최종 결과 출력(리스트를 문자열로 변환해 출력)
print(''.join(res))

'''
문제 해결 아이디어
요구사항 대로 충실히 구현하면 됨
문자열이 입력되었을 때 문자를 하나씩 확인
- 숫자인 경우 따로 합계 계산
- 알파벳은 별도의 리스트에 저장
결과적으로 리스트에 저장된 알파벳을 정렬해 출력, 합계를 뒤에 붙여 출력하면 정답!
'''