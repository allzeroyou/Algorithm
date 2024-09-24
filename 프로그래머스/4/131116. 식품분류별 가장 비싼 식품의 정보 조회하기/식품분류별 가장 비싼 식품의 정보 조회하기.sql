-- 코드를 입력하세요
-- FOOD_PRODUCT: 식품정보
-- 식품분류별로 "가격이 제일 비싼" 식품의 분류, 가격, 이름을 조회
-- 식품분류: 과자, 국, 김치, 식용유 만 출력
-- 식품 가격 기준으로 내림차순

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT F
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
AND PRICE = (
        SELECT MAX(PRICE)
        FROM FOOD_PRODUCT FP
        WHERE FP.CATEGORY=F.CATEGORY)
ORDER BY MAX_PRICE DESC;