-- 2번 형질을 보유하지 않으면서 1이나 3형질을 포함한다 == 8로 나누었을 때의 나머지가 1, 4, 5 중 하나
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE GENOTYPE % 8 IN (1, 4, 5)