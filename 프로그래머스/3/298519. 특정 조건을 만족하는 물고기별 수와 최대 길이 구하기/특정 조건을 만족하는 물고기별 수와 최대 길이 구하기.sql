-- 코드를 작성해주세요
-- 평균 33cm 이상인 물고기-> 종류별 분류
-- 잡은수, 최대길이, 물고기 종류 출력
-- 물고기 종류에 대해 오름차순 정렬
-- 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 NULL -> 10cm로 취급

SELECT
    COUNT(*) AS FISH_COUNT,
    MAX(CASE
        WHEN LENGTH IS NULL THEN 10 
        ELSE LENGTH END) AS MAX_LENGTH,
    FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(CASE
        WHEN LENGTH IS NULL THEN 10 
        ELSE LENGTH
    END) >= 33
ORDER BY FISH_TYPE;