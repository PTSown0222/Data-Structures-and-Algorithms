# Write your MySQL query statement below

# copy another employee table and compare
SELECT e.name as Employee
FROM Employee e, Employee m
WHERE e.managerId = m.id 
AND e.salary > m.salary;
