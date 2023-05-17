SELECT first_name, last_name, department_name, employees.department_id
FROM employees
INNER JOIN department ON employees.department_id = department.department_id;

SELECT first_name, last_name, department_name, city, state_province
FROM employees
INNER JOIN department ON employees.department_id = department.department_id
INNER JOIN locations ON locations.location_id = department.location_id;

SELECT first_name, last_name, department_name, employees.department_id
FROM employees
INNER JOIN department ON employees.department_id = department.department_id
WHERE employees.department_id = 80 OR employees.department_id = 40;

SELECT department_name, first_name || ' ' || last_name AS 'Full name'
FROM department
LEFT JOIN employees ON department.department_id = employees.department_id;

SELECT e.first_name, m.first_name
FROM employees AS e
INNER JOIN employees as m ON e.employee_id = m.manager_id;

SELECT job_title, first_name || ' ' || last_name AS 'Full name', max_salary - salary as difference
FROM employees
INNER JOIN jobs ON employees.job_id = jobs.job_id;

SELECT job_title, avg(salary) AS Average_salary
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id
GROUP BY job_title;

SELECT first_name || ' ' || last_name AS Full_name, salary, city
FROM employees
JOIN department ON employees.department_id = department.department_id
JOIN locations ON department.location_id = locations.location_id
WHERE city = 'London';

SELECT department_name, COUNT(employee_id)
FROM department
LEFT JOIN employees USING(department_id)
GROUP BY department_name;