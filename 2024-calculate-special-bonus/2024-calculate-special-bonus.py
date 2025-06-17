import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[(employees['employee_id'] % 2 == 0) | (employees['name'].str[0] == 'M'), 'salary'] = 0
    df = employees[['employee_id', 'salary']].rename(columns={'salary': 'bonus'})
    df = df.sort_values(by='employee_id')
    return df

  