import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    vals = []
    for i in range(len(employee)):
        if not pd.isnull(employee.iloc[i, -1]):
            temp = employee[employee["id"] == employee.iloc[i, -1]]
            if(len(temp)>0):
                if(temp["salary"].values[0] < employee.iloc[i, -2]):
                    vals += [employee.iloc[i, 1]]
    return pd.DataFrame({"Employee": vals})
