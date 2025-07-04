SELECT AI.NAME, AI.DATETIME
FROM ANIMAL_INS AS AI
WHERE 
    NOT EXISTS(
      SELECT 1
      FROM ANIMAL_OUTS AS AO
      WHERE AI.ANIMAL_ID = AO.ANIMAL_ID)
ORDER BY DATETIME
LIMIT 3