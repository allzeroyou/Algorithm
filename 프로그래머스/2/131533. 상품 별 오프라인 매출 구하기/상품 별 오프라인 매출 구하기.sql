-- 코드를 입력하세요
-- PRODUCT: 의류 쇼핑몰에서 판매중인 상품 정보
-- OFFLINE_SALE: 오프라인 상품 판매 정보
-- 상품코드 별 매출액(판매가*판매량) 합계 출력
-- 매출액 기준 내림차순, 매출액 같다면 상품코드 기준으로 오름차순 정렬

SELECT PRODUCT_CODE, SUM(PRICE*SALES_AMOUNT) AS SALES
FROM PRODUCT P
JOIN OFFLINE_SALE O ON P.PRODUCT_ID=O.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE