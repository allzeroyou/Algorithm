-- 대여 차 정보: rental
-- 대여 기록: history
-- 할인 정보: discount
-- 할인율: 7일 이상(~30), 30일 이상(~90), 90일 이상 -> 7일 미만은 할인 x
-- 트럭 대여 기록(1,6,8,12,20,30)
-- 대여 기록별로 대여 금액(FEE 컬럼) 구하기 -> 대여 기록 id, 대여 금액 리스트 출력
-- 대여 금액 기준 내림차순, 대여 기록 id 내림차순

-- 주의할 점
-- 0. 할인율 하드코딩 하면 안됨(할인율 테이블 달라질 수 있음)
-- 1.DATEDIFF 는 +1 을 해줘야함(대여일 포함)
-- 2.CASE THEN은 switch 문처럼 위에서 부터 순차 실행되므로, 큰 범위부터 거르기
-- 3. 걍 JOIN은 할인 적용 안될 경우를 누락함. LEFT JOIN으로 7일 미만일 경우도 포함해야 함
    
    
WITH TMP AS(
    SELECT 
        HISTORY_ID, DAILY_FEE, DATEDIFF(end_date, start_date)+1 AS RENTAL_DATE, CAR_TYPE,
     CASE 
        WHEN DATEDIFF(end_date, start_date)+1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(end_date, start_date)+1 >=30 THEN '30일 이상'
        WHEN DATEDIFF(end_date, start_date)+1 >=7 THEN '7일 이상'
        ELSE 'NULL' END AS TYPE 
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY R
    JOIN CAR_RENTAL_COMPANY_CAR C ON C.CAR_ID=R.CAR_ID
    WHERE CAR_TYPE = '트럭'
)
    
SELECT T.HISTORY_ID, ROUND(
    T.DAILY_FEE*T.RENTAL_DATE*(100-IFNULL(P.DISCOUNT_RATE, 0))/100) AS FEE
FROM TMP T
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
ON P.duration_type=T.TYPE
AND P.CAR_TYPE=T.CAR_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC;