-- 올해의 평균 평가점수를 기준으로 GRADE와 BONUS를 계산한다. 
SELECT HE.EMP_NO,
       HE.EMP_NAME,
       CASE 
       WHEN TEMP.AVG >= 96 THEN 'S'
       WHEN TEMP.AVG >= 90 THEN 'A'
       WHEN TEMP.AVG >= 80 THEN 'B'
       ELSE 'C'
       END AS GRADE,
       CASE  
       WHEN TEMP.AVG >= 96 THEN SAL * 0.2
       WHEN TEMP.AVG >= 90 THEN SAL * 0.15
       WHEN TEMP.AVG >= 80 THEN SAL * 0.1
       ELSE 0
       END AS BONUS
-- 사원정보 테이블의 사번을 기준으로, 해당 사번의 올해 평균 평가점수를 조인한다.
FROM HR_EMPLOYEES HE JOIN (SELECT EMP_NO, AVG(SCORE) AS AVG
                          FROM HR_GRADE
                          GROUP BY EMP_NO) TEMP ON HE.EMP_NO = TEMP.EMP_NO
ORDER BY EMP_NO
