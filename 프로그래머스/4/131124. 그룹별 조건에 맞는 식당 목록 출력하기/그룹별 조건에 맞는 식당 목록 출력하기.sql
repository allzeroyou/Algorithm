-- 두개 테이블에서 리뷰를 가장 많이 작성한 회원들의 리뷰 조회
-- 회원 이름 ,리뷰 텍스트 ,리뷰 작성일 출력
-- 결과는 리뷰 작성일 기준으로 오름차순, 리뷰 작성일 같다면 리뷰 텍스트 기준으로 오름차순

WITH A as (SELECT MEMBER_ID
          FROM REST_REVIEW
          GROUP BY MEMBER_ID -- 같은 값을 가진 행끼리 하나의 그룹으로 합친다
          ORDER BY count(*) DESC
          LIMIT 1)
SELECT MEMBER_NAME, REVIEW_TEXT,  DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
FROM MEMBER_PROFILE as m, REST_REVIEW as r, A
WHERE m.MEMBER_ID=r.MEMBER_ID AND m.MEMBER_ID=A.MEMBER_ID
ORDER BY 3, 2
