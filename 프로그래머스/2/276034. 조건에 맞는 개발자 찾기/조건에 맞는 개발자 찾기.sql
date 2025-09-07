-- 개발자의 SKILL_CODE와 원하는 기술의 CODE를 & 연산했을때 결과가 0이면 해당기술 없음
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE
                    FROM SKILLCODES
                    WHERE NAME = 'Python') != 0
      OR
      SKILL_CODE & (SELECT CODE
                    FROM SKILLCODES
                    WHERE NAME = 'C#') != 0
ORDER BY ID
                    
      