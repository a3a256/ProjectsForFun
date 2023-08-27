import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values('salary', inplace=True)
    nums = employee['salary'].unique()
    if len(nums) <= 1:
        return pd.DataFrame({'SecondHighestSalary': [np.nan]})

    return pd.DataFrame({'SecondHighestSalary': [nums[-2]]})
