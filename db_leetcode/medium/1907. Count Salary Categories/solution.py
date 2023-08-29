import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    mp = {'Low Salary': 0,
        'Average Salary': 0,
        'High Salary': 0}

    for i in accounts['income'].values:
        if i < 20000:
            mp['Low Salary'] += 1
        elif i>=20000 and i<= 50000:
            mp['Average Salary'] += 1
        else:
            mp['High Salary'] += 1

    
    return pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'],
    'accounts_count': [mp['Low Salary'], mp['Average Salary'], mp['High Salary']]})
