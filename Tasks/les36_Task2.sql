SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

SELECT DISTINCT department_id
FROM employees;

SELECT *
FROM employees
ORDER BY first_name;

SELECT first_name || last_name AS 'Full name', salary, (salary * 0.12) AS PF
FROM employees;

SELECT MAX(salary), MIN(salary)
FROM employees;

SELECT ROUND(salary, 2) AS salary
FROM employees;
