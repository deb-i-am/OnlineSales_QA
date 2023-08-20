# -*- coding: utf-8 -*-


import pandas as pd

df_dept = pd.read_csv("/content/Departments.csv")
df_emp = pd.read_csv("/content/Employees.csv")
df_sal = pd.read_csv("/content/Salaries.csv")
df_dept.head()

result = df_sal.merge(df_emp, left_on='EMP_ID', right_on='ID').merge(df_dept, left_on='DEPT ID', right_on='ID')
dept_avg_salaries = result.groupby('NAME_y')['AMT (USD)'].mean()
top_3_departments = dept_avg_salaries.nlargest(3)
top_3_departments
