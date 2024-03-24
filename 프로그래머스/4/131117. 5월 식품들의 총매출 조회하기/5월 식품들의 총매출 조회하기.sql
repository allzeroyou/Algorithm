-- 코드를 입력하세요
-- 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, SUM(o.AMOUNT)*p.PRICE as TOTAL_SALES
FROM FOOD_PRODUCT as p, FOOD_ORDER as o
where p.PRODUCT_ID = o.PRODUCT_ID AND o.PRODUCE_DATE LIKE "2022-05%"
group by 1
order by 3 desc, 1;