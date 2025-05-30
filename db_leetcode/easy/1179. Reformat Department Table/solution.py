import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    dd = {"id": []}
    for i in months:
        dd["{}_Revenue".format(i)] = []

    for i in sorted(department["id"].unique()):
        dd["id"] += [i]
        for j in months:
            dd["{}_Revenue".format(j)] += [pd.NA]
    dd = pd.DataFrame(dd)
    for i in sorted(department["id"].unique()):
        for j in months:
            temp_df = department[(department["id"] == i) & (department["month"] == j)]
            if len(temp_df) > 0:
                dd.loc[dd["id"] == i, "{}_Revenue".format(j)] = temp_df["revenue"].values[0]

    return dd
