# Write your MySQL query statement below
SELECT id FROM (
    SELECT id,temperature,recordDate,
    LAG(temperature) OVER (ORDER BY recordDate) as prev_temp,
    LAG(recordDate) OVER(ORDER BY recordDate) as prev_date
FROM Weather
) AS t
WHERE temperature > prev_temp AND DATEDIFF(recordDate,prev_date)=1;

