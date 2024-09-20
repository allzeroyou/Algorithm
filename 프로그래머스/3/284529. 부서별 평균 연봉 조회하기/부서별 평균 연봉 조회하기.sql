-- 코드를 작성해주세요
-- 부서별 평균 연봉
-- 부서별 부서id, 영문 부서명, 평균 연봉 조회(소수점 첫째 자리 반올림 round(,0)) as AVG_SAL
-- 부서별 평균 연봉 내림차순 정렬




SELECT E.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(SAL),0) AS AVG_SAL
FROM HR_EMPLOYEES E
JOIN HR_DEPARTMENT D ON  E.DEPT_ID=D.DEPT_ID
GROUP BY E.DEPT_ID
ORDER BY AVG_SAL DESC;
