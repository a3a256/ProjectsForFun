import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    departments = employee["departmentId"].unique()
    dd = {"Department": [], "Employee": [], "Salary": []}
    for dep in departments:
        temp_df = employee[employee["departmentId"] == dep]
        dep_name = department.loc[department["id"] == dep, "name"].values[0]
        temp_df = temp_df.sort_values("salary", ascending=False)
        temp_df.reset_index(drop=True)
        money = sorted(temp_df["salary"].unique().tolist())
        money = money[-3:]
        for j in money:
            names = temp_df.loc[temp_df["salary"] == j, "name"].values.tolist()
            dd["Department"] += [dep_name]*len(names)
            dd["Employee"] += names
            dd["Salary"] += [j]*len(names)
    return pd.DataFrame(dd)
