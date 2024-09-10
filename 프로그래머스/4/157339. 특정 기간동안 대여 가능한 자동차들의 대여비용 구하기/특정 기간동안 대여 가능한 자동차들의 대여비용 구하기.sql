-- '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트
-- 1. 2022년 11월 대여 가능한 자동차
-- 2. 세단, suv만 선택
-- 3. 30일 대여시 할인율 적용한 금액 계산
-- 4. 계산된 금액이 50만원 이상, 200만원 미만인거만
-- 5. 정렬

SELECT
  C.CAR_ID,
  C.CAR_TYPE,
  FLOOR(C.DAILY_FEE * 30 * (1 - D.DISCOUNT_RATE/100)) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR C
LEFT JOIN
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN D ON C.CAR_TYPE=D.CAR_TYPE AND D.DURATION_TYPE = '30일 이상'
WHERE
    C.CAR_TYPE IN ('세단','SUV' )
    AND C.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
    )
HAVING
    FEE BETWEEN 500000 AND 1999999
ORDER BY
    FEE DESC,
    C.CAR_TYPE,
    C.CAR_ID DESC;
