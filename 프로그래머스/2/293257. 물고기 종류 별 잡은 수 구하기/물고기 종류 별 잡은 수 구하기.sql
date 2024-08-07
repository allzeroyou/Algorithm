-- 코드를 작성해주세요
SELECT COUNT(FN.FISH_TYPE) AS FISH_COUNT, FISH_NAME
FROM FISH_NAME_INFO FN
INNER JOIN FISH_INFO FI
ON FN.FISH_TYPE = FI.FISH_TYPE
GROUP BY FN.FISH_NAME
ORDER BY FISH_COUNT DESC;