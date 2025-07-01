SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE
  (OPTIONS LIKE '%열선시트%')    -- 열선시트 있으면 1, 아니면 0
  + (OPTIONS LIKE '%통풍시트%')  -- 통풍시트 있으면 1
  + (OPTIONS LIKE '%가죽시트%')  -- 가죽시트 있으면 1
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE