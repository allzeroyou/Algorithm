-- 코드를 입력하세요
-- USED_GOODS_BOARD: 게시판
-- USED_GOODS_USER: 게시판 첨부파일
-- 중고거래 3건 이상 등록한 사용자의 id, 닉네임, 주소, 전화번호 조회
-- 주소: 시, 도로명주소, 상세 주소 함께 출력! => CONCAT: 문자열 합치는 함수 사용
-- 전화번호는 010-3333-2222 처럼 (-)삽입
-- 회원 id 기준으로 내림차순 정렬
-- 


SELECT U.USER_ID, U.NICKNAME,
CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
CONCAT(LEFT(TLNO,3),'-',MID(TLNO,4,4),'-',RIGHT(TLNO,4)) AS 전화번호
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U ON B.WRITER_ID=U.USER_ID
GROUP BY WRITER_ID
HAVING COUNT(*)>=3
ORDER BY U.USER_ID DESC;