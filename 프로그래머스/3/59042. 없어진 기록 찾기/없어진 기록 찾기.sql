-- 코드를 입력하세요
-- ANIMAL_INS: 동물 보호소에 들어온 동물 정보
-- ANIMAL_OUTS: 동물 보호소에서 입양보낸 동물 정보
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID, 이름-> 정보가 유실된 동물 정보 출력 -> 차집합?
-- 정렬: ID 오름차순

SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS O
WHERE NOT EXISTS (
    SELECT *
    FROM ANIMAL_INS I
    WHERE I.ANIMAL_ID=O.ANIMAL_ID
)
ORDER BY ANIMAL_ID;
