-- 코드를 입력하세요
-- BOOK: 도서정보
-- AUTHOR: 저자정보
-- BOOK_SALES: 각 도서의 날짜별 판매량 정보
-- 2022년 1월 도서판매데이터를 기준으로 저자, 카테고리 별 매출액(AS TOTAL_SALES = 판매량 * 판매가) 구해서
-- 저자id, 저자명, 카테고리, 매출액 리스트 출력
-- 저자id 오름차순, 카테고리 내림차순

SELECT
    A.AUTHOR_ID,
    A.AUTHOR_NAME,
    B.CATEGORY,
    SUM(B.PRICE*S.SALES) AS TOTAL_SALES
FROM BOOK B
JOIN AUTHOR A ON B.AUTHOR_ID=A.AUTHOR_ID
JOIN BOOK_SALES S ON B.BOOK_ID=S.BOOK_ID
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC;