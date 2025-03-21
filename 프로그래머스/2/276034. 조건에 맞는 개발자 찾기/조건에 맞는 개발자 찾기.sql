-- 코드를 작성해주세요
-- &: 공통 비트 찾기 
SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) > 0
WHERE S.NAME IN ('Python', 'C#')
ORDER BY ID;