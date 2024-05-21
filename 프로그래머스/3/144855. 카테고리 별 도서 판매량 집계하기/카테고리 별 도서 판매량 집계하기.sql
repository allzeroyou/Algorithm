-- 코드를 입력하세요
SELECT CATEGORY, sum(SALES) TOTAL_SALES
FROM BOOK_SALES bs
INNER JOIN BOOK b ON bs.BOOK_ID=b.BOOK_ID
WHERE SALES_DATE LIKE "2022-01%"
GROUP BY 1
ORDER BY 1