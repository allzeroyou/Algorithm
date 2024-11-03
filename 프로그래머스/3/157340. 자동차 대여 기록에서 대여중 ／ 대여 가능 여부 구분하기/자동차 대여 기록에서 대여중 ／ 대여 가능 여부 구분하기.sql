-- 코드를 입력하세요
-- 2022년 10월 16일에 대여중이라면 '대여중', 대여중이지 않으면 '대여 가능'
-- 반납 날짜가 10월 16일 경우에도 '대여중'으로 표시
-- 자동차 id 기준 내림차순 정렬

WITH temp as
(
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= DATE '2022-10-16' AND END_DATE>= DATE '2022-10-16'
    GROUP BY CAR_ID
)

SELECT
    CAR_ID,
    CASE
        WHEN CAR_ID IN (SELECT * FROM temp)
        THEN '대여중'
        ELSE '대여 가능'        
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC