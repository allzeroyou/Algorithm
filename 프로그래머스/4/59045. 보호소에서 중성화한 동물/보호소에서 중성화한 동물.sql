-- 코드를 입력하세요
-- 중성화 거친 동물 정보?
-- 보호소 들어올 때는 중성화 x, 나갈 때 중성화된 동물 id, 종, 이름 조회

-- id 순으로
-- 보호소 들어올때
-- SEX_UPON_INTAKE: Spayed-중성화, Intact-중성화 x
-- 보호소 나갈때
-- SEX_UPON_INTAKE: Neutered-중성화


SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE 'Intact%'
AND (O.SEX_UPON_OUTCOME LIKE 'Neutered%' OR O.SEX_UPON_OUTCOME LIKE 'Spayed%')
ORDER BY I.ANIMAL_ID;