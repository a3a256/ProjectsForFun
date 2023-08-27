import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values('salary', inplace=True)
    nums = employee['salary'].unique()
    if len(nums) < N:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [np.nan]})
    
    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [nums[-N]]})
