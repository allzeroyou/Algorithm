-- 코드를 입력하세요
-- 출고여부는 IF OUT_DATE <= 2022년 5월 1일: 출고완료
-- 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력
-- 아직 case문이 안붙네...(case로 시작하고, end로 끝남.
-- 이때 if문은 when 키워드처럼, 사용)

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d'), 
    CASE
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
        ELSE '출고미정'
    END '출고여부'
        FROM FOOD_ORDER
ORDER BY ORDER_ID;