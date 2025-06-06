-- 코드를 입력하세요
-- 2022년 3월 오프라인, 온라인 상품 판매데이터 판매날짜, 상품 id, 유저 id, 판매량
-- 오프라인 user id 값은 null로 표시
-- 판매일 기준 오름차순 정렬, 상품 id, 유저 id
-- ORDER BY SALES_DATE, PRODUCT_ID, USER_ID

WITH TMP AS
(
    SELECT SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
    FROM OFFLINE_SALE
    WHERE SALES_DATE BETWEEN DATE '2022-03-01' AND DATE '2022-03-31'
    UNION ALL
    SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE SALES_DATE BETWEEN DATE '2022-03-01' AND DATE '2022-03-31'
)

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM TMP
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID