SELECT SUM(HG.SCORE) AS SCORE, HE.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM HR_EMPLOYEES AS HE
INNER JOIN HR_GRADE AS HG
ON HE.EMP_NO = HG.EMP_NO
WHERE HG.YEAR = 2022
GROUP BY HE.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
ORDER BY SCORE DESC
LIMIT 1;
