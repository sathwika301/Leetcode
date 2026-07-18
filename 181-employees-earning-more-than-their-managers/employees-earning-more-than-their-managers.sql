# Write your MySQL query statement below
SELECT e.name  as Employee 
from  Employee e
WHERE e.salary>

(SELECT m.salary FROM Employee m
WHERE m.id=e.managerId)
