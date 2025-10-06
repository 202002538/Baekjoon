-- 재귀적 CTE 사용
-- SQL의 자기 호출이 아닌 자기 참조 방식.
-- 임시 테이블에 UNION ALL로 행을 늘리는 식으로 반복됨. 재귀를 실행했는데 새로운 행이 하나라도 추가되면, 그 추가된 행을 포함한 전체 결과 집합으로 재귀를 다시 실행
WITH RECURSIVE generation_cte(ID, PARENT_ID, GENERATION) AS(
    -- 1세대 정의: 부모가 없는 값들
    SELECT
        ID,
        PARENT_ID,
        1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT
        e.ID,
        e.PARENT_ID,
        g.GENERATION + 1
    FROM 
        ECOLI_DATA e
    JOIN -- 재귀: 이미 찾은 부모의 세대를 참조하여 현 개체의 세대가 정해짐
        generation_cte g ON e.PARENT_ID = g.ID 
)
-- 최종 쿼리
SELECT COUNT(*) AS COUNT, g.GENERATION
FROM generation_cte g
WHERE g.ID NOT IN (SELECT PARENT_ID FROM ECOLI_DATA WHERE PARENT_ID IS NOT NULL)
GROUP BY g.GENERATION
ORDER BY g.GENERATION


