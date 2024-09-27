-- 코드를 입력하세요
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY: 자동차 대여 기록
-- AVAILABILITY: 2022-10-16에 대여중인 자동차 -> '대여중' 표시, if 대여 중 x -> '대여 가능'
-- 자동차 id, AVAILABILITY 출력
-- 반납 날짜: 2022-10-16인 경우에도 '대여중' 표시!
-- 자동차 id 기준 내림차순
-- MAX는 단 1개의 최댓값만 추출하므로 count해서 대여기록이 1개라도 있는 경우 대여중으로 표시
SELECT 
    CAR_ID,
    CASE 
        WHEN EXISTS (
            SELECT 1 
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS subquery
            WHERE subquery.CAR_ID = CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID
            AND subquery.START_DATE <= '2022-10-16'
            AND subquery.END_DATE >= '2022-10-16'
        ) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 
    CAR_ID
ORDER BY CAR_ID DESC;
