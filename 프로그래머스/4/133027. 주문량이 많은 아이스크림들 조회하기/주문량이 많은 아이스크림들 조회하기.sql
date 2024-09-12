-- 코드를 입력하세요
-- 아이스크림 가게 상반기 주문 정보: first_half 테이블-기본키: flavor, july 테이블의 fk: shipment_id
-- 7월의 아이스크림 주문 정보: july 테이블-기본키: shipment_id, first_half 테이블의 fk: flavor

-- 7월에는 주문량이 많아 같은 아이스크림에 대해 서로 다른 두 공장에서 가게로 출하 진행하는 경우 o
-- 이 경우 같은 맛의 아이스크림이라도 다른 출하 번호 가짐

-- 7월 아이스크림의 총 주문량+ 상반기 아이스크림 총 주문량 -> 상위 3개 맛 조회


-- 1.july 테이블에서 같은 맛 아이스크림 주문량 합치기
# SELECT FLAVOR, SUM(TOTAL_ORDER) AS J_TOTAL
# FROM JULY 
# GROUP BY FLAVOR

-- 2. 상반기 테이블 + 7월 테이블
SELECT
    F.FLAVOR
FROM FIRST_HALF F
LEFT JOIN 
    (SELECT FLAVOR, SUM(TOTAL_ORDER) AS J_TOTAL
    FROM JULY 
    GROUP BY FLAVOR) J
ON
    F.FLAVOR = J.FLAVOR
ORDER BY
    (F.TOTAL_ORDER + COALESCE(J.J_TOTAL, 0)) DESC
LIMIT 3;