-- 코드를 입력하세요
-- 동물 중성화 여부? 되었다면 'O', 'X'
-- N, S -> 중성화 한거
-- 맞는 조건일때 O,X로 표시 어떻게하지?

SELECT ANIMAL_ID, NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE 'Neutered%' THEN 'O'
    ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
