SELECT d.NAME as DEPT_NAME, AVG(s.AMT) as AVG_MONTHLY_SALARY from Salaries s
    JOIN Employees e ON s.EMP_ID = e.ID
    JOIN Departments d ON d.ID = e.DEPT ID
    GROUP BY d.NAME ORDER BY AVG_MONTHLY_SALARY DESC LIMIT 3;

