import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dd = {"teacher_id": [], "cnt": []}
    for i in teacher["teacher_id"].unique():
        dd["teacher_id"] += [i]
        dd["cnt"] += [teacher[teacher["teacher_id"] == i]["subject_id"].nunique()]
    return pd.DataFrame(dd)
