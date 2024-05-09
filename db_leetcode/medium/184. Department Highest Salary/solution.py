import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby("departmentId")
    maxed = pd.DataFrame(grouped["salary"].max())
    dd = {"Department": [], "Employee": [], "Salary": []}
    for i in range(maxed.shape[0]):
        depart = maxed.index[i]
        names = employee.loc[(employee["departmentId"] == depart) & (employee["salary"] == maxed.iloc[i, 0]), "name"].values
        department_names = department.loc[department["id"] == depart, "name"].values[0]
        dd["Department"] += [department_names]*len(names)
        dd["Employee"] += names.tolist()
        dd["Salary"] += [maxed.iloc[i, 0]]*len(names)
    
    return pd.DataFrame(dd)
