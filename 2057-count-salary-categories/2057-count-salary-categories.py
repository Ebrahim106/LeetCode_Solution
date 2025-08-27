import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category'] = pd.cut(accounts.income, bins=[0, 20000, 50001, accounts.income.max() + 1], right=False, labels=['Low Salary', 'Average Salary', 'High Salary'])
    return accounts.groupby('category', observed=False, as_index=False).account_id.nunique().rename(columns={'account_id' : 'accounts_count'})