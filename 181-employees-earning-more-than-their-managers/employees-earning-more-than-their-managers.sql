# Write your MySQL query statement below
SELECT e.name  as Employee 
FROM  Employee e JOIN Employee m
WHERE e.managerId=m.Id and e.salary> m.salary


