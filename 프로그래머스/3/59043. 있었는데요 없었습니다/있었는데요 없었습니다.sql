-- 코드를 입력하세요
-- ANIMAL_INS: 동물보호소에 들어온 동물 정보
-- ANIMAL_OUTS: 동물보호소에서 보낸 동물 정보
-- 동물 입양일이 잘못 입력됨
-- 보호 시작일보다 입양일이 더 빠른 동물 id, 이름 조회
-- 보호 시작일 오름차순 정렬

SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID
WHERE O.DATETIME<I.DATETIME
ORDER BY I.DATETIME;