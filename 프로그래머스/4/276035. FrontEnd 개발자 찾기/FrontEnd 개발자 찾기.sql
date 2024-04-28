# -- 코드를 작성해주세요
# 예를 들어 어떤 개발자의 SKILL_CODE가 400 (=b'110010000')이라면, 이는 SKILLCODES 테이블에서 CODE가 256 (=b'100000000'), 128 (=b'10000000'), 16 (=b'10000') 에 해당하는 스킬을 가졌다는 것 -> 어떻게 구현? "&" -> 비트 연산자 사용!


SELECT distinct(ID), EMAIL, FIRST_NAME, LAST_NAME
FROM SKILLCODES s, DEVELOPERS d
WHERE d.SKILL_CODE & s.CODE and s.CATEGORY LIKE 'Front%'
ORDER BY d.ID
