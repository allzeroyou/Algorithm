-- 코드를 작성해주세요
-- SKILL_CODE -> 2진수 변환-> CODE의 조합으로 2진수가 되는 스킬 case 구하기
-- 2진수 변환 how?
-- front end스킬, python 스킬 함께 가진 개발자 -> front end스킬 포함되어있는지 어떻게 알지?

WITH FE AS (
    SELECT SUM(CODE)
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)
SELECT
    CASE
        WHEN SKILL_CODE & (SELECT * FROM FE) AND
            SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME='Python')
        THEN 'A'
        WHEN SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME='C#')
        THEN 'B'
        WHEN SKILL_CODE & (SELECT * FROM FE)
        THEN 'C'
    END AS 'GRADE', ID, EMAIL
FROM DEVELOPERS
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID;