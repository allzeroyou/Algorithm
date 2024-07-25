-- 코드를 작성해주세요
-- 길이가 10 이하: NULL -> 10으로 취급해서 평균 길이 구하기(case문 or coalesce 함수)
-- 1. type으로 그룹화(select 절에는 1.집계함수 or 2.group by에 명시된 컬럼만 사용 가능)
-- 2. 

SELECT
    COUNT(*) AS FISH_COUNT,
    MAX(CASE WHEN LENGTH IS NULL THEN 10 
        ELSE LENGTH END) AS MAX_LENGTH,
    FISH_TYPE 
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING
    AVG(CASE WHEN LENGTH IS NULL THEN 10 
        ELSE LENGTH END) >= 33
ORDER BY FISH_TYPE;