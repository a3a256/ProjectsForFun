import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employees = employee["employee_id"].unique()
    mp = {"employee_id": [], "department_id": []}
    for i in employees:
        departments = employee[employee["employee_id"] == i]
        if len(departments) > 1:
            ans = departments[departments["primary_flag"] == "Y"]["department_id"].values[0]
        else:
            ans = departments["department_id"].values[0]
        mp["employee_id"] += [i]
        mp["department_id"] += [ans]
    
    return pd.DataFrame(mp)
